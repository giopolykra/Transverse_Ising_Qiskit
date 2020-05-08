import sys
import numpy as np
from numpy import array
from qiskit import *
from E import *
from angles import *
from circuit import *
from state_dict import *
from b_values_data import *
from scipy.optimize import minimize
from custom_optimizers import *
from b_values_data import *
import numpy.linalg as linalg
#error_calls = []
#momenta_calls = []
#opt_energy = []
#opt_param = []

#sys.stdout.write('HERE')

def init(param,a):  # usefull when optimizing layer by layer
    if N!=1:
        init = param[4*a-4:4*a]
    else:
        init = param[3*a-3:3*a]
    return(init)

def psi(param,N,layers,PBC):
#    list_en = list(eval('dict_en_HT_N{}J{}h{}'.format(N,J_name,h_name)).keys())
    qc0  = circuit1(N,param,layers, PBC = PBC, momentum = 0) #int(list_en[p][1])
    backend = Aer.get_backend('statevector_simulator')
    result = execute(qc0, backend).result()
    psi = result.get_statevector(qc0, decimals=5)
    psi = np.reshape(psi,(2**N,1))
    return(psi)

def base_term(param,N,layers,J,h,PBC,p,opt_param,epsilon):
    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
    energy = np.dot(psi(param,N,layers,PBC).conj().T,np.dot(H,psi(param,N,layers,PBC))).real
    return(energy[0][0])

def extra_term(param,N,layers,J,h,PBC,p,opt_param,epsilon):
    h_name = str(h[0]).replace(".","")
    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
    extra_term = np.dot(np.conjugate(psi(param,N,layers,PBC).T),np.dot(H,psi(param,N,layers,PBC))).real
    b = np.array(eval('b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),p)))*epsilon
    for k in range(len(b)):
        a = np.dot(psi(param,N,layers,PBC).conj().T,psi(opt_param[k],N,layers,PBC))
        a = a*np.dot(psi(opt_param[k],N,layers,PBC).conj().T,psi(param,N,layers,PBC))
        extra_term+=b[k]*a[0][0].real
    return(extra_term)

def error_callbacks(param,N,layers,J,h,PBC,p,error_calls):
    h_name = str(h[0]).replace(".","")
    state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())[p]
    a = np.dot(psi(param,N,layers,PBC).conj().T,state_th)
    a = a*np.dot(state_th.conj().T,psi(param,N,layers,PBC))
    error =  1- a[0].real
    error_calls.append(error)
# energy_calls = []

def momenta_callbacks(param,N,layers,J,h,PBC,p,momenta_calls):
    h_name = str(h[0]).replace(".","")
    T = eval('getT({})'.format(N))
    state = psi(param,N,layers,PBC)
    momenta = np.angle(np.dot(np.dot(state.conj().T,T),state)[0][0])
    if np.abs(momenta+np.pi)<1E-6:
        momenta = -1.*momanta
    momenta = momenta/np.pi
#    state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())[p]
#    momenta = np.angle(np.dot(np.dot(state_th.conj().T,T),state_th))/np.pi
    momenta_calls.append(momenta)

N = 4
K=2
J = [0,0,1]
h = [0.5,0,0]
PBC = True
layers = 2
Iter = 5
param = parameters(N,layers, PBC = PBC)
opt_param = [parameters(N,layers, PBC = PBC)]
momenta_calls = []
epsilon = 1
p=1
k=0
H = HeisenbergHamiltonian(N,J,h,PBC = PBC)
T = getT(N)

E1, E2 = linalg.eig(H)
U1, U2 = linalg.eig(T)
ind = E1.real.argsort()[::+1]
E1 = E1[ind].real
E2 = E2[:,ind]
states = []
a = []

momenta_th = []
energy_th = []
for k in range(len(E1)):
    locals()['state_{}'.format(k)] = []
    for i in range(len(E1)):
        locals()['state_{}'.format(k)].append(E2[i][k])
    locals()['state_{}'.format(k)] = np.asarray(eval('state_{}'.format(k)))
    p = np.angle(np.dot(np.dot(eval('state_{}'.format(k)).conj().T,T),eval('state_{}'.format(k))))/np.pi
    if abs(p)<1E-6: p=0
    momenta_th.append(p)
    energy_th.append( np.dot(np.dot(eval('state_{}'.format(k)),H),eval('state_{}'.format(k))).real)

print('momenta\x09->{}\nenergy\x09->{}'.format(momenta_th,energy_th))
#E0 = np.dot(np.dot(state.conj().T,H),state)
#U1 = np.angle(U1)/np.pi
#U1 = U1[ind]

#state0 = [0,0,0,0]
#state1 = np.zeros(2**N)
#state1[1] = -1
#state1[2] = 1
#state1 = np.reshape(state1,(2**N,1))
#momenta = np.dot(np.dot(state1.conj().T,T),state1)[0][0]
#momenta = np.angle(np.dot(np.dot(state1.conj().T,T),state1))/np.pi
#print(E0,'\n',E1,'\n',U1)
#a = np.dot(psi(param,N,layers,PBC).conj().T,psi(opt_param[k],N,layers,PBC))
#a = a*np.dot(psi(opt_param[k],N,layers,PBC).conj().T,psi(param,N,layers,PBC))
#
#state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),str(h[0]).replace(".",""),str(PBC))).values())[p]
#
#b = np.dot(psi(param,N,layers,PBC).conj().T,state_th)
#b = b*np.dot(state_th.conj().T,psi(param,N,layers,PBC))
#er = 1- b[0].real
#print(er)

#H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
#energy = np.dot(psi(x0,N,layers,PBC).conj().T,np.dot(H,psi(x0,N,layers,PBC)))
#print(energy)
#a = np.dot(psi(x0,N,layers,PBC).conj().T,psi(opt_param[0],N,layers,PBC))
#a = a*np.dot(psi(opt_param[0],N,layers,PBC).conj().T,psi(x0,N,layers,PBC))
#print(a[0][0].real)
#state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),str(h[0]).replace(".",""),str(PBC))).values())[p]
#a = np.abs(np.dot(np.conjugate(psi(x0,N,layers,PBC).T),state_th))
#print('First a:\x09',a)
#a  = np.dot(a.conj().T,a)
#print('Second a:\x09',a)
#error =  1- a[0][0]
#bs = base_term(x0,N,layers,J,h,PBC,p,opt_param,epsilon)
#print(bs)
#a = np.dot(psi(x0,N,layers,PBC).conj().T,psi(x0,N,layers,PBC))*np.dot(psi(x0,N,layers,PBC).conj().T,psi(x0,N,layers,PBC))
#print(a)
#ex = extra_term(x0,N,layers,J,h,PBC,p,opt_param,epsilon)
#print(ex)
#momenta_callbacks(x0,N,layers,J,h,PBC,p,momenta_calls)
#print(momenta_calls)
#H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
#for p in range(K):
#    if p==0:
#        ret = minimize(base_term,x0,args=(N,layers,J,h,PBC,p,opt_param,epsilon),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 100})
#        ret = [array(ret.x),ret.fun]
#        sys.stdout.write('end ret\x09->{}\n'.format(ret[1]))
#        sys.stdout.flush()
#        res_sequencial = sequencial_minimizer(base_term,ret[0],Iter,N,layers,J,h,PBC,p,opt_param,epsilon)
#        sys.stdout.write('end res_seq \x09-> {}\n'.format(res_sequencial[1]))
#        sys.stdout.flush()
#    else:
#        ret = minimize(extra_term,x0,args=(N,layers,J,h,PBC,p,opt_param,epsilon),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 100})
#        ret = [array(ret.x),ret.fun]
#        sys.stdout.write('end ret\x09->{}\n'.format(ret[1]))
#        sys.stdout.flush()
#        res_sequencial = sequencial_minimizer(extra_term,ret[0],Iter,N,layers,J,h,PBC,p,opt_param,epsilon)
#        sys.stdout.write('end res_seq \x09-> {}\n'.format(res_sequencial[1]))
#        sys.stdout.flush()

#T = getT(N)
##param = array([1.56921579, 6.907327  , 4.70751059, 6.28399227])
#param = array([8.23708555, 1.49911648, 2.95987606, 2.29404927, 5.48096309,
#       5.3336229 , 5.45160225, 5.3995599 ])
#my_little_array = error_callbacks(param,layers,N,J,h,PBC,p)
#print(error_calls)
#state0  = list(dict_vec_HT_N2J1h1_True.values())[p]
#state0 = np.array([state0])
#print('state0 shape ->\x09',state0.shape)
#print('state0.T shape ->\x09',state0.conjugate().T.shape)
#state1 = psi(param,layers,N,J,h,PBC)
#state1 = np.array([state1])
#print('state1 shape ->\x09',state1.shape)
#print('state1.T shape ->\x09',state1.conjugate().T.shape)
#energy0 = np.dot(np.dot(state0,H),state0.conjugate().T).real
#energy1 = np.dot(np.dot(state1,H),state1.conjugate().T).real
#momentum0 = np.angle(np.dot(np.dot(state0,T),state0.conjugate().T))/np.pi
#momentum1 = np.angle(np.dot(np.dot(state1,T),state1.conjugate().T))/np.pi
#result = np.dot(state0,state1.conjugate().T)*np.dot(state1,state0.conjugate().T)
#print('state0 ->\x09',state0,'\nstate1 ->\x09',state1)
#print('energy0 ->',energy0,'energy1 ->',energy1)
#print('momentum0 ->',momentum0,'momentum1->',momentum1)
#print('result ->',result.real)
#er = error_callbacks(param,layers,N,J,h,PBC,p)
#print('error_calls ->',error_calls)


#sys.stdout.write('{}\n'.format(base_term(param,layers,N,J,h,PBC,p,opt_param)))
#ret = minimize(base_term,param,args=(layers,N,J,h,PBC,p,opt_param),method='COBYLA',options={'maxiter': 10})
#ret = [ret.x,ret.fun]
#sys.stdout.write('ret -> {}\n'.format(ret))
#ret_seq = sequencial_minimizer(base_term,ret[0],Iter,layers,N,J,h,PBC,p,opt_param)
#sys.stdout.write('ret_seq -> {}\n'.format(ret_seq))
#opt_param_callbacks(ret_seq[0],opt_param)
#opt_energy.append(ret_seq[1])
#sys.stdout.write('opt_energy -> {}\n'.format(opt_energy))
#sys.stdout.write('opt_param -> {}\n'.format(opt_param))
#sys.stdout.flush()
#print(opt_energy)
#for p in range(1,K):
#    sys.stdout.write('k{}\n\n'.format(p))
#    sys.stdout.flush()
#    x0 = parameters(N,layers, PBC = PBC)
#    ret = minimize(extra_term,x0,args=(layers,N,J,h,PBC,p,opt_param),method='COBYLA',options={'maxiter': 10})
#    ret = [ret.x,ret.fun]
#    ret_seq = sequencial_minimizer(extra_term,ret[0],Iter,layers,N,J,h,PBC,p,opt_param)
#    opt_param_callbacks(ret_seq[0],opt_param)
#    opt_energy.append(ret_seq[1])
#    sys.stdout.write('opt_energy -> {}\n'.format(opt_energy))
#    sys.stdout.write('opt_param -> {}\n'.format(opt_param))
#    sys.stdout.flush()

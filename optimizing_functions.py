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
    return(psi)

def base_term(param,N,layers,J,h,PBC,p,opt_param,epsilon):
    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
    energy = np.dot(np.conjugate(psi(param,N,layers,PBC).T),np.dot(H,psi(param,N,layers,PBC))).real
    return(energy)

def extra_term(param,N,layers,J,h,PBC,p,opt_param,epsilon):
    h_name = str(h[0]).replace(".","")
    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
    extra_term = np.dot(np.conjugate(psi(param,N,layers,PBC).T),np.dot(H,psi(param,N,layers,PBC))).real
    b = np.array(eval('b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),p)))*epsilon
    for k in range(len(b)):
        extra_term+=b[k]*np.abs(np.dot(np.conjugate(psi(param,N,layers,PBC).T),psi(opt_param[k],N,layers,PBC)))**2
    return(extra_term)

def error_callbacks(param,N,layers,J,h,PBC,p,error_calls):
    h_name = str(h[0]).replace(".","")
    state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())[p]
    error =  1- np.abs(np.dot(np.conjugate(psi(param,N,layers,PBC).T),state_th))**2
    error_calls.append(error)
# energy_calls = []

def momenta_callbacks(param,N,layers,J,h,PBC,p,momenta_calls):
    h_name = str(h[0]).replace(".","")
    T = eval('getT({})'.format(N))
    state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())[p]
    momenta = np.angle(np.dot(np.dot(state_th.conj().T,T),state_th))/np.pi
    momenta_calls.append(momenta)

#def base_term(param,layers,N,J,h,PBC,p,opt_param):
#    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
#    state = psi(param,layers,N,J,h,PBC)
#    state = np.array([state])
#    energy = (np.dot(state,np.dot(H,state.conjugate().T)).real)[0]
#    return(energy[0])

#def extra_term(param,layers,N,J,h,PBC,p,opt_param):
#    h_name = str(h[0]).replace('.','')
#    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
#    state = psi(param,layers,N,J,h,PBC)
#    state = np.array([state])
#    #sys.stdout.write('state => {}\n'.format(state))
#    extra_term = np.dot(state,np.dot(H,state.conjugate().T)).real[0]
#    b = np.array(eval('b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),p)))
#    for k in range(len(b)):
#        state_old = psi(opt_param[k],layers,N,J,h,PBC)
#        #sys.stdout.write('state_old => {}\n'.format(state_old))
#        state_old = np.array([state_old])
#        extra_term += b[k]*(np.dot(state,state_old.conjugate().T).real)[0]**2
#    return(extra_term[0])

#def extra_term(param,layers,N,J,h,PBC,p,opt_param):
#    h_name = str(h[0]).replace('.','')
#    H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
#    state = psi(param,layers,N,J,h,PBC)
#    extra_term = np.dot(state,np.dot(H,state.conjugate().T)).real
#    b = np.array(eval('b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),p)))
#    for k in range(len(b)):
#        state_old = psi(opt_param[k],layers,N,J,h,PBC)
#        extra_term += b[k]*(np.dot(state,state_old.conjugate().T).real)**2
#    return extra_term

#def opt_param_callbacks(param,opt_param):
#    opt_param.append(np.array(param))
#
#def opt_energy_callbacks(x,opt_energy):
#    opt_energy.append(x)

#def error_callbacks(param,layers,N,J,h,PBC,p,error_calls):
#    h_name = str(h[0]).replace('.','')
#    state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())[p]
#    state_th = np.array([state_th])
#    state = psi(param,layers,N,J,h,PBC)
#    state = np.array([state])
#    error =  1- np.abs(np.dot(state,state_th.conjugate().T))**2
#    error_calls.append(error[0][0])
#
#def momenta_callbacks(param,N,J,h,PBC,p,momenta_calls):
#    h_name = str(h[0]).replace('.','')
#    T = eval('getT({})'.format(N))
#    state_th = list(eval('dict_vec_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())[p]
#    state_th = np.array([state_th])
#    momenta = np.angle(np.dot(np.dot(state_th,T),state_th.conjugate().T))/np.pi
#    momenta_calls.append(momenta[0][0])


#N = 2
#K=4
#J = [0,0,1]
#h = [0.5,0,0]
#PBC = True
#p=0
#layers = 2
#Iter = 5
#x0 = parameters(N,layers, PBC = PBC)
#opt_param = []
#epsilon = 1
#H = eval('HeisenbergHamiltonian({},{},{},PBC={})'.format(N,J,h,PBC))
#ret = minimize(base_term,x0,args=(N,layers,J,h,PBC,p,opt_param,epsilon),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 100})
#print(ret)

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

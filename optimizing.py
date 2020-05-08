import sys
import numpy as np
from numpy import array
from qiskit import *
from scipy.optimize import basinhopping
from scipy.optimize import minimize
from scipy.optimize import fmin_l_bfgs_b
from qiskit.aqua.components.optimizers import COBYLA, NELDER_MEAD, SLSQP, SPSA, ADAM, CG, L_BFGS_B,TNC
from E import *
from angles import *
from circuit import *
from state_dict import *
from custom_optimizers import *
from optimizing_functions import *

import pathlib
path = pathlib.Path().absolute()



def main_opt(Layers,Iter,N,K,J,PBC,Epsilon):
    la = ''.join(map(str, Layers))
    h0 = ''.join(map(str, [2]))
    file = open(str(path)+'/trials/N{}_Iter{}_h{}_layers{}_{}.py'.format(N,Iter,h0,la,str(PBC)),'w+')
    file.write('import numpy as np\n')
    file.write('from numpy import array\n')
#    if N==2 and K>4:
#        sys.stdout.write("There are only 4 eigenstates for N=2. Please provide K<5")
#        sys.stdout.flush()
    for epsilon in [1]:
        for layers in [3]:#
            # the bounds
            xmin = -np.ones(4*layers)*np.pi*2
            xmax = np.ones(4*layers)*np.pi*2
            # rewrite the bounds in the way required by PSO
            bounds = [(low, high) for low, high in zip(xmin, xmax)]
            for h_value in [0.5,1,2]:
                h_name = str(h_value).replace('.','')
                h = [h_value,0,0]
                error_calls = []
                momenta_calls = []
                opt_energy =[]
                opt_param =[]
                x0 = parameters(N,layers,PBC = PBC)
                locals()['Seq_en_N{}J1h{}_l{}_iter{}_e{}_{}'.format(N,h_name,layers,Iter,epsilon,str(PBC))] = []
                locals()['Seq_errors_N{}J1h{}_l{}_iter{}_e{}_{}'.format(N,h_name,layers,Iter,epsilon,str(PBC))] = []
                locals()['Seq_momenta_N{}J1h{}_l{}_iter{}_e{}_{}'.format(N,h_name,layers,Iter,epsilon,str(PBC))] = []
                for p in range(K):
                    if p!=0:
                        sys.stdout.write('N{}\x09k{}\x09h{}\x09layers{}\x09e{}\n'.format(N,p,h_value,layers,epsilon))
                        sys.stdout.flush()
                        ret = minimize(extra_term,x0,args=(N,layers,J,h,PBC,p,opt_param,epsilon),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 10})
                        ret = [array(ret.x),ret.fun]
                        sys.stdout.write('end ret\x09->{}\n'.format(ret[1]))
                        sys.stdout.flush()
                        res_sequencial = sequencial_minimizer(extra_term,ret[0],Iter,N,layers,J,h,PBC,p,opt_param,epsilon)
                        sys.stdout.write('end res_seq \x09-> {}\n'.format(res_sequencial[1]))
                        sys.stdout.flush()
                        opt_param.append(res_sequencial[0])
                        opt_energy.append(res_sequencial[1])
                        error_callbacks(res_sequencial[0],N,layers,J,h,PBC,p,error_calls)
                        sys.stdout.write('error\x09-> {}\n'.format(error_calls))
                        momenta_callbacks(res_sequencial[0],N,layers,J,h,PBC,p,momenta_calls)
                        sys.stdout.write('momenta\x09-> {}\n'.format(momenta_calls))
                        #sys.stdout.write('param \x09-> {}\n'.format(opt_param))
                        sys.stdout.flush()
                    else:
                        sys.stdout.write('N{}\x09k{}\x09h{}\x09layers{}\x09e{}\n'.format(N,p,h_value,layers,epsilon))
                        sys.stdout.flush()
                        ret = minimize(base_term,x0,args=(N,layers,J,h,PBC,p,opt_param,epsilon),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 10})
                        ret = [array(ret.x),ret.fun]
                        sys.stdout.write('end ret\x09->{}\n'.format(ret[1]))
                        sys.stdout.flush()
                        res_sequencial = sequencial_minimizer(base_term,ret[0],Iter,N,layers,J,h,PBC,p,opt_param,epsilon)
                        sys.stdout.write('end res_seq \x09-> {}\n'.format(res_sequencial[1]))
                        sys.stdout.flush()
                        opt_param.append(res_sequencial[0])
                        #sys.stdout.write('opt_param ->{}\n'.format(opt_param))
                        opt_energy.append(res_sequencial[1])
                        error_callbacks(res_sequencial[0],N,layers,J,h,PBC,p,error_calls)
                        sys.stdout.write('error\x09-> {}\n'.format(error_calls))
                        momenta_callbacks(res_sequencial[0],N,layers,J,h,PBC,p,momenta_calls)
                        sys.stdout.write('momenta\x09-> {}\n'.format(momenta_calls))
                    if p==K-1:
                        txt1 = "Seq_en_N{}J1h{}_l{}_iter{}_e{}_{} = np.array({})\n".format(N,h_name,layers,Iter,epsilon,str(PBC),opt_energy)
                        txt2 = "Seq_errors_N{}J1h{}_l{}_iter{}_e{}_{} = np.array({})\n".format(N,h_name,layers,Iter,epsilon,str(PBC),error_calls)
                        txt3 = "Seq_momenta_N{}J1h{}_l{}_iter{}_e{}_{} = np.array({})\n".format(N,h_name,layers,Iter,epsilon,str(PBC),momenta_calls)
                        file.write(txt1+txt2+txt3)
                txt4 = "Seq_param_N{}J1h{}_l{}_iter{}_e{}_{} = {}\n".format(N,h_name,layers,Iter,epsilon,str(PBC),opt_param)
                file.write(txt4)
    file.close()

N = 2
K = 4
Iter = 2
LAYERS = [1,2,3]
EPSILON = 1
J = [0,0,1]
#h0_array = [0.5,1,2,4,8,10,20]
PBC = True
h = [1,0,0]
opt_param = []
p=0
#for i in range(len(LAYERS)):
#    x0 = parameters(N,LAYERS[i],PBC)
#    ret = minimize(base_term,x0,args=(N,LAYERS[i],J,h,PBC,p,opt_param,EPSILON[0]),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 100})
#    print(ret)
main_opt(LAYERS,Iter,N,K,J,PBC,EPSILON)

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

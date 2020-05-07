import numpy as np
from numpy import array,kron,random,identity
from qiskit import *
import matplotlib.pyplot as plt
from numpy.linalg import inv
from E import *
from states import *
from angles import *
from circuit import *
from matrix_plot import *
from custom_optimizers import *
from optimizing_functions import *
from optimizing import *
import pathlib
from pathlib import Path
path = pathlib.Path().absolute()

N=2
K=4
Iter = 1
layers =5
J = [0,0,1]
h = [1,0,0]
PBC = True
#print(path)
#Create the libraries 'state_dict.py' and 'E_data' of theoretical eigenstates and eigenvectors
#file_a = Path(str(path)+"/state_dict.py")
#file_b = Path(str(path)+'/E_data.py')
#if file_a.is_file() == False:
#    theor_data()
#from state_dict import *
#if file_b.is_file() == False:
#    theo_k_data()

#main_opt(layers,Iter,N,K,J,h,PBC)
#param = parameters(N,layers,PBC = PBC)
#print(param)
#Plot the circuit to be used in the following computations
#qc = circuit1(N,param,layers,PBC = PBC)
#print("param={}".format(repr(param)))
#qc.draw(output="mpl")#, filename = 'my_circuit.png')
#plt.savefig(str(path)+'/trials/circuit.png')

#Plot a 2d representation of the Hamiltonian and Translation Operator
#and their mutual eigenvalues
plot_matrices(N,J,h,PBC)
plot_scatter(N,J,h,PBC)


#opt_param = []
#opt_energy = []
#
#for p in range(K):
#    if p==0:
#        sys.stdout.write('{}\n'.format(base_term(param,layers,N,J,h,PBC,p,opt_param)))
#        ret = minimize(base_term,param,args=(layers,N,J,h,PBC,p,opt_param),method='COBYLA',options={'maxiter': 100})
#        ret = [ret.x,ret.fun]
#        sys.stdout.write('ret -> {}\n'.format(ret))
##        ret_seq = sequencial_minimizer(base_term,ret[0],Iter,layers,N,J,h,PBC,p,opt_param)
##        sys.stdout.write('ret_seq -> {}\n'.format(ret_seq))
#        opt_param.append(ret[0])
#        opt_energy.append(ret[1])
#        sys.stdout.write('opt_energy -> {}\n'.format(opt_energy))
#        sys.stdout.write('opt_param -> {}\n'.format(opt_param))
#        sys.stdout.flush()
#        print(opt_energy)
#    else:
#        sys.stdout.write('k{}\n\n'.format(p))
#        sys.stdout.flush()
#        x0 = parameters(N,layers, PBC = PBC)
#        ret = minimize(extra_term,x0,args=(layers,N,J,h,PBC,p,opt_param),method='COBYLA',options={'maxiter': 100})
#        ret = [ret.x,ret.fun]
##        ret_seq = sequencial_minimizer(extra_term,ret[0],Iter,layers,N,J,h,PBC,p,opt_param)
#        opt_param.append(ret[0])
#        opt_energy.append(ret[1])
#        sys.stdout.write('opt_energy -> {}\n'.format(opt_energy))
#        sys.stdout.write('opt_param -> {}\n'.format(opt_param))
#        sys.stdout.flush()




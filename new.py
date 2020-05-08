import sys
import pathlib
path = pathlib.Path().absolute
sys.path.insert(0,str(path)+'/trials')
from E import *
from trials.E_diff import *
from trials.E_diff_criticality import *
#from trials.results_N2_Iter10_h0512481020_layers321_True import *
from optimizing_functions import *

from state_dict import *
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from trials.N2_Iter15_h2_layers123_True import *
from trials.results_N4_Iter15_h12481020_layers321_True import *

a = Seq_en_N2J1h05_l3_iter15_e1_True
N=4
J = [0,0,1]
h = [0.5,0,0]
layers = 3
epsilon = 1
PBC = True
K=4
T  = getT(N)
H = HeisenbergHamiltonian(N,J,h,PBC)
Energy = []
Momenta = []
Energy_th = []
Momenta_th = []
Error = []
for i in range(4):
    #params  = Seq_param_N2J1h05_l3_iter15_e1_True[i]
    params = Seq_param_N4J1h05_l3_iter15_e1_True[i]
    #print('params\x09->{}'.format(params))
    state = psi(params,N,layers,PBC)
    #print('state\x09->{}'.format(state))
    state = np.reshape(state, (2**N, 1))
    state_th = list(dict_vec_HT_N4J1h05_True.values())[i]
    state_th = np.reshape(state_th, (2**N, 1))
    #print(state_th)
    #print(state_th.conj().T.shape,'\n',state_th.conj().T)
    error = 1-(np.dot(state_th.conj().T,state))*(np.dot(state.conj().T,state_th))
    Error.append(error[0][0])
    energy_th = np.dot(np.dot(state_th.conj().T,H),state_th).real
    Energy_th.append(energy_th[0][0])
    momenta_th = np.angle(np.dot(np.dot(state_th.conj().T,T),state_th))[0][0]/np.pi
    Momenta_th.append(momenta_th)
    energy = np.dot(np.dot(state.conj().T,H),state).real
    Energy.append(energy[0][0])
    momenta = np.angle(np.dot(np.dot(state.conj().T,T),state))[0][0]/np.pi
    Momenta.append(momenta)
print('Energy_th\x09 -> {}\n Energy\x09 -> {}'.format(Energy_th,Energy))
print('Momenta_th\x09 -> {}\n Momenta\x09 -> {}'.format(Momenta_th,Momenta))
print('Error\x09 -> {}'.format(Error))
    #energy = np.dot(np.dot(state.conj().T,H),state).real
    #momentum_th = np.angle(np.dot(np.dot(state_th.conj().T,T),state))
    #momentum = np.angle(np.dot(np.dot(state.conj().T,T),state))
#    if abs(momentum+np.pi)<1E-6:
#        momentum = -1.*momentum
#    if abs(momentum_th+np.pi)<1E-6:
#        momentum_th = -1.*momentum_th
#    momentum = momentum/np.pi
#    momentum_th = momentum_th/np.pi
#    print('K = {}'.format(i))
#    print('state\x09-> {}\nmomentum ->\x09 {}\nmonetum_th ->\x09 {}'.format(state_th,momentum[0],momentum_th[0]))
#    print('energy \x09->{}\nenergy_th\x09->{}'.format(energy,energy_th))


#
#def en_diff():
#    file = open(str(path)+'/trials/E_diff.py','w+')
#    file.write('from numpy import array\n')
#    for N in [2]:
#        for i in [1,2,4,8,10,20]:
#            #print(log10(i*N))
#            h = str(i).replace(".","")
#            for layers in [1,2,3]:
#                for epsilon in [1,5,10]:
#                    for PBC in [True]:
#                        locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                        locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                        E_th = list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h,str(PBC))).values())
#                        E_sim = eval('Seq_en_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))
#                        for k in range(len(E_sim)):
#                            ED = abs(E_th[k]-E_sim[k])
#                            locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(ED)
#                            locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(log10(1/ED))
#                        file.write('{} = {}\n'.format('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#                        file.write('{} = {}\n'.format('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#        for i in [1]:
#            h = str(i).replace(".","")
#            for layers in [4,5]:
#                for epsilon in [1,5,10]:
#                    for PBC in [True]:
#                        locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                        locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                        E_th = list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h,str(PBC))).values())
#                        E_sim = eval('Seq_en_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))
#                        for k in range(len(E_sim)):
#                            ED = abs(E_th[k]-E_sim[k])
#                            locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(ED)
#                            locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(log10(1/ED))
#                        file.write('{} = {}\n'.format('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#                        file.write('{} = {}\n'.format('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#    file.close()

#def en_diff_crit():
#    file = open(str(path)+'/trials/E_diff_criticality.py','w+')
#    file.write('from numpy import array\n')
#    for N in [6,8]:
#        for epsilon in [1]:
#            for PBC in [True]:
#                if N==6:
#                    for layers in [1,2,3]:
#                        for i in [0.5,1,2]:
#                            h = str(i).replace(".","")
#                            locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                            locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                            E_th = list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h,str(PBC))).values())
#                            E_sim = eval('Seq_en_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))
#                            for k in range(len(E_sim)):
#                                ED = abs(E_th[k]-E_sim[k])
#                                locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(ED)
#                                locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(log10(1/ED))
#                            file.write('{} = {}\n'.format('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#                            file.write('{} = {}\n'.format('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#def en_diff_crit():
#    file = open(str(path)+'/trials/E_diff_criticality.py','w+')
#    file.write('from numpy import array\n')
#    for N in [8]:
#        for epsilon in [1]:
#            for PBC in [True]:
#                    for layers in [1,2,3,4]:
#                        for i in [1]:
#                            #sys.stdout.write('N={}\x09h = {}\x09\layers = {}\x09ED = {}'.format(N,h,layers))
#                            h = str(i).replace(".","")
#                            locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                            locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
#                            E_th = list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h,str(PBC))).values())
#                            E_sim = list(eval('Seq_en_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h,layers,epsilon,str(PBC))))
#                            ED = abs(E_th[0]-E_sim[0])
#                            sys.stdout.write('N={}\x09h = {}\x09\layers = {}\x09ED = {}'.format(N,h,layers,ED))
#                            locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(ED)
#                            locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(log10(1/ED))
#                            file.write('{} = {}\n'.format('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
#                            file.write('{} = {}\n'.format('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))






#en_diff()
#en_diff_crit()

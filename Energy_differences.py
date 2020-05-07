import math
from math import log10
import sys
import pathlib
from pathlib import Path
path = pathlib.Path().absolute()
sys.path.append(str(path)+'/trials')

from state_dict import *
from results_N2_Iter10_layers123_True import *
from results_N2_Iter10_h1_layers4_True import *
from results_N2_Iter10_h1_layers5_True import *

from results_N3_Iter10_h1_layers123_True import *

from results_N4_Iter10_h1_layers123_True import *

from results_N6_maxiter100_Iter10_h0512_layers123_True import *

from results_N8_maxiter100_Iter10_h0512_layers1234_True import *

from results_N10_maxiter100_Iter10_h0512_layers12345_True import *

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



def en_diff_crit():
    file = open(str(path)+'/trials/E_diff_criticality.py','w+')
    file.write('from numpy import array\n')
    for N in [2,3,4,6,8,10]:
        for epsilon in [1]:
            for PBC in [True]:
                if N==2:
                    L=3
                    h_array = [1]
                if N==3:
                    L=3
                    h_array = [1]
                if N==4:
                    L=3
                    h_array = [1]
                if N==6:
                    L=3
                    h_array = [0.5,1,2]
                if N==8:
                    L=4
                    h_array = [0.5,1,2]
                if N==10:
                    L=5
                    h_array = [0.5,1,2]
                for i in  h_array:
                    for layers in range(1,L+1):
                    #sys.stdout.write('N={}\x09h = {}\x09\layers = {}\x09ED = {}'.format(N,h,layers))
                        h = str(i).replace(".","")
                        locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
                        locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))]=[]
                        E_th = list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h,str(PBC))).values())
                        E_sim = list(eval('Seq_en_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h,layers,epsilon,str(PBC))))
                        for k in range(len(E_sim)):
                            ED = abs(E_th[k]-E_sim[k])
                            locals()['DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(ED)
                            locals()['logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC))].append(log10(1/ED))
                        sys.stdout.write('N={}\x09h = {}\x09layers = {}\x09ED = {}\n'.format(N,h,layers,ED))
                        file.write('{} = {}\n'.format('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('DE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
                        file.write('{} = {}\n'.format('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)),eval('logDE_N{}J1h{}_l{}_e{}_{}'.format(N,h,layers,epsilon,str(PBC)))))
    file.close()

en_diff_crit()


import sys
import pathlib
path = pathlib.Path().absolute
sys.path.insert(0,str(path)+'/trials')

from trials.E_diff import *
from trials.E_diff_criticality import *
#from trials.results_N2_Iter10_h0512481020_layers321_True import *
#from trials.results_N4_Iter15_h12481020_layers321_True import *
from trials.results_N2_Iter10_layers123_True import *
from trials.results_N2_Iter10_h1_layers4_True import *
from trials.results_N2_Iter10_h1_layers5_True import *
from trials.results_N3_Iter10_h1_layers123_True import *
from trials.results_N4_Iter10_h1_layers123_True import *
from trials.results_N6_maxiter100_Iter10_h0512_layers123_True import *
from trials.results_N8_maxiter100_Iter10_h0512_layers1234_True import *
from trials.results_N10_maxiter100_Iter10_h0512_layers12345_True import *
from optimizing_functions import *

from state_dict import *
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import numpy as np
from numpy import array

fig, axs = plt.subplots(nrows = 2)
plt.subplots_adjust(hspace=0.4, wspace=0.2)
fig.suptitle('Cobyla maxiter 100 | Sequential: COBYLA iter = 10 maxiter = 10',y=1,fontsize=20)
axs[0].title.set_text("Layers: h=1")
axs[0].title.set_size(20)
for N in [2,3,4,6,8,10]:
    for e in [1]:
        if N==2:
            L = 5
            h_array = [1]
        if N==3:
            L = 3
            h_array = [1]
        if N==4:
            L = 3
            h_array = [1]
        if N==6:
            L = 3
            h_array = [0.5,1,2]
        if N==8:
            L = 4
            h_array = [0.5,1,2]
        if N==10:
            L = 5
            h_array = [0.5,1,2]
        for i in  h_array:
            h = str(i).replace(".","")
            locals()['y_N{}'.format(N)] = []
            locals()['x0_N{}_h{}_e{}'.format(N,h,e)] = []
            locals()['x1_N{}_h{}_e{}'.format(N,h,e)] = []
            for l in range(1,L+1):
                locals()['y_N{}'.format(N)].append(l)
                locals()['x0_N{}_h{}_e{}'.format(N,h,e)].append(eval('DE_N{}J1h{}_l{}_e{}_True'.format(N,h,l,e))[0])
                locals()['x1_N{}_h{}_e{}'.format(N,h,e)].append(eval('logDE_N{}J1h{}_l{}_e{}_True'.format(N,h,l,e))[0])

axs[0].plot(x0_N2_h1_e1,y_N2, linestyle='-',linewidth = 3.0, marker='>',color ='#00ffff', label = 'N=2 h=1' )
axs[0].plot(x0_N3_h1_e1,y_N3, linestyle='-',linewidth = 3.0, marker='>',color ='#ff99cc', label = 'N=3 h=1' )
axs[0].plot(x0_N4_h1_e1,y_N4, linestyle='-',linewidth = 3.0, marker='>',color ='#ffff00', label = 'N=4 h=1' )
axs[0].plot(x0_N6_h1_e1,y_N6, linestyle='-',linewidth = 3.0, marker='>',color ='#0000ff', label = 'N=6 h=1' )
axs[0].plot(x0_N8_h1_e1,y_N8, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600', label = 'N=8 h=1' )
axs[0].plot(x0_N10_h1_e1,y_N10, linestyle='-',linewidth = 3.0, marker='>',color ='#009933', label = 'N=10 h=1' )

axs[0].plot(x0_N6_h2_e1,y_N6, linestyle='-',linewidth = 3.0, marker='^',color ='#009999', label = 'N=6 h=2' )
axs[0].plot(x0_N8_h2_e1,y_N8, linestyle='-',linewidth = 3.0, marker='^',color ='#663300', label = 'N=8 h=2' )
axs[0].plot(x0_N10_h2_e1,y_N10, linestyle='-',linewidth = 3.0, marker='^',color ='#999966', label = 'N=10 h=2' )

axs[0].set(xlabel='$\Delta E$', ylabel='Depth')
axs[0].yaxis.label.set_size(15)
axs[0].xaxis.label.set_size(15)
axs[0].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
axs[0].yaxis.set_major_locator(MaxNLocator(integer=True))
axs[0].grid()


axs[1].plot(x1_N6_h05_e1,y_N6, linestyle='-',linewidth = 3.0, marker='>',color ='#ffc266', label = 'N=6 h=0.5' )
axs[1].plot(x1_N8_h05_e1,y_N8, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6666', label = 'N=8 h=0.5' )
axs[1].plot(x1_N10_h05_e1,y_N10, linestyle='-',linewidth = 3.0, marker='>',color ='#ff66b3', label = 'N=10 h=0.5' )

axs[1].plot(x1_N2_h1_e1,y_N2, linestyle='-',linewidth = 3.0, marker='>',color ='#00ffff', label = 'N=2 h=1' )
axs[1].plot(x1_N3_h1_e1,y_N3, linestyle='-',linewidth = 3.0, marker='>',color ='#ff99cc', label = 'N=3 h=1' )
axs[1].plot(x1_N4_h1_e1,y_N4, linestyle='-',linewidth = 3.0, marker='>',color ='#ffff00', label = 'N=4 h=1' )
axs[1].plot(x1_N6_h1_e1,y_N6, linestyle='-',linewidth = 3.0, marker='>',color ='#0000ff', label = 'N=6 h=1' )
axs[1].plot(x1_N8_h1_e1,y_N8, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600', label = 'N=8 h=1' )
axs[1].plot(x1_N10_h1_e1,y_N10, linestyle='-',linewidth = 3.0, marker='>',color ='#009933', label = 'N=10 h=1' )

axs[1].plot(x1_N6_h2_e1,y_N6, linestyle='-',linewidth = 3.0, marker='>',color ='#009999', label = 'N=6 h=2' )
axs[1].plot(x1_N8_h2_e1,y_N8, linestyle='-',linewidth = 3.0, marker='>',color ='#663300', label = 'N=8 h=2' )
axs[1].plot(x1_N10_h2_e1,y_N10, linestyle='-',linewidth = 3.0, marker='>',color ='#999966', label = 'N=10 h=2' )

axs[1].set(xlabel='$log_{10}(1/\epsilon)$', ylabel='Depth')
axs[1].yaxis.label.set_size(15)
axs[1].xaxis.label.set_size(15)
axs[1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
axs[1].yaxis.set_major_locator(MaxNLocator(integer=True))
axs[1].grid()

plt.savefig(str(pathlib.Path().cwd())+'/trials/log.png')
plt.show()

#for n in [2,6]:
#    for e in [3]:
#        for l in [1,2,3]:
#            if n==2:
#                for k in range(4):
#                    locals()['Seq_l{}_{}d_e{}_k{}'.format(l,n,e,k)] = {}
#                    locals()['Seq_errors_l{}_{}d_e{}_k{}'.format(l,n,e,k)] = {}
#                    for h in [1,2,4,8,10,20]:
#                        locals()['Seq_l{}_{}d_e{}_k{}'.format(l,n,e,k)]['h{}j{}'.format(h,1)] = eval('Seq_h{}j1_l{}_{}d_zero_PBC'.format(h,l,n))[k]
#                        locals()['Seq_errors_l{}_{}d_e{}_k{}'.format(l,n,e,k)]['h{}j{}'.format(h,1)] = eval('Seq_errors_h{}j1_l{}_{}d_zero_PBC'.format(h,l,n))[k]
#                    print('Seq_l{}_{}d_e{}_k{} = '.format(l,n,e,k), eval('Seq_l{}_{}d_e{}_k{}'.format(l,n,e,k)),'\n')
#                    print('Seq_errors_l{}_{}d_e{}_k{} = '.format(l,n,e,k), eval('Seq_errors_l{}_{}d_e{}_k{}'.format(l,n,e,k)),'\n')
#
#for N in [2,4]:
#    if N==2:
#        Iter = 10
#        K = 4
#        L = 3
#        h_array = [0.5,1,2,4,8,10,20]
#    if N==4:
#        Iter = 15
#        K = 4
#        L = 3
#        h_array = [1,2,4,8,10,20]
#    for PBC in [True]:
#        for e in [1,5,10]:
#            for k in range(K):
#                for l in range(1,L+1):
#                    locals()['y_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    locals()['y_diff_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    locals()['y_errors_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    locals()['yE_{}d_k{}'.format(N,k)] = []
#                    locals()['yP_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    locals()['y_momenta_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    for h in h_array:
#                        h_name = str(h).replace(".","")
#                        locals()['y_l{}_{}d_e{}_k{}'.format(l,N,e,k)].append(eval('Seq_en_N{}J1h{}_l{}_iter{}_e{}_{}'.format(N,h_name,l,Iter,e,str(PBC)))[k])
#                        locals()['y_errors_l{}_{}d_e{}_k{}'.format(l,N,e,k)].append(eval('Seq_errors_N{}J1h{}_l{}_iter{}_e{}_{}'.format(N,h_name,l,Iter,e,str(PBC)))[k])
#                        locals()['yP_l{}_{}d_e{}_k{}'.format(l,N,e,k)].append(list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h_name,str(PBC))).keys())[k][1])
#                        locals()['y_momenta_l{}_{}d_e{}_k{}'.format(l,N,e,k)].append(eval('Seq_momenta_N{}J1h{}_l{}_iter{}_e{}_{}'.format(N,h_name,l,Iter,e,str(PBC)))[k])
#                        locals()['yE_{}d_k{}'.format(N,k)].append(list(eval('dict_en_HT_N{}J1h{}_{}'.format(N,h_name,str(PBC))).values())[k])
#                    locals()['y_diff_l{}_{}d_e{}_k{}'.format(l,N,e,k)]=np.array(locals()['y_l{}_{}d_e{}_k{}'.format(l,N,e,k)])-np.array(locals()['yE_{}d_k{}'.format(N,k)])
#                locals()['ypsi_errors_2d'.format(k)] = []
#                locals()['ypsi_errors_2d'.format(k)] = np.zeros(2)
#for N in [2,4]:
#    for e in [1,5,10]:
#        fig, axs = plt.subplots(nrows=4,ncols=3, figsize=(25, 10))
#        plt.subplots_adjust(hspace=0.4, wspace=0.2)
#        if N==2:
#            fig.suptitle(' N={} | epsilon = {} \n All: Cobyla maxiter 100 | Sequential: COBYLA iter = 15 maxiter = 10'.format(N,e),y=1,fontsize=20)
#            xcouplings = ['h05j1','h1j1', 'h2j1', 'h4j1', 'h8j1', 'h10j1', 'h20j']
#        if N==4:
#            fig.suptitle(' N={} | epsilon = {} \n All: Cobyla maxiter 100 | Sequential: COBYLA iter = 10 maxiter = 10'.format(N,e),y=1,fontsize=20)
#            xcouplings = ['h1j1', 'h2j1', 'h4j1', 'h8j1', 'h10j1', 'h20j']
#        for l in [1,2,3]:
#            axs[0,l-1].title.set_text("Layers: {}".format(l))
#            axs[0,l-1].title.set_size(20)
#            axs[0,l-1].plot(xcouplings,np.array(eval('y_l{}_{}d_e{}_k0'.format(l,N,e)))/2, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#            axs[0,l-1].plot(xcouplings,np.array(eval('y_l{}_{}d_e{}_k1'.format(l,N,e)))/2, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#            axs[0,l-1].plot(xcouplings,np.array(eval('y_l{}_{}d_e{}_k2'.format(l,N,e)))/2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#            axs[0,l-1].plot(xcouplings,np.array(eval('y_l{}_{}d_e{}_k3'.format(l,N,e)))/2, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#            axs[0,l-1].plot(xcouplings,np.array(eval('yE_{}d_k0'.format(N)))/2, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#            axs[0,l-1].plot(xcouplings,np.array(eval('yE_{}d_k1'.format(N)))/2, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#            axs[0,l-1].plot(xcouplings,np.array(eval('yE_{}d_k2'.format(N)))/2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#            axs[0,l-1].plot(xcouplings,np.array(eval('yE_{}d_k3'.format(N)))/2, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#            axs[0,l-1].grid()
#
#            axs[1,l-1].plot(xcouplings,eval('y_diff_l{}_{}d_e{}_k0'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600',label = 'Ground State' )
#            axs[1,l-1].plot(xcouplings,eval('y_diff_l{}_{}d_e{}_k1'.format(l,N,e,k)), linestyle='-',linewidth = 3.0, marker='>',color ='#088A08',label = '1st Excited' )
#            axs[1,l-1].plot(xcouplings,eval('y_diff_l{}_{}d_e{}_k2'.format(l,N,e,k)), linestyle='-',linewidth = 3.0, marker='>',color ='#b30000',label = '2nd Excited' )
#            axs[1,l-1].plot(xcouplings,eval('y_diff_l{}_{}d_e{}_k3'.format(l,N,e,k)), linestyle='-',linewidth = 3.0, marker='>',color ='#2E9AFE',label = '3nd Excited' )
#            axs[1,l-1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#            axs[1,l-1].xaxis.set_major_locator(MaxNLocator(integer=True))
#            axs[1,l-1].grid()
#            axs[2,l-1].plot(xcouplings,eval('y_errors_l{}_{}d_e{}_k0'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#            axs[2,l-1].plot(xcouplings,eval('y_errors_l{}_{}d_e{}_k1'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#            axs[2,l-1].plot(xcouplings,eval('y_errors_l{}_{}d_e{}_k2'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#            axs[2,l-1].plot(xcouplings,eval('y_errors_l{}_{}d_e{}_k3'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#            axs[2,l-1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#            axs[2,l-1].xaxis.set_major_locator(MaxNLocator(integer=True))
#            axs[2,l-1].grid()
#            axs[3,l-1].plot(xcouplings,eval('y_momenta_l{}_{}d_e{}_k0'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#            axs[3,l-1].plot(xcouplings,eval('y_momenta_l{}_{}d_e{}_k1'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#            axs[3,l-1].plot(xcouplings,eval('y_momenta_l{}_{}d_e{}_k2'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#            axs[3,l-1].plot(xcouplings,eval('y_momenta_l{}_{}d_e{}_k3'.format(l,N,e)), linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#            axs[3,l-1].plot(xcouplings,eval('yP_l{}_{}d_e{}_k0'.format(l,N,e)), linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#            axs[3,l-1].plot(xcouplings,eval('yP_l{}_{}d_e{}_k1'.format(l,N,e)), linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#            axs[3,l-1].plot(xcouplings,eval('yP_l{}_{}d_e{}_k2'.format(l,N,e)), linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#            axs[3,l-1].plot(xcouplings,eval('yP_l{}_{}d_e{}_k3'.format(l,N,e)), linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#            axs[3,l-1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#            axs[3,l-1].xaxis.set_major_locator(MaxNLocator(integer=True))
#            axs[3,l-1].grid()
#
#
#            for ax in axs[0,:].flat:
#                ax.set(xlabel='Couplings J/h', ylabel='Energy/N')
#                #ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.74, 1., .10))
#                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#                ax.yaxis.label.set_size(15)
#                ax.xaxis.label.set_size(15)
#            for ax in axs[1,:].flat:
#                ax.set(xlabel='Couplings J/h', ylabel='$\Delta E$')
#                #ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#                ax.yaxis.label.set_size(15)
#                ax.xaxis.label.set_size(15)
#            for ax in axs[2,:].flat:
#                ax.set(xlabel='Couplings J/h', ylabel='$\epsilon=1-|<\psi_{sim}|\psi_{th}>|^2$')
#                #ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#                ax.yaxis.label.set_size(15)
#                ax.xaxis.label.set_size(15)
#            for ax in axs[3,:].flat:
#                ax.set(xlabel='Couplings J/h', ylabel='Momenta')
#                #ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#                ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#                ax.yaxis.label.set_size(15)
#                ax.xaxis.label.set_size(15)
#        plt.savefig(str(pathlib.Path().cwd())+'/trials/en_e{}.png'.format(e))
#plt.show()




#fig, axs = plt.subplots(nrows=3,ncols=3, figsize=(25, 10))
#plt.subplots_adjust(hspace=0.4, wspace=0.2)
#fig.suptitle(' N=2 | epsilon = 5 \n All: Cobyla maxiter 100 | Sequential: COBYLA iter = 15 maxiter = 10',y=1,fontsize=20)
#
#
#xcouplings = ['h05j1','h1j1', 'h2j1', 'h4j1', 'h8j1', 'h10j1', 'h20j1']
#xcouplings1 = ['h1j1', 'h2j1', 'h4j1', 'h8j1', 'h10j1', 'h20j1']
#xcouplings2 = np.linspace(1,0,11)
#
##print(y_momenta_l1_2d_e1_k0)
#axs[0,0].title.set_text("Layers: 1")
#axs[0,0].title.set_size(20)
#axs[0,0].plot(  xcouplings,np.array(y_l1_2d_e5_k0)/2, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#axs[0,0].plot(  xcouplings,np.array(y_l1_2d_e5_k1)/2, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#axs[0,0].plot(  xcouplings,np.array(y_l1_2d_e5_k2)/2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#axs[0,0].plot(  xcouplings,np.array(y_l1_2d_e5_k3)/2, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#
#axs[0,0].plot(  xcouplings,np.array(yE_2d_k0)/2, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[0,0].plot(  xcouplings,np.array(yE_2d_k1)/2, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[0,0].plot(  xcouplings,np.array(yE_2d_k2)/2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[0,0].plot(  xcouplings,np.array(yE_2d_k3)/2, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#
#axs[0,0].grid()
#
#axs[0,1].title.set_text("Layers: 2")
#axs[0,1].title.set_size(20)
#axs[0,1].plot(  xcouplings,np.array(y_l2_2d_e5_k0)/2, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#axs[0,1].plot(  xcouplings,np.array(y_l2_2d_e5_k1)/2, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#axs[0,1].plot(  xcouplings,np.array(y_l2_2d_e5_k2)/2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#axs[0,1].plot(  xcouplings,np.array(y_l2_2d_e5_k3)/2, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#
#axs[0,1].plot(  xcouplings,np.array(yE_2d_k0)/2, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[0,1].plot(  xcouplings,np.array(yE_2d_k1)/2, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[0,1].plot(  xcouplings,np.array(yE_2d_k2)/2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[0,1].plot(  xcouplings,np.array(yE_2d_k3)/2, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#axs[0,1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[0,1].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[0,1].grid()
#
#axs[0,2].title.set_text("Layers: 3")
#axs[0,2].title.set_size(20)
#axs[0,2].plot(  xcouplings,np.array(y_l3_2d_e5_k0)/2, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#axs[0,2].plot(  xcouplings,np.array(y_l3_2d_e5_k1)/2, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#axs[0,2].plot(  xcouplings,np.array(y_l3_2d_e5_k2)/2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#axs[0,2].plot(  xcouplings,np.array(y_l3_2d_e5_k3)/2, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#
#axs[0,2].plot(  xcouplings,np.array(yE_2d_k0)/2, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[0,2].plot(  xcouplings,np.array(yE_2d_k1)/2, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[0,2].plot(  xcouplings,np.array(yE_2d_k2)/2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[0,2].plot(  xcouplings,np.array(yE_2d_k3)/2, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#axs[0,2].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[0,2].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[0,2].grid()
#
#axs[1,0].plot(  xcouplings,y_errors_l1_2d_e5_k0, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[1,0].plot(  xcouplings,y_errors_l1_2d_e5_k1, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[1,0].plot(  xcouplings,y_errors_l1_2d_e5_k2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[1,0].plot(  xcouplings,y_errors_l1_2d_e5_k3, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
##axs[1,0].plot(  xcouplings,ypsi_errors_1d, linestyle='--',linewidth = 3.0, marker='>',color ='#070719' ,label = 'theory')
#axs[1,0].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[1,0].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[1,0].grid()
#
#
#axs[1,1].plot(  xcouplings,y_errors_l2_2d_e5_k0, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[1,1].plot(  xcouplings,y_errors_l2_2d_e5_k1, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[1,1].plot(  xcouplings,y_errors_l2_2d_e5_k2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[1,1].plot(  xcouplings,y_errors_l2_2d_e5_k3, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#axs[1,1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[1,1].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[1,1].grid()
#
#axs[1,2].plot(  xcouplings,y_errors_l3_2d_e5_k0, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[1,2].plot(  xcouplings,y_errors_l3_2d_e5_k1, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[1,2].plot(  xcouplings,y_errors_l3_2d_e5_k2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[1,2].plot(  xcouplings,y_errors_l3_2d_e5_k3, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#axs[1,2].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[1,2].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[1,2].grid()
#
#axs[2,0].plot(  xcouplings,y_momenta_l1_2d_e5_k0, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#axs[2,0].plot(  xcouplings,y_momenta_l1_2d_e5_k1, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#axs[2,0].plot(  xcouplings,y_momenta_l1_2d_e5_k2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#axs[2,0].plot(  xcouplings,y_momenta_l1_2d_e5_k3, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#
#axs[2,0].plot(  xcouplings,yP_l1_2d_e5_k0, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[2,0].plot(  xcouplings,yP_l1_2d_e5_k1, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[2,0].plot(  xcouplings,yP_l1_2d_e5_k2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[2,0].plot(  xcouplings,yP_l1_2d_e5_k3, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#axs[2,0].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[2,0].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[2,0].grid()
#
#axs[2,1].plot(  xcouplings,y_momenta_l1_2d_e5_k0, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#axs[2,1].plot(  xcouplings,y_momenta_l1_2d_e5_k1, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#axs[2,1].plot(  xcouplings,y_momenta_l1_2d_e5_k2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#axs[2,1].plot(  xcouplings,y_momenta_l1_2d_e5_k3, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#
#axs[2,1].plot(  xcouplings,yP_l1_2d_e5_k0, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[2,1].plot(  xcouplings,yP_l1_2d_e5_k1, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[2,1].plot(  xcouplings,yP_l1_2d_e5_k2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[2,1].plot(  xcouplings,yP_l1_2d_e5_k3, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
#axs[2,1].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[2,1].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[2,1].grid()
#
#axs[2,2].plot(  xcouplings,y_momenta_l1_2d_e5_k0, linestyle='-',linewidth = 3.0, marker='>',color ='#ff6600' )
#axs[2,2].plot(  xcouplings,y_momenta_l1_2d_e5_k1, linestyle='-',linewidth = 3.0, marker='^',color ='#088A08' )
#axs[2,2].plot(  xcouplings,y_momenta_l1_2d_e5_k2, linestyle='-',linewidth = 3.0, marker='*',color ='#b30000' )
#axs[2,2].plot(  xcouplings,y_momenta_l1_2d_e5_k3, linestyle='-',linewidth = 3.0, marker='o',color ='#2E9AFE' )
#
#axs[2,2].plot(  xcouplings,yP_l1_2d_e5_k0, linestyle='--',linewidth = 3.0, marker='>',color ='#ff6600' ,label = 'Ground State')
#axs[2,2].plot(  xcouplings,yP_l1_2d_e5_k1, linestyle='--',linewidth = 3.0, marker='^',color ='#088A08' ,label = '1st Excited')
#axs[2,2].plot(  xcouplings,yP_l1_2d_e5_k2, linestyle='--',linewidth = 3.0, marker='*',color ='#b30000' ,label = '2nd Excited')
#axs[2,2].plot(  xcouplings,yP_l1_2d_e5_k3, linestyle='--',linewidth = 3.0, marker='o',color ='#2E9AFE' ,label = '3rd Excited')
##axs[2,1].plot(  xcouplings,ypsi_errors_1d, linestyle='--',linewidth = 3.0, marker='>',color ='#070719' ,label = 'theory')
#axs[2,2].legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#axs[2,2].xaxis.set_major_locator(MaxNLocator(integer=True))
#axs[2,2].grid()
#
#for ax in axs[0,:].flat:
#    ax.set(xlabel='Couplings J/h', ylabel='Energy/N')
#    ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.74, 1., .10))
#    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#    ax.yaxis.label.set_size(15)
#    ax.xaxis.label.set_size(15)
#for ax in axs[1,:].flat:
#    ax.set(xlabel='Couplings J/h', ylabel='$\epsilon=1-|<\psi_{sim}|\psi_{th}>|^2$')
#    ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#    ax.yaxis.label.set_size(15)
#    ax.xaxis.label.set_size(15)
#for ax in axs[2,:].flat:
#    ax.set(xlabel='Couplings J/h', ylabel='Momenta')
#    ax.legend(shadow=False,framealpha=0.7, ncol=2,fancybox=True,bbox_to_anchor=(0., 0.84, 1., .10))
#    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
#    ax.yaxis.label.set_size(15)
#    ax.xaxis.label.set_size(15)
#
#plt.savefig(str(athlib.Path().cwd())+'/trials/en_e5.png')
#plt.show()



#for N in [2]:
#    if N==2 or N==4:
#        K = 4
#        L = 3
#        h_array = [0.5,1,2,4,8,10,20]
#    if N==4:
#        K = 4
#        L = 3
#        h_array = [1]
#    for PBC in [True]:
#        for e in [1,5,10]:
#            for k in range(K):
#                for l in range(1,L+1):
#                    locals()['y_state_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    locals()['yS_th_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    locals()['y_errors_l{}_{}d_e{}_k{}'.format(l,N,e,k)] = []
#                    for h in h_array:
#                        h_name = str(h).replace(".","")
#                        param = list(eval('Seq_param_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h_name,l,e,str(PBC))))[k]
#                        state = psi(param,N,l,PBC)
#                        state_th = list(eval('dict_vec_HT_N{}J1h{}_{}'.format(N,h_name,str(PBC))).values())[k]
#                        cross = np.dot(state_th.conjugate().T,state).real
#                        error = 1-cross**2
#                        locals()['y_errors_l{}_{}d_e{}_k{}'.format(l,N,e,k)].append(error)
#                    print(eval('y_errors_l{}_{}d_e{}_k{}'.format(l,N,e,k)))
#e=1
#N=2
#PBC = True
#for l in [1,2,3]:
#    for h in [0.5,1,2,4,8,10,20]:
#        h_name = str(h).replace(".","")
#        for k in [1]:
#            a = list(eval('Seq_param_N{}J1h{}_l{}_iter10_e{}_{}'.format(N,h_name,l,e,str(PBC))))[k]
#            state = psi(a,N,l,PBC)
#            state_th = list(eval('dict_vec_HT_N{}J1h{}_{}'.format(N,h_name,str(PBC))).values())[k]
#            cross = np.dot(state_th.conjugate().T,state).real
#            error = 1-cross**2
#            print('N {}\x09h {}\x09layers {} \x09error -> {}'.format(N,h,l,error))

import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy.linalg as linalg
import numpy as np
import pathlib
path = pathlib.Path().absolute()

from E import *

def plot_matrices(N,J,h,PBC = True):

    H = HeisenbergHamiltonian(N,J,h,PBC = PBC)
    T = getT(N)
    # For testing the simultanious diagonalization may not work -> Plot the matrices in 2d
    HT = H+0.001*T
    U1, U2 = linalg.eig(HT)
    idx = U1.real.argsort()[::+1]
    U1 = U1[idx]
    U2 = U2[:,idx]

    energies, en_vec = linalg.eig(H)
    momenta, mom_vec = linalg.eig(T)
    momenta = np.angle(momenta)
    ind = energies.real.argsort()[::+1]
    energies = energies[ind]
    momenta = momenta[ind]

    # Identify -pi with pi
    ind2 = np.where(np.abs(momenta+np.pi) <1E-6)
    momenta[ind2] = -1.* momenta[ind2]

    Hd = np.dot(np.dot(U2.conj().T,H),U2).real
    Td = np.dot(np.dot(U2.conj().T,T),U2).real
    Matrices1 = [Hd,Td]
    Matrices = []

    for M1 in Matrices1:
        Matrices.append(M1)

    fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(22, 10))

    text = ['Hamiltonian','Translation Operator']

    for ax,txt,M in zip(ax.flat,text,Matrices):
        ax.set(xlabel='state')
        ax.set(ylabel='state')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.yaxis.label.set_size(24)
        ax.xaxis.label.set_size(24)
        im = ax.imshow(M.real)
        ax.set_title("{}".format(txt),fontdict={'fontsize': 24 })#rcParams['axes.titlesize']
        fig.colorbar(im,ax=ax)
        for i in range(len(M)):
            for j in range(len(M)):
                if np.abs(M[i][j])>1E-10:
                    c = np.round(M[i][j].real,4)
                    ax.text(i, j, c, va='center', ha='center',color ='#71ACB3',fontsize=14)
    plt.savefig(str(path)+'/trials/matrices.png')
    plt.show()

def plot_scatter(N,J,h,PBC):

    H = HeisenbergHamiltonian(N,J,h,PBC = PBC)
    T = getT(N)

    HT = H+0.001*T
    U1, U2 = linalg.eig(HT)
    idx = U1.real.argsort()[::+1]
    U1 = U1[idx]
    U2 = U2[:,idx]
#     energies, en_vec = linalg.eig(H)
#     momenta, mom_vec = linalg.eig(T)
    energies = np.diag(np.dot(np.dot(U2.conj().T,H),U2)).real
    momenta = np.angle(np.diag(np.dot(np.dot(U2.conj().T,T),U2)))
    ind = energies.real.argsort()[::+1]
    energies = energies[ind]
    momenta = momenta[ind]
    # Identify -pi with pi
    ind2 = np.where(np.abs(momenta+np.pi) <1E-6)
    momenta[ind2] = -1.* momenta[ind2]
#     return(momenta)
    # Plot the dispersion
    fig, ax = plt.subplots(figsize=(7, 5), tight_layout=True)

    ax.title.set_text("N={},$J_x$={},$J_y$={},$J_z$={},$h_x$={},$h_y$={},$h_z$={}".format(N,J[0],J[1],J[2],h[0],h[1],h[2]))
    ax.set(xlabel='p/$\pi$', ylabel='E(p)')

    ax.scatter(momenta / np.pi,energies.real)
    _, ind = (energies.real.min(),np.where(energies == energies.min())[0][0])
    ax.scatter(momenta[ind] / np.pi,energies[ind].real,marker = "o",s = 100)
    plt.savefig(str(path)+'/trials/scatter.png')
    plt.show()


N=4
J=[0,0,1]
h=[1,0,0]
PBC =True
plot_matrices(N,J,h,PBC = True)
plot_scatter(N,J,h,PBC)

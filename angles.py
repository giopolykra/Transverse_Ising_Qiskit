import numpy as np
from numpy import array,kron,random,identity

def parameters(N,layers, PBC = True):
    if layers<1:
        print('layers have to be possitive integers')
    else:
        if PBC == True:
            if N!=1:
                a = 2*np.pi*np.random.rand(4*layers)
            else:
                a = 2*np.pi*np.random.rand(3*layers)
        else:
            if N!=1:
                a = 2*np.pi*np.random.rand(((3*N)+N)*layers)
            else:
                a = 2*np.pi*np.random.rand((3*N)*layers)
        return(a)

def parameters2(N,layers, PBC):
    if N%2!=0:
        print('error: N has to be an even number')
    else:
        if PBC == 'tight':
            a = 2*np.pi*np.random.rand(2*N)
            for i in range(1,layers):
                a = np.concatenate((a,2*np.pi*np.random.rand(2)),axis=None)
            return(a)
        if PBC == 'soft':
            a = np.concatenate((np.tile(2*np.pi*np.random.rand(1),N),np.tile(2*np.pi*np.random.rand(1),np.int(np.floor(N/2)))), axis = None)
            b = a
            b = np.concatenate((b,np.tile(2*np.pi*np.random.rand(1),N),np.tile(2*np.pi*np.random.rand(1),np.int(np.floor(N/2)))),axis = None)
            for l in range(1,layers):
                c = np.concatenate((np.tile(2*np.pi*np.random.rand(1),N),np.tile(2*np.pi*np.random.rand(1),np.int(np.floor(N/2)))), axis = None)
                d = np.concatenate((c,np.tile(2*np.pi*np.random.rand(1),N),np.tile(2*np.pi*np.random.rand(1),np.int(np.floor(N/2)))),axis = None)
                b = np.concatenate((b,d),axis = None)
            return(b)
        if PBC == 'no':
            a = 2*np.pi*np.random.rand(3*N*layers)
            return(a)

import numpy as np
from numpy import array,kron


def HeisenbergHamiltonian(N, J, h, PBC=False):
#     # Some error checking
    if (len(J) != 3):
        print("error: Vector containing the couplings has to have length 3")
    if (len(h) != 3):
        print("error: Vector containing the field strengths has to have length 3")
#     # Provide the Pauli matrices
    s0 = array([[1+0.0j,0+0.0j],[0+0.0j,1+0.0j]])
    sx = array([[0+0.0j,1+0.0j],[1+0.0j,0+0.0j]])
    sy = array([[0+0.0j,-1.0j],[0.0+1.0j,0.0+0.0j]])
    sz = array([[1+0.0j,0+0.0j],[0+0.0j,-1+0.0j]])
    H = np.zeros(shape=(2**N,2**N))
    for i in range(1,N+1):
        id_left = array(np.identity(2**(i - 1)), copy=False)
        id_right = array(np.identity(2**(N - i)), copy=False)
        H = (
            H
            + kron(kron(id_left,sx),id_right)
            + (h[1]/h[0])*kron(kron(id_left,sy),id_right)
            + (h[2]/h[0])*kron(kron(id_left,sz),id_right)
            )
#         print('H = ',H)
        if (i<N):
            id_right = array(np.identity(2**(N-i-1)), copy=False)
            H = (
                H
                + (J[0]/h[0])*kron(kron(kron(id_left,sx),sx),id_right)
                + (J[1]/h[0])*kron(kron(kron(id_left,sy),sy),id_right)
                + (J[2]/h[0])*kron(kron(kron(id_left,sz),sz),id_right)
                )
    if PBC==True:
        idx = array(np.identity(2**(N-2)), copy=False)
        H = (
            H + (J[0]/h[0])*kron(kron(sx,idx),sx)
                + (J[1]/h[0])*kron(kron(sy,idx),sy)
                + (J[2]/h[0])*kron(kron(sz,idx),sz)
            )
    return(H)

def getT(N):
    swap = array([[1., 0., 0., 0.],
       [0., 0., 1., 0.],
       [0., 1., 0., 0.],
       [0., 0., 0., 1.]])
    res = array(np.identity(2**N), copy=False)
    for i in range(1,N):
        id_left = array(np.identity(2**(i - 1)), copy=False)
        id_right = array(np.identity(2**(N - i - 1)), copy=False)
        tmp = kron(kron(id_left,swap),id_right)
        res = np.dot(tmp,res)
#         print("id_left = {}\nid_right = {}\ntmp = {}\nres = {}".format(repr(id_left),repr(id_right),repr(tmp),repr(res)))
    return(res)




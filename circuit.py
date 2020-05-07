from qiskit import *
import numpy as np

def circuit1(N,param,layers, PBC = True, momentum = 0):
    qr = QuantumRegister(N)
    cr = ClassicalRegister(N)
    qc = QuantumCircuit(qr, cr)
    #param4
    if momentum ==1:
        qc.x(qr[0])
        [qc.cx(qr[i],qr[i+1]) for i in range(N-1)]
        qc.barrier()
    if PBC == True:
        for l in range(layers):
            if N!=1:
                [qc.rx(param[0+4*l],qr[i]) for i in range(N)]
                [qc.ry(param[1+4*l],qr[i]) for i in range(N)]
                [qc.rz(param[2+4*l],qr[i]) for i in range(N)]
                for i in range(N-1):
                    qc.rzz(param[3+4*l],qr[i],qr[i+1])
                qc.rzz(param[3+4*l],qr[N-1],qr[0])
            else:
                [qc.rx(param[0+3*l],qr[i]) for i in range(N)]
                [qc.ry(param[1+3*l],qr[i]) for i in range(N)]
                [qc.rz(param[2+3*l],qr[i]) for i in range(N)]
            qc.barrier()
        qc.unitary
    else:
        if N!=1:
            for l in range(layers):
                [qc.rx(param[(0+i)*l],qr[i]) for i in range(N)]
                [qc.ry(param[(1+i)*l],qr[i]) for i in range(N)]
                [qc.rz(param[(2+i)*l],qr[i]) for i in range(N)]
                for j in range(N-1):
                    qc.rzz(param[(3*N+j)*l],qr[j],qr[j+1])
                qc.rzz(param[(4*N-1)*l],qr[N-1],qr[0])
                qc.barrier()
        else:
            for l in range(layers):
                [qc.rx(param[(0+i)*l],qr[i]) for i in range(N)]
                [qc.ry(param[(1+i)*l],qr[i]) for i in range(N)]
                [qc.rz(param[(2+i)*l],qr[i]) for i in range(N)]
                qc.barrier()
#     [qc.measure(qr[i], cr[i]) for i in range(N)]
    return qc


def circuit2(N,param,layers,PBC):
    qr = QuantumRegister(N)
    cr = ClassicalRegister(N)
    qc = QuantumCircuit(qr, cr)
    if PBC == 'tight':
        for l in range(layers):
            [qc.ry(param[0+l],qr[i]) for i in range(N)]
            for j in range(np.int(np.floor(N/2))):
                qc.rzz(param[1+l],qr[2*j],qr[2*j+1])
            [qc.ry(param[2+l],qr[i]) for i in range(N)]
            qc.rzz(param[3+l],qr[N-1],qr[0])
            for j in range(1,np.int(np.floor(N/2))):
                qc.rzz(param[3+l],qr[2*j],qr[2*j-1])
            qc.barrier()
    elif PBC == 'soft' or 'no':
        for l in range(layers):
            [qc.ry(param[3*N*l+i],qr[i]) for i in range(N)]
            for j in range(np.int(np.floor(N/2))):
                qc.rzz(param[3*N*l+N+j],qr[2*j],qr[2*j+1])
            [qc.ry(param[(3*N)*l+N+int(N/2)+i],qr[i]) for i in range(N)]
            qc.rzz(param[(3*N)*l+2*N+int(N/2)],qr[N-1],qr[0])
            for j in range(1,np.int(np.floor(N/2))):
                qc.rzz(param[(3*N)*l+2*N+int(N/2)+j],qr[2*j],qr[2*j-1])
            qc.barrier()
    return qc

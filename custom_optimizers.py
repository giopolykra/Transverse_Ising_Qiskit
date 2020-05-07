import numpy as np
from numpy import array
from scipy.optimize import minimize
from qiskit import *
from E import *
from angles import *
from optimizing_functions import *

def sequencial_minimizer(func, param1, Iter,N , layers, J, h, PBC , p, opt_param, epsilon):
    xmin = -np.ones(1)*np.pi*2
    xmax = np.ones(1)*np.pi*2
    bounds = [(low, high) for low, high in zip(xmin, xmax)]

    energy_callbacks = []
    energy_callbacks = [0,func(param1,N,layers,J,h,PBC,p,opt_param,epsilon)]

    term = func.__name__

    param_callbacks = []
    param_callbacks = [0, param1[0]]
    param_full_callbacks = []
    param_full_callbacks = [0, param1]
    full_array = []

    def printing(x,param_new,energy_callbacks,when):
        if when == True:
            print('\n#####\x09AFTER:')
        if when == False:
            print('\n#####\x09BEFORE:')
        print('\na \x09\x09= {}\nparam \x09\x09= {}\nlen(param) \x09= {}'.format(a,param_new,len(param_new)))
        print('x\x09\x09= {}'.format(x))
        if a!=0 or i!=0 or when!=False:
            print('res[0] \x09\x09= {}'.format(res[0]))
            print('res[1] \x09\x09= {}'.format(res[1]))
        print('energy_callback\x09= {}'.format(energy_callbacks))
        print('param_full_callbacks\x09= {}\n'.format(param_full_callbacks))

    for i in range(Iter):
#        print('\nITTER = {} \x09Layer = {}\n'.format(i,layers))
        for a in range(len(param1)):
            x = param1[a]
#            print('a={}\x09param = {}\x09x = {}'.format(a,param1,x))
            def wrapper(x,N,layers,J,h,PBC,p,opt_param,epsilon):
                my_array = []
                my_array = np.array(list(param_full_callbacks[1][:a])+list(x)+list(param_full_callbacks[1][a+1:]))
#                print('my_array = ',repr(my_array))
#                print('eval(term)(my_array) = ', eval(term)(my_array,layers,N,J,h,PBC,p))
                return(eval(term)(my_array,N,layers,J,h,PBC,p,opt_param,epsilon))
#            printing(x,param_full_callbacks[1],energy_callbacks,False)
            ret = minimize(wrapper,x,args=(N,layers,J,h,PBC,p,opt_param,epsilon),method='COBYLA',jac=None, bounds=None, tol=None, callback=None,options={'maxiter': 10})
            res = [[ret.x],ret.fun]
#            print('RES ->',res)
#            print('energy_callbacks ->',energy_callbacks)
#            print('wrapper ->',wrapper(res[0],layers,N,J,h,PBC,p))
#             res = optimizer1.optimize(objective_function=wrapper,initial_point=x,num_vars= len(x))
            if wrapper(res[0],N,layers,J,h,PBC,p,opt_param,epsilon) < energy_callbacks[1]:
                energy_callbacks[0] = energy_callbacks[1]
                energy_callbacks[1] = res[1]
                param_callbacks[0] = param_callbacks[1]
                param_callbacks[1] = res[0]
                param_full_callbacks[0] = param_full_callbacks[1]
#                print('HERE')
                param_full_callbacks[1] = np.array(list(param_full_callbacks[1][:a])+list(res[0][:])+list(param_full_callbacks[1][a+1:]))
                x = res[0]
#            printing(x,param_full_callbacks[1],energy_callbacks,True)
    return(param_full_callbacks[1],energy_callbacks[1])

#N = 2
#J = [0,0,1]
#h = [1,0,0]
#p = 1
#layers = 1
#PBC = True
#Iter = 1
#param = parameters(N,layers,PBC)
#sequencial_minimizer(extra_term , param , Iter , layers , N , J , h , PBC , p)

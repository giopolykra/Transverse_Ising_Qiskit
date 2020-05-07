from state_dict import *

file = open("b_values_data.py","w+")

N=2
J = [0,0,1]
h = [1,0,0]

for N in range(2,7):
    for h_value in [0.5,1,2,4,8,10,20]:
        h_name = str(h_value).replace('.','')
        for PBC in [True,False]:
            a = list(eval('dict_en_HT_N{}J{}h{}_{}'.format(N,int(J[2]),h_name,str(PBC))).values())
            b = a[1:]
            for k in range(1,len(a)):
                locals()['b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),k)] = []
                for m in range(k):
                    locals()['b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),k)].append(a[k]-a[m])
                txt1 = 'b_N{}J{}h{}_{}_k{} = '.format(N,int(J[2]),h_name,str(PBC),k)
                txt2 = "{}\n".format(eval('b_N{}J{}h{}_{}_k{}'.format(N,int(J[2]),h_name,str(PBC),k)))
                file.write(txt1+txt2)
file.close

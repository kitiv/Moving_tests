from numpy import zeros
def split_func(name):
    f=open(name,'r')
    a=f.read()
    f.close
    b=a.split('\n')
    NofS=list()
    for i in range(0,len(b)-1):
        NofS.append(b[i][20:32])
    return NofS, len(set(NofS))

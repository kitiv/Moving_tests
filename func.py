from numpy import zeros
def open_func(name):
    f=open(name,'r')
    a=f.read()
    f.close
    b=a.split('\n')
    Incl1=zeros((len(b)-1,24))
    for i in range(0,len(b)-1):
        Incl1[i,:]=b[i].split(',')[2:26]
    return Incl1
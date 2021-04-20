# -*- coding: utf-8 -*-

pi=3.14159265359
sigma=1
koef=1/(2*pi*sigma**2)

def Gauss(x,size):
    N=len(x)
    h=[[0]*size for i in range(size)]
    flag=0
    if(np.size(x[0].split(","))/np.size(float)==2):
        flag=1
    for i in range(N):
        n=x[i].split(",")
        x0+=float(n[0])
        y0+=float(n[1])
    x0/=N
    y0/=N
    for i in range(N):
        n=x[i].split(",")
        i1=math.trunc(n[0])
        j1=math.trunc(n[1])
        h[i1][j1]+=koef*pow(e, (-(float(n[0])-x0)**2 - (float(n[1])-y0)**2) / (2*sigma**2) )
        '''
        if (flag==0):
            var=int(n[2])#########################################################################
        else: var=1
        i1=math.trunc(n[0])
        j1=math.trunc(n[1])
        '''
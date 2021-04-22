# -*- coding: utf-8 -*-

from our_func import *
sigma=10
koef=1/(2*pi*sigma**2)

def Gauss_text(x,size):
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

def Gauss_pix(mass,size):
    h=[[0]*size for i in range(size)]
    
    sum_x,sum_y=0,0
    for i in range(size):
        for j in range(size):
            sum_x+=mass[i][j]*i
            sum_y+=mass[i][j]*j
    sum_x/=size**2
    sum_y/=size**2
    
    '''
    sum=-1
    for i in range(size):
        for j in range(size):
            if(sum<mass[i][j]):
                sum=mass[i][j]
    '''
    for i in range(size):
        for j in range(size):
            h[i][j]=koef*pow(e, (-(sum_x-mass[i][j]*i)**2 - (sum_y-mass[i][j]*j)**2) /  (2*sigma**2) )
    return h

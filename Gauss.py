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
    sum=0
    for i in range(size):
        for j in range(size):
            sum_x+=mass[i][j]*i
            sum_y+=mass[i][j]*j
            sum += mass[i][j]
    sum_x/=sum
    sum_y/=sum
    
    '''
    sum=-1
    for i in range(size):
        for j in range(size):
            if(sum<mass[i][j]):
                sum=mass[i][j]
    '''
    for i in range(size):
        for j in range(size):
            h[i][j]=mass[i][j]*koef*pow(e, (-(sum_x-i)**2 - (sum_y-j)**2) /  (2*sigma**2) )
    return h

def G(i,j,sigma,sum_x, sum_y):
    koef=1/(2*pi*sigma**2)
    return koef*pow(e, (-(sum_x-i)**2 - (sum_y-j)**2) /  (2*sigma**2) )

def nw_Gauss(mass,size):
    h=[[0]*size for i in range(size)]
    
    sum_x,sum_y=0,0
    sum=0
    for i in range(size):
        for j in range(size):
            sum_x+=mass[i][j]*i
            sum_y+=mass[i][j]*j
            sum += mass[i][j]
    sum_x/=sum
    sum_y/=sum
    
    '''
    sum=-1
    for i in range(size):
        for j in range(size):
            if(sum<mass[i][j]):
                sum=mass[i][j]
    '''
    
    for i in range(size):
        for j in range(size):
            h[i][j]=mass[i][j]*(G(i,j,1.,sum_x,sum_y) - G(i,j,100.,sum_x,sum_y))
            if(h[i][j] != 0):
                if(h[i][j] < 0):    
                    h[i][j]*=pow(4.*pi,0.5)*3.*(1/(pow(abs(h[i][j])*G(i,j,100.,sum_x,sum_y),0.5)))
                else:
                    h[i][j]*=pow(4.*pi,0.5)*3.*(1/(pow(h[i][j]*G(i,j,100.,sum_x,sum_y),0.5)))   
                
    return h
    
# -*- coding: utf-8 -*-
from our_func import *

cf2,cf4=0.25,0.5
#Распределяет звезду в ближайшие смежные по правилу покрытия сf клетки
def ValSep(x,y,value,size,cf,mass):
    i1=math.trunc(x)
    j1=math.trunc(y)
    mass[j1][i1]+=value
    #
    su=0
    if(x - i1 < cf and i1 > 0):
        mass[j1][i1-1]+=value
        su+=1
    if(x - i1 > 1 - cf and i1 < size - 1):
        mass[j1][i1+1]+=value    
        su+=3
    if(y - j1 < cf and j1 > 0):
        mass[j1-1][i1]+=value 
        su+=1
    if(y - j1 > 1 - cf and j1 < size - 1):
        mass[j1+1][i1]+=value    
        su+=5
    if(su==2):
        mass[j1-1][i1-1]+=value
    if(su==4):
        mass[j1-1][i1+1]+=value
    if(su==6):
        mass[j1+1][i1-1]+=value
    if(su==8):
        mass[j1+1][i1+1]+=value


def StarDensityTxtWithRad_P(x,size):
    N=len(x)

    h=[[0]*size for i in range(size)]
    #h1=[[0]*size for i in range(size)]
    flag=0
    if(np.size(x[0].split(","))/np.size(float)==2):
        flag=1
    for i in range(N):
        n=x[i].split(",")
        if (flag==0):
            var=int(n[2])#########################################################################
        else: var=1
        ValSep(float(n[0]),float(n[1]),var,size,cf2,h)
        
        '''
    for i in range(size):
        for j in range(size):
            if (not h1[i][j]==0):
                h[i][j]=h[i][j]/h1[i][j]   
        '''
        
    return h

def PforEach(mass,size):
    sum_of_all=0
    P_max = -1
    P_min = 1
    P_mass = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            sum_of_all += mass[i][j]
    for i in range(size):
        for j in range(size):
            P_mass[i][j] = mass[i][j]/sum_of_all
            if (P_max < P_mass[i][j]):
                P_max = P_mass[i][j]
            if (P_min > P_mass[i][j]):
                P_min = P_mass[i][j]
    return P_mass,P_max,P_min
    

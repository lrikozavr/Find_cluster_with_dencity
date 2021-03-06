# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
import math

pi=3.14159265359
e=2.7182818284

def TxtToArray(filename,size,col):
    maxr,minr=-1,361
    maxd,mind=-91,91
    mass,mass1=[],[]
    for line in open(filename):
        n=line.split(",")
        if (col > 2):
            mass.append(n[0]+","+n[1]+","+n[col-1])#################################################################
        else: mass.append(n[0]+","+n[1])
        a=float(n[0])
        b=float(n[1])
        if (a>maxr):
            maxr=a
        if (a<minr):
            minr=a
        if (b>maxd):
            maxd=b
        if (b<mind):
            mind=b
    #print(100/(maxr-minr),100/(maxd-mind))
    KORA=abs((size-1e-5)/(maxr-minr))
    KODA=abs((size-1e-5)/(maxd-mind))
    h,h1=0,0
    #
    if (mind < 0 and maxd < 0):
        h=1
    if (minr < 0 and maxr < 0):
        h1=1
    for line in mass:
        n=line.split(",")
        if (h==1):
            b1=abs(float(n[1]))-abs(maxd)
            #print(b1)                
        else:
            b1=float(n[1])-mind
            #print(b1)
        if (h1==1):
            a1=abs(float(n[0]))-abs(maxr)   
            #print(a1)             
        else:
            a1=float(n[0])-minr
            #print(a1)
        if (col > 2):
            mass1.append(str(a1*KORA)+","+str(b1*KODA)+","+str(n[2]))#####################################################
        else: mass1.append(str(a1*KORA)+","+str(b1*KODA))
    #kk=[[0]*size for i in range(size)]
    #kk=StarDensityTxtWithRad(mass1,size)
    #return kk
    return mass1,minr,maxr,mind,maxd
    #lets
    #do it
def ArrayToTxt(filename,co,a_list,size):
    g=open(filename,"w")
    
    dx=co[1]-co[0]
    dy=co[3]-co[2]
    
    #ox=dx/2.
    #oy=dy/2.

    KORA=abs(dx/float(size))
    KODA=abs(dy/float(size))
    
    for i in range(len(a_list)):
        n=a_list[i].split(",")
        g.write(str(float(n[0])*KORA+co[0])+","+str(float(n[1])*KODA+co[2])+"\n")





def Piece_of_mass(mass,v,size):
    if (size + v[0] - 1 > pow(np.size(mass),0.5) or size + v[1] - 1 > pow(np.size(mass),0.5)):
        print("Error index out")
        return
    rezult = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            rezult[i][j] = mass[v[0]+i][v[1]+j]
    return rezult

def SumOfMatrix(mass1,mass2,size):
    rezult=[[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            rezult[i][j]=mass1[i][j]+mass2[i][j]
    return rezult
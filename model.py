# -*- coding: utf-8 -*-
import random
from matplotlib import pyplot as plt

from our_func import ArrayToTxt
from Parzen import StarDensityTxtWithRad_W
from Picture import Sep_Pic,Pic
def WhiteNoiseModel(ax,bx,ay,by,count,rezult):
    for i in range(count):
        #list=[random.uniform(a,b),random.uniform(a,b)]
        list=str(random.uniform(ax,bx))+","+str(random.uniform(ay,by))
        rezult.append(list)

def GaussModel(ax,bx,ay,by,g_c,count,rezult):
    dx=bx-ax
    dy=by-ay
    ox=dx/2.
    oy=dy/2.
    center_x = ax + ox
    center_y = ay + oy
    #g_c=10.
    ddx=ox/g_c
    ddy=oy/g_c
    for g in range(count):
        sumx,sumy=center_x,center_y
        for i in range(int(g_c)):
            sumx+=random.uniform(-ddx,ddx)
            sumy+=random.uniform(-ddy,ddy)
        list=str(sumx)+","+str(sumy)
        rezult.append(list)

def GaussAndWhiteNoiseModel(ax,bx,ay,by,g_c,count,half,rezult):
    Gcount=int(half*count)
    Wcount=int((1-half)*count)
    GaussModel(ax,bx,ay,by,g_c,Gcount,rezult)
    WhiteNoiseModel(ax,bx,ay,by,Wcount,rezult)

def SepRandModeling(ax,bx,ay,by,size,n):
    k=int(size/n)
    dx=(bx-ax)/float(k)
    dy=(by-ay)/float(k)
    noise_count = 400000
    global_list = []
    WhiteNoiseModel(ax,bx,ay,by,noise_count,global_list)
    #v=[0,0]
    #z=[[0]*size for i in range(size)]
    for i in range(k):
        for j in range(k):
            #KORA=abs((size-1e-5)/(dx))
            #KODA=abs((size-1e-5)/(dy))
            #v[0]=i*n
            #v[1]=j*n
            count=10000
            if(random.randint(0,10)>9):
                GaussModel(j*dx,(j+1)*dx,i*dy,(i+1)*dy,5.,count,global_list)
    return global_list
'''
size=1000
#len_=10000
data=[[0]*size for i in range(size)]

#mass=GaussAndWhiteNoiseModel(0,1000,5.,len_,0.5)
mass = SepRandModeling(0.,size,0,size,size,250)
print(len(mass))
co=[300.,310.,40.,50.]
ArrayToTxt("/home/kiril/github/Find_cluster_with_dencity/gauss_pic/gauss.csv",co,mass,size)
fin = StarDensityTxtWithRad_W(mass,size)
Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/gauss_pic/","Gauss",fin,size,size,Pic)
'''

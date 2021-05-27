# -*- coding: utf-8 -*-
import random
from matplotlib import pyplot as plt

def WhiteNoiseModel(ax,bx,ay,by,count):
    rezult=[]
    for i in range(count):
        #list=[random.uniform(a,b),random.uniform(a,b)]
        list=[random.randint(ax,bx),random.randint(ay,by)]
        rezult.append(list)
    return rezult

def GaussModel(ax,bx,ay,by,g_c,count):
    rezult=[]
    dx=bx-ax
    dy=by-ay
    ox=dx/2.
    oy=dy/2.
    #g_c=10.
    ddx=ox/g_c
    ddy=oy/g_c
    for g in range(count):
        sumx,sumy=ox,oy
        for i in range(int(g_c)):
            sumx+=random.randint(-ddx,ddx)
            sumy+=random.randint(-ddy,ddy)
        list=[sumx,sumy]
        rezult.append(list)
    return rezult    

def GaussAndWhiteNoiseModel(ax,bx,ay,by,g_c,count,half):
    Gcount=int(half*count)
    Wcount=int((1-half)*count)
    rezult=GaussModel(ax,bx,ay,by,g_c,Gcount)
    #print(rezult)
    rez=WhiteNoiseModel(ax,bx,ay,by,Wcount)
    #print(rez)
    f=[]
    for i in range(len(rez)):
        f.append(rez[i])
    for i in range(len(rezult)):
        f.append(rezult[i])
    return f
'''
size=1000
len_=10000
data=[[0]*size for i in range(size)]

mass=GaussAndWhiteNoiseModel(0,1000,5.,len_,0.5)
print(len(mass))
x,y=[0]*len_,[0]*len_
for i in range(len_-1):
	x[i]=mass[i][0]
	y[i]=mass[i][1]
plt.scatter(x,y)
#for i in range()
#
'''
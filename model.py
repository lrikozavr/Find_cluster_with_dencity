# -*- coding: utf-8 -*-
import random
from matplotlib import pyplot as plt

def WhiteNoiseModel(a,b,count):
    rezult=[]
    for i in range(count):
        #list=[random.uniform(a,b),random.uniform(a,b)]
        list=[random.randint(a,b),random.randint(a,b)]
        rezult.append(list)
    return rezult

def GaussModel(a,b,g_c,count):
    rezult=[]
    d=b-a
    o=d/2.
    #g_c=10.
    dd=o/g_c
    for g in range(count):
        sumx,sumy=o,o
        for i in range(int(g_c)):
            sumx+=random.randint(-dd,dd)
            sumy+=random.randint(-dd,dd)
        list=[sumx,sumy]
        rezult.append(list)
    return rezult    

def GaussAndWhiteNoiseModel(a,b,g_c,count,half):
    Gcount=int((1-half)*count)
    Wcount=int(half*count)
    rezult=GaussModel(a,b,g_c,Gcount)
    #print(rezult)
    rez=WhiteNoiseModel(a,b,Wcount)
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
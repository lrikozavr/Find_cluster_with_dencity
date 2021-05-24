# -*- coding: utf-8 -*-
import random

def WhiteNoiseModel(a,b,count):
    rezult=[0]*count
    for i in range(count):
        list=[random(a,b),random(a,b)]
        rezult[i]=list
    return rezult

def GaussModel(a,b,count):
    rezult=[0]*count
    d=b-a
    o=d/2.
    dd=o/100.
    for g in range(count):
        sumx,sumy=o,o
        for i in range(100):
            sumx+=random(-dd,dd)
            sumy+=random(-dd,dd)
        list=[sumx,sumy]
        rezult[g]=list
    return rezult    

def GaussAndWhiteNoiseModel(a,b,count,half):
    rezult=[]
    Gcount=(1-half)*count
    Wcount=half*count
    rezult.append(GaussModel(a,b,Gcount))
    rezult.append(WhiteNoiseModel(a,b,Wcount))
    return rezult
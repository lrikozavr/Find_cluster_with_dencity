# -*- coding: utf-8 -*-
import pylab
from matplotlib import pyplot as plt

from Wavelet import Wavlet,KF90,makeData
from our_func import *
from Gauss import *

def Sep_Pic(path,data,size,n):
    #n=100
    k=int(size/n)
    v=[0,0]
    z=[]
    for i in range(k):
        for j in range(k):
            v[0]=i*n
            v[1]=j*n
            x, y = makeData(range(n),range(n))
            z = Piece_of_mass(data,v,n)
            #mass = []
            '''
            mass = Wavlet(z,1,KF90)
            pylab.pcolormesh(x,y,np.array(mass))
            pylab.savefig(path+"Wavelet_"+str(i)+"_"+str(j)+".png")
            '''
            #mass = []
            mass = Gauss_pix(z,n)
            pylab.pcolormesh(x,y,np.array(mass))
            pylab.savefig(path+"Gauss_"+str(i)+"_"+str(j)+".png")
            #
            '''
            pylab.pcolormesh(x,y,np.array(z))
            pylab.savefig(path+"Pure_pic_"+str(i)+"_"+str(j)+".png")
            '''

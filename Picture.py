# -*- coding: utf-8 -*-
import pylab
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

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
            mass = nw_Gauss(z,n)
            #print(mass)
            pylab.pcolormesh(x,y,np.array(mass))
            pylab.savefig(path+"nw_Gauss_"+str(i)+"_"+str(j)+".png")
            #
            mass = Wavlet(z,1,KF90)
            pylab.pcolormesh(x,y,np.array(mass))
            pylab.savefig(path+"Wavelet_"+str(i)+"_"+str(j)+".png")
            
            #mass = []
            mass = Gauss_pix(z,n)
            pylab.pcolormesh(x,y,np.array(mass))
            pylab.savefig(path+"Gauss_"+str(i)+"_"+str(j)+".png")
            #
            

            #
            pylab.pcolormesh(x,y,np.array(z))
            pylab.savefig(path+"Pure_pic_"+str(i)+"_"+str(j)+".png")
            
def Sep_Pic_3d(path,data,size,n):
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
            fig=plt.figure()
            axes=Axes3D(fig)
            #
            axes.plot_surface(x,y,np.array(z),rstride=1, cstride=1, cmap = cm.jet)
            fig.savefig(path+"Pure_pic_3D_"+str(i)+"_"+str(j)+".png")
            #
            mass = Wavlet(z,1,KF90)
            axes.plot_surface(x,y,np.array(mass),rstride=1, cstride=1, cmap = cm.jet)
            fig.savefig(path+"Wavelet_3D_"+str(i)+"_"+str(j)+".png")
            
            #mass = []
            mass = Gauss_pix(z,n)
            axes.plot_surface(x,y,np.array(mass),rstride=1, cstride=1, cmap = cm.jet)
            fig.savefig(path+"Gauss_3D"+str(i)+"_"+str(j)+".png")
            #

            mass = nw_Gauss(z,n)
            axes.plot_surface(x,y,np.array(mass),rstride=1, cstride=1, cmap = cm.jet)
            fig.savefig(path+"nw_Gauss_3D"+str(i)+"_"+str(j)+".png")
            
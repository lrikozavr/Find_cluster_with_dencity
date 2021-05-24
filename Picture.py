# -*- coding: utf-8 -*-
import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib as mpl

from Wavelet import Wavlet,KF90,KF98,makeData
from our_func import *
from Parzen import Parzen_P
#from Gauss import *


def Pic(mass,path):
    fig = plt.figure()
    cmap = mpl.colors.LinearSegmentedColormap.from_list('my_colormap',['black','white'],256)
    img = plt.imshow(mass,interpolation='nearest',
            cmap = cmap,
            origin='lower')
    plt.colorbar(img,cmap=cmap)     
    plt.savefig(path)
            



def Sep_Pic_Parzen(path,data,size,n):
    #n=100
    k=int(size/n)
    v=[0,0]
    z=[]

    for i in range(k):
        for j in range(k):
            v[0]=i*n
            v[1]=j*n
            #x, y = makeData(range(n),range(n))
            z = Piece_of_mass(data,v,n)
            #
            Pic(z,path+"Pure_pic_"+str(i+1)+"_"+str(j+1)+".png")
            #pylab.pcolormesh(x,y,np.array(z))
            #pylab.savefig(path+"Pure_pic_"+str(i+1)+"_"+str(j+1)+".png")
            #
            mass = Parzen_P(z,n)
            Pic(mass,path+"Parzen_S_"+str(i+1)+"_"+str(j+1)+".png")
            #

def Sep_Pic_Wavelet(path,data,size,n):
    #n=100
    k=int(size/n)
    v=[0,0]
    z=[]
    data = np.array(data)
    data = data.transpose()
    for i in range(k):
        for j in range(k):
            v[0]=i*n
            v[1]=j*n
            #x, y = makeData(range(n),range(n))
            z = Piece_of_mass(data,v,n)
            #
            fig=pylab.figure()
            Pic(z,path+"Pure_pic_"+str(i)+"_"+str(j)+".png")
            #mass = []
            #
            mass = Wavlet(z,1,KF98)
            Pic(mass,path+"Wavelet_"+str(i)+"_"+str(j)+".png")
            
'''           
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
'''            
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import pylab
from Parzen import *
from Wavelet import *
#"/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt"
filename = "/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_1_60_n.txt"

size = 1000
col_num = 62

data=[[0]*size for i in range(size)]

data = StarDensityTxtWithRad_P(TxtToArray(filename,size,col_num),size)
#P_data,P_data_max,P_data_min = PforEach(data,size)
##########
#x, y = makeData(range(size),range(size))
#
#fig0=plt.figure()
#axes=Axes3D(fig0)
#
#axes.plot_surface(x,y,np.array(data), rstride=1, cstride=1, cmap = cm.jet)
#pylab.pcolormesh(x,y,np.array(data))
#
#fig0.savefig("/home/kiril/github/Find_cluster_with_dencity/data100_62.png")
#
#pylab.show()

def Piece_of_mass(mass,v,size):
    if (size + v[0] - 1 > pow(np.size(mass),0.5) or size + v[1] - 1 > pow(np.size(mass),0.5)):
        print("Error index out")
        return
    rezult = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            rezult[i][j] = mass[v[0]+i][v[1]+j]
    return rezult

n=100
k=int(size/n)
v=[0,0]
z=[]
for i in range(k):
    for j in range(k):
        v[0]=i*n
        v[1]=j*n
        z = Piece_of_mass(data,v,n)
        x, y = makeData(range(n),range(n))
        pylab.pcolormesh(x,y,np.array(z))
        pylab.savefig("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures/data_"+str(i)+"_"+str(j)+".png")



#MainWavlet("/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt",100,0,1,KF90)

#fig_w=MainWavlet(filename,size,col_num,1,KF90)
#plt.show()

# -*- coding: utf-8 -*-


from Parzen import *
from Wavelet import *
from our_func import *
from Picture import Sep_Pic
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

Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures/",data,size,100)



#MainWavlet("/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt",100,0,1,KF90)

#fig_w=MainWavlet(filename,size,col_num,1,KF90)
#plt.show()

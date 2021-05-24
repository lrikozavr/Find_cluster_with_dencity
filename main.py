#!/home/kiril/python_env_iron_ment/my_project/bin/python
# -*- coding: utf-8 -*-
import sys

from Parzen import *
from Wavelet import *
from our_func import *
from Picture import Sep_Pic_Parzen,Sep_Pic_Wavelet
#"/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt"
#filename = "/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_1_60_n_81_80_70_69.txt"
#filename = "/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_1_60_n.txt"

fileinput=sys.argv[1]
fileoutput=sys.argv[2]
col_num=sys.argv[3]

size_w = 100
size_p = 1000
#col_num = 60

data_w=[[0]*size_w for i in range(size_w)]
data_p=[[0]*size_p for i in range(size_p)]

data_w = StarDensityTxtWithRad_W(TxtToArray(fileinput,size_w,int(col_num)),size_w)
data_p = StarDensityTxtWithRad_P(TxtToArray(fileinput,size_p,int(col_num)),size_p)
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
Sep_Pic_Parzen(fileoutput,data_p,size_p,1000)
Sep_Pic_Wavelet(fileoutput,data_w,size_w,100)
#Sep_Pic_3d("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures_60/",data,size,100)

#Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures_60/",data,size,1000)
'''
col_num = 0
data1=[[0]*size for i in range(size)]
data1 = StarDensityTxtWithRad_P(TxtToArray(filename,size,col_num),size)
#Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/BMS_80_81_69_70_pictures/",data1,size,100)
#Sep_Pic_3d("/home/kiril/github/Find_cluster_with_dencity/BMS_80_81_69_70_pictures/",data1,size,100)

Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures/",data1,size,100)
Sep_Pic_3d("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures/",data1,size,100)

Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures/",data1,size,1000)
#Sep_Pic_3d("/home/kiril/github/Find_cluster_with_dencity/BMS_80_81_69_70_pictures/",data1,size,1000)


#Sep_Pic("/home/kiril/github/Find_cluster_with_dencity/BMS_pictures/",data,size,100)



#MainWavlet("/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt",100,0,1,KF90)

#fig_w=MainWavlet(filename,size,col_num,1,KF90)
#plt.show()
'''
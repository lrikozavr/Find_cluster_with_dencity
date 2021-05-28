#!/home/kiril/python_env_iron_ment/my_project/bin/python
# -*- coding: utf-8 -*-
import sys

from Parzen import *
from Wavelet import *
from our_func import *
from Picture import *
from Picture import UnderGround
from model import GaussAndWhiteNoiseModel
#"/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt"
#filename = "/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_1_60_n_81_80_70_69.txt"
#filename = "/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_1_60_n.txt"

fileinput=sys.argv[1]
fileoutput=sys.argv[2]
fileexamplecat=sys.argv[3]
col_num=sys.argv[4]

size_w = 100
size_p = 1000
#col_num = 60
#len_=200000
#data_g=GaussAndWhiteNoiseModel(0,1000,0,1000,200.,len_,0.5)
#
data_w=[[0]*size_w for i in range(size_w)]
temp_w,minr_w,maxr_w,mind_w,maxd_w=TxtToArray(fileinput,size_w,int(col_num))
data_w = StarDensityTxtWithRad_W(temp_w,size_w)
example_w=AddExample(fileexamplecat,5,minr_w,maxr_w,mind_w,maxd_w,size_w)
#print(example_w)
#
data_p=[[0]*size_p for i in range(size_p)]
temp_p,minr_p,maxr_p,mind_p,maxd_p=TxtToArray(fileinput,size_p,int(col_num))
data_p = StarDensityTxtWithRad_P(temp_p,size_p)
example_p=AddExample(fileexamplecat,5,minr_p,maxr_p,mind_p,maxd_p,size_p)
#
#Обрабатывай данные сдесь, а не в картинках

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

mass_w = SumOfMatrix(UnderGround(Wavlet(data_w,1,KF98),size_w,3),example_w,size_w)
pure_example_w = SumOfMatrix(UnderGround(data_w,size_w,3),example_w,size_w)
Sep_Pic(fileoutput,"Pure_Ex_W",pure_example_w,size_w,100,Pic_Example)
Sep_Pic(fileoutput,"Wavelet_Ex",mass_w,size_w,100,Pic_Example)

mass_p = SumOfMatrix(UnderGround(Parzen_P(data_p,size_p),size_p,3),example_p,size_p)
pure_example_p = SumOfMatrix(UnderGround(data_p,size_p,3),example_p,size_p)
Sep_Pic(fileoutput,"Pure_Ex_P",pure_example_p,size_p,1000,Pic_Example)
Sep_Pic(fileoutput,"Parzen_Ex",mass_p,size_p,1000,Pic_Example)



#Sep_Pic_Parzen(fileoutput,data_p,size_p,1000)
#Sep_Pic_Wavelet(fileoutput,data_w,size_w,100)





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
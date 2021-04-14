# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from Parzen import *
from Wavelet import *

size = 100
col_num = 7
filename = filename

data=[[0]*size for i in range(size)]
data1=[[0]*size for i in range(size)]

data,data1 = StarDensityTxtWithRad_P(TxtToArray(filename,size,col_num),size)
P_data,P_data_max,P_data_min = PforEach(data,size)
P_data1,P_data1_max,P_data1_min = PforEach(data1,size)
##########
x, y = makeData(range(size),range(size))
#
fig=plt.figure()
axes=Axes3D(fig)
#
axes.plot_surface(x,y,P_data, rstride=1, cstride=1, cmap = cm.jet)
##########

MainWavlet("/media/kiril/j_08/CATALOGUE/gaiadr2_BMS_sort_n.txt",100,0,1,KF90)
MainWavlet("/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_1_60_n.txt",100,62,1,KF90)
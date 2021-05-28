#!/home/kiril/python_env_iron_ment/my_project/bin/python
# -*- coding: utf-8 -*-
import sys

from Parzen import *
from Wavelet import *
from our_func import *
from Picture import *
from Picture import UnderGround
from model import GaussAndWhiteNoiseModel

fileinput=sys.argv[1]
fileoutput=sys.argv[2]
#fileexamplecat=sys.argv[3]
#col_num=sys.argv[4]
col_num=sys.argv[3]

size_w = 100
#
data_w=[[0]*size_w for i in range(size_w)]
temp_w,minr_w,maxr_w,mind_w,maxd_w=TxtToArray(fileinput,size_w,int(col_num))
data_w = StarDensityTxtWithRad_W(temp_w,size_w)
#example_w=AddExample(fileexamplecat,5,minr_w,maxr_w,mind_w,maxd_w,size_w)

#mass_w = SumOfMatrix(UnderGround(Wavlet(data_w,1,KF98),size_w,3),example_w,size_w)
mass_w = Wavlet(data_w,1,KF98)

#pure_example_w = SumOfMatrix(UnderGround(data_w,size_w,3),example_w,size_w)
pure_example_w = data_w

Sep_Pic(fileoutput,"Pure_Ex_W",pure_example_w,size_w,100,Pic)
Sep_Pic(fileoutput,"Wavelet_Ex",mass_w,size_w,100,Pic)

size_p = 1000
#
data_p=[[0]*size_p for i in range(size_p)]
temp_p,minr_p,maxr_p,mind_p,maxd_p=TxtToArray(fileinput,size_p,int(col_num))
data_p = StarDensityTxtWithRad_P(temp_p,size_p)
#example_p=AddExample(fileexamplecat,5,minr_p,maxr_p,mind_p,maxd_p,size_p)

#mass_p = SumOfMatrix(UnderGround(Parzen_P(data_p,size_p),size_p,3),example_p,size_p)
mass_p = UnderGround(Parzen_P(data_p,size_p),size_p,3)

#pure_example_p = SumOfMatrix(UnderGround(data_p,size_p,3),example_p,size_p)
pure_example_p = data_p

Sep_Pic(fileoutput,"Pure_Ex_P",pure_example_p,size_p,1000,Pic)
Sep_Pic(fileoutput,"Parzen_Ex",mass_p,size_p,1000,Pic)
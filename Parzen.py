# -*- coding: utf-8 -*-
from our_func import *

cf2,cf4=0.25,0.5
#Распределяет звезду в ближайшие смежные по правилу покрытия сf клетки
def ValSep(x,y,value,size,cf,mass):
    i1=math.trunc(x)
    j1=math.trunc(y)
    mass[j1][i1]+=value
    #
    su=0
    if(x - i1 < cf and i1 > 0):
        mass[j1][i1-1]+=value
        su+=1
    if(x - i1 > 1 - cf and i1 < size - 1):
        mass[j1][i1+1]+=value    
        su+=3
    if(y - j1 < cf and j1 > 0):
        mass[j1-1][i1]+=value 
        su+=1
    if(y - j1 > 1 - cf and j1 < size - 1):
        mass[j1+1][i1]+=value    
        su+=5
    if(su==2):
        mass[j1-1][i1-1]+=value
    if(su==4):
        mass[j1-1][i1+1]+=value
    if(su==6):
        mass[j1+1][i1-1]+=value
    if(su==8):
        mass[j1+1][i1+1]+=value

def ValSep_P(x,y,value,size,mass):
    i1=math.trunc(x)
    j1=math.trunc(y)
    su=0
    if(i1 + 1 == size):
        i1-=1
        su+=1
    if(j1 + 1 == size):
        j1-=1
        su+=2
    mass[i1][j1]+=value
    if(i1>0 and j1>0):
        if(su==0):
            mass[i1-1][j1-1]+=value
            mass[i1][j1-1]+=value
            mass[i1-1][j1]+=value
        if(su==1):
            mass[i1][j1-1]+=value
        if(su==2):
            mass[i1-1][j1]+=value
    else:
        if(j1>0):
            if(su!=2):
                mass[i1][j1-1]+=value
        if(i1>0):
            if(su!=1):
                mass[i1-1][j1]+=value
    
def AddExample(filename,minr,maxr,mind,maxd,size):
    rezult=[[0]*size for i in range(size)]
    KORA=abs((size-1e-5)/(maxr-minr))
    KODA=abs((size-1e-5)/(maxd-mind))
    for line in open(filename):
        n=line.split(",")
        y=KODA*float(n[1])
        x=KORA*float(n[0])
        ValSep(x,y,1,size,cf2,rezult)#!!!!!!!!!!!!!!!!!!!!!
    return rezult    
    

def StarDensityTxtWithRad_W(x,size):
    N=len(x)

    h=[[0]*size for i in range(size)]
    #h1=[[0]*size for i in range(size)]
    flag=0
    if(np.size(x[0].split(","))/np.size(float)==2):
        flag=1
    for i in range(N):
        n=x[i].split(",")
        if (flag==0):
            var=int(n[2])#########################################################################
        else: var=1
        ValSep(float(n[0]),float(n[1]),var,size,cf2,h)

        
        '''
    for i in range(size):
        for j in range(size):
            if (not h1[i][j]==0):
                h[i][j]=h[i][j]/h1[i][j]   
        '''
        
    return h

def StarDensityTxtWithRad_P(x,size):
    N=len(x)

    h=[[0]*size for i in range(size)]
    #h1=[[0]*size for i in range(size)]
    flag=0
    if(np.size(x[0].split(","))/np.size(float)==2):
        flag=1
    for i in range(N):
        n=x[i].split(",")
        if (flag==0):
            var=int(n[2])#########################################################################
        else: var=1
        #ValSep(float(n[0]),float(n[1]),var,size,cf2,h)
        ValSep_P(float(n[0]),float(n[1]),var,size,h)
        
        '''
    for i in range(size):
        for j in range(size):
            if (not h1[i][j]==0):
                h[i][j]=h[i][j]/h1[i][j]   
        '''
        
    return h

def Moda(bach,mass,size):
    temp=[0]*bach
    #temp=[[0]*size for i in range(size)]
    max,min=-1,1
    for i in range(size):
        for j in range(size):
            if(mass[i][j]>max):
                max=mass[i][j]
            if(mass[i][j]<min):
                min=mass[i][j]
    dm=max-min
    koef_bach=(bach-1e-5)/dm
    for i in range(size):
        for j in range(size):
            temp[math.trunc((mass[i][j]-min)*koef_bach)]+=1
    maxt=-1
    index=-1
    for i in range(bach):
        if(temp[i]>maxt):
            maxt=temp[i]
            index=i
    index+=0.5
    rezult = (index*dm)/(bach-1e-5) + min
    return rezult
        

def LocalMaxima(mass,size,mode):
    rezult=[]
    for i in range(size):
        for j in range(size):
            flag=1
            if(mass[i][j]>mode):
                for i1 in range(-2,3,1):
                    for j1 in range(-2,3,1):
                        if(i1!=0 and j1!=0 and i+i1<size and i+i1>=0 and j+j1<size and j+j1>=0):
                            if(mass[i][j]<mass[i+i1][j+j1]):
                                flag=0
                                break
                    if(not flag):
                        break
            if(flag):
                line=[i,j]
                rezult.append(line)
    return rezult

def calc_lambada(loc_m,mass,step):
    loc=[]
    for i in range(len(loc_m)):
        loc.append(mass[loc_m[i][0]][loc_m[i][1]])
    #big to small
    loc.sort(reverse=True)
    dl,fl=0,0
    for i in range(len(loc)):
        if(i+1 != len(loc)):
            if(dl > loc[i+1]-loc[i]):
                return loc[i]
                '''
                fl+=1
            dl=loc[i+1]-loc[i]
            if(fl>step):
                return loc[i]
                '''

def sigma_bg(loc_m,mass,N,mode,lambada):
    sum=0
    for i in range(len(loc_m)):
        Li=mass[loc_m[i][0]][loc_m[i][1]]
        if(Li <= lambada):
            sum+=math.pow(Li-mode,2)
    return math.sqrt(sum/N)


def Parzen_P(mass,size):
    #N=len(x)
    #mass=[[0]*size for i in range(size)]
    h=[[0]*size for i in range(size)]
    bachsize=40
    localmaxima=[]
    #mass=StarDensityTxtWithRad_P(x,size)
    N=0
    for i in range(size):
        for j in range(size):
            N+=mass[i][j]
    for i in range(size):
        for j in range(size):
            h[i][j]=mass[i][j]/(N*4)
    moda=Moda(bachsize,h,size)
    localmaxima=LocalMaxima(h,size,moda)
    #
    #plt.hist(localmaxima,20)
    #
    lambada=calc_lambada(localmaxima,h,0)
    sig_bg=sigma_bg(localmaxima,h,N,moda,lambada)
    for i in range(size):
        for j in range(size):
            if(h[i][j]<2*sig_bg+moda):
                h[i][j]=0
    return h

def PforEach(mass,size):
    sum_of_all=0
    P_max = -1
    P_min = 1
    P_mass = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            sum_of_all += mass[i][j]
    for i in range(size):
        for j in range(size):
            P_mass[i][j] = mass[i][j]/sum_of_all
            if (P_max < P_mass[i][j]):
                P_max = P_mass[i][j]
            if (P_min > P_mass[i][j]):
                P_min = P_mass[i][j]
    return P_mass,P_max,P_min
    

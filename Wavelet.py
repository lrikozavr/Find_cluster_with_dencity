from our_func import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

e=2.7182818284
KF98=5.64 #1.68
KF95=3.81 #1.38
KF90=2.59 #1.14
#N=2160 #10'

#MHAT
def f(t):
    return (1-t**2)*e**((-t**2)/2)

# Главный ряд
def Ryad1(x,f,i,j):
    N=len(x)
    s,l=0,0
    a,b=round(j+3.6*i),round(j-3.6*i)
    d=a-b
    k=math.trunc(b)
    while(l<d): 
        if (k < 0):
            k += N
        elif (k == N):
            k=0
        s+=x[k]*f((l-d/2)/i)  
        k+=1
        l+=1
    return s
# Константа n
def Ryad_n(i):
    s,l=0,0
    a,b=round(3.6*i),round(-3.6*i)
    d=a-b 
    while(l<d):
        s+=e**(-0.5*(((l-d/2)/i)**2))
        l+=1
    return s    
# Автоматически центрирует ряд
def SerRyad(x):
    s=0.
    #s=0
    m=len(x)
    xk=[0]*m
    for i in range(m):
        s+=x[i]
    sr=s/m
    for i in range(m):
        xk[i]=x[i]-sr
    return xk
# Сигма в квадрате
def SigmaSqr(x):
    N=len(x)
    s=0.
    for i in range(N):
        s+=x[i]**2
    s=s/(N-1)
    return s
#
def Z(x,f,i,j):
    N=len(x)
    s=0.
    for k in range(N):
        s+=f((k-j)/float(i))**2
    z=s/Ryad_n(i)**2
    return z
#
def Wavlet(mass,ig,koef):
    size=math.trunc(pow(np.size(mass),0.5))
    kkk=[0]*size
    WWW=[[0]*size for i in range(size)]
    for p1 in range(size):
        #?
        #Так правильно, но отображает лучше другой случай
        p=abs(p1-size+1)
        kkk=SerRyad(mass[p])
        #print(kkk,np.size(kkk))
        #i=1
        for j in range(len(kkk)):
            m=Ryad1(kkk,f,ig,j)/Ryad_n(ig)
            #KF98 коэффициент для 98% вероятности
            if (m*m >= SigmaSqr(kkk)*Z(kkk,f,ig,j)*koef):
                WWW[j][p]=m*abs(m)
    return WWW
#cstride,cstride accuracy of graphic
def makeData(x,y):
    xgrid, ygrid = np.meshgrid(x, y)
    return xgrid, ygrid
#
def MainWavlet(filename,size,col,ig,koef):
    kk=[[0]*size for i in range(size)]    
    kk=StarDensityTxtWithRad_W(TxtToArray(filename,size,col),size)
    #    
    x, y = makeData(range(size),range(size))
    #
    fig=plt.figure()
    axes=Axes3D(fig)
    #
    #axes.plot_surface(x,y,np.array(Wavlet(kk,ig,koef)), rstride=1, cstride=1, cmap = cm.jet)
    axes.plot_surface(x,y,np.array(kk), rstride=1, cstride=1, cmap = cm.jet)
    fig.savefig("/home/kiril/github/Find_cluster_with_dencity/wivelet.png")
    #plt.show()
    return fig


#main("/media/kiril/j_08/skop/psqldata_catalogue/gaiadr2_BMS_79807069.txt",100,62,1,KF98)
def StarDensityTxtWithRad_W(x,size):
    N=len(x)
    h=[[0]*size for i in range(size)]
    #h1=[[0]*size for i in range(size)]
    flag=0
    if(np.size(x[0].split(","))/np.size(float)==2):
        flag=1
    for i in range(N):
        n=x[i].split(",")
        i1=math.trunc(float(n[0]))
        j1=math.trunc(float(n[1]))
        #print(i1,j1)
        #h1[j1][i1]+=1;
        if (flag==0):
            h[j1][i1]+=int(n[2])#########################################################################
        else: h[j1][i1]+=1
        '''
    for i in range(size):
        for j in range(size):
            if (not h1[i][j]==0):
                h[i][j]=h[i][j]/h1[i][j]   
        '''
    return h

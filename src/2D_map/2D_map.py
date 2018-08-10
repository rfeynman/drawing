'''
Created on Aug 9, 2018

@author: wange
'''
import numpy as np
from numpy import genfromtxt, dtype
import time
import matplotlib.pyplot as plt

import matplotlib.cm as cm
from dask.array.reshape import reshape
from mpl_toolkits.mplot3d import Axes3D
from astropy.units import ccount


def main():
    lpower=0.14*10**(-3)
    raw=genfromtxt('photocathodeMap.Aug.07.2018_13.31.txt',delimiter='\t',names=True,dtype=None)
    x=raw['X_position']
    y=raw['Y_position']
    p=raw['measurement']
   
    #print(np.reshape(y[:-3],(16,17)))

    #print(np.reshape(x[:-3],(16,17)))
    tot_length=len(x)
    rows_ind=np.unique(y)
    nrows=len(rows_ind)
    #print(ncols)
    ncols=int(tot_length/nrows)
    factor_qe=124000/532/lpower
    x_sqr=x[:nrows*ncols].reshape(ncols,nrows)
    y_sqr=y[:nrows*ncols].reshape(ncols,nrows)
    p_sqr=p[:nrows*ncols].reshape(ncols,nrows)
    
    p_qe=(p_sqr-p_sqr[0,0])*factor_qe
    print(len(x_sqr),len(y_sqr))
    #x,y=np.meshgrid(x,y))
    #print(x_grid)
    #ncols=len(y)
    
    fig1=plt.figure(1)
    ax=fig1.gca(projection='3d')
    surf_pi=ax.plot_trisurf(x[:nrows*ncols],y[:nrows*ncols],p[:nrows*ncols],cmap=cm.coolwarm)

    #plt.imshow(grid,extent=(x.min(),x.max(),y.max(),y.min()),interpolation='nearest',cmap=cm.gist_rainbow)
    fig1.colorbar(surf_pi,shrink=0.5,aspect=5)
    plt.show()
    
    fig2=plt.figure(2)
    ax2=fig2.gca(projection='3d')
    surf_qe=ax2.plot_trisurf(x[:nrows*ncols],y[:nrows*ncols],(p[:nrows*ncols]-p_sqr[0,0])*factor_qe,cmap=cm.coolwarm)

    #plt.imshow(grid,extent=(x.min(),x.max(),y.max(),y.min()),interpolation='nearest',cmap=cm.gist_rainbow)
    fig2.colorbar(surf_qe,shrink=0.5,aspect=5)
    plt.show()
    
    fig3=plt.figure(3)
    #contour_qe=plt.tricontourf(x_sqr,y_sqr,p_sqr,cmap=cm.coolwarm)#pcolormesh， contourf
    contour_qe=plt.tricontourf(x[:nrows*ncols],y[:nrows*ncols],(p[:nrows*ncols]-p_sqr[0,0])*factor_qe,cmap=cm.coolwarm)#pcolormesh， contourf
    fig3.colorbar(contour_qe,shrink=0.5,aspect=5)
    plt.show()
    return 0

if __name__ == '__main__':
    main()
'''
Created on Jan 20, 2018

@author: wange
'''

import numpy as np
from numpy import genfromtxt, dtype
import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from datetime import datetime
import dateutil
from dateutil import parser
#warnings.simplefilter("error", OptimizeWarning)

def importdata():
    raw_llbk=genfromtxt('llbkf.txt',delimiter='\t',names=True,dtype=None)
    return raw_llbk
def dataplot(llbk):
    tt=np.array(llbk['time'])
    t_beforefilter= np.array([parser.parse(d) for d in tt])
    pc_beforefilter=np.array(llbk['current'])*(-1e6)
    pc_index=pc_beforefilter>=(0.1)
    pc=pc_beforefilter[pc_index]
    #print(pc_index,t_beforefilter)
    t=t_beforefilter[pc_index]
    

    #tem=np.append(pc.T,t.T,axis=1)
    
    #print(t,pc)

    
    plt.plot(t[:23500],pc[:23500])
    plt.ylabel('Photocurrent[uA]')
    plt.xlabel('Datetime[mm-dd hr]')
    plt.gcf().autofmt_xdate()
    plt.savefig('start1.png')
    plt.show()
    
def main():
    llbkdata=importdata()
    dataplot(llbkdata)
    
if __name__ == '__main__':
    main()
'''
Created on Mar 4, 2015

@author: wange
'''

import numpy as np

import matplotlib.pyplot as plt

data=np.genfromtxt('datas.dat',delimiter='\t',skip_header=1)


data_min=np.amin(data[:,2])
data_max=np.amax(data[:,2])
margin=(data_max-data_min)/20

fig=plt.figure()
plt.hist(data[:,2], bins=20,facecolor='g')
plt.xlabel('Radius in pixel')
plt.ylabel('Accumulate')
plt.title('CysZ_X336')
plt.xlim(data_min-margin,data_max+margin)
plt.text(250,14,'')
#plt.ylim(0,280)

fig.savefig('test.pdf')
plt.show()

if __name__ == '__main__':
    pass
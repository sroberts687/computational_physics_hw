# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


# read in text files
data = np.genfromtxt('C:\\Users\\srobe\\Desktop\\ax.txt')
data2 = np.genfromtxt('C:\\Users\\srobe\\Desktop\\ay.txt')

# set up grid / mesh
x = np.linspace(-2,2,200)
y = np.linspace(-2,2,200)
nx = 2
ny = 2
x=np.arange(-nx,nx,1)
y=np.arange(-ny,ny,1)
xi,yi=np.meshgrid(x,y)

N = 5
Fx = data[::, ::] 
Fy = data2[::, ::] 
nrows, ncols = Fx.shape

nx = 5
ny = 5
x = np.linspace(-nx, nx, ncols)
y = np.linspace(-ny, ny, nrows)
xi, yi = np.meshgrid(x, y, indexing='ij')

plt.axes([0.065, 0.065, 0.9, 0.9])
plt.quiver(xi, yi, Fx, Fy, alpha=.5)
plt.quiver(xi, yi, Fx, Fy, edgecolor='k', facecolor='none', linewidth=.5)

plt.show()


# read in potential from file
z = np.genfromtxt('C:\\Users\\srobe\\Desktop\\potential.txt')
plt.contour(x,y,z)
plt.show()





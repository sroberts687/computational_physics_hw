# -*- coding: utf-8 -*-
"""
HW3 Python Script

Sarah Roberts
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


# read in text files
#data = np.genfromtxt('C:\\Users\\srobe\\Desktop\\ax_311.txt')




# Part 2.1

#initialize x and y
x = np.linspace(-1,1,200)
y = 1/(25*x*x+1)

plt.plot(x,y)
#plt.savefig('C:\\Users\\srobe\\Desktop\\2_1.png')
plt.show
plt.close()
plt.clf()


# read in text files
data = np.genfromtxt('C:\\Users\\srobe\\Desktop\\ax_10011.txt')
data2 = np.genfromtxt('C:\\Users\\srobe\\Desktop\\ay_10011.txt')

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

nx = 2
ny = 2
x = np.linspace(-nx, nx, ncols)
y = np.linspace(-ny, ny, nrows)
xi, yi = np.meshgrid(x, y, indexing='ij')

plt.axes([0.065, 0.065, 0.9, 0.9])
plt.quiver(xi, yi, -1*Fx, -1*Fy, alpha=.5)
plt.quiver(xi, yi, -1*Fx, -1*Fy, edgecolor='k', facecolor='none', linewidth=.5)



# read in potential from file
z = np.genfromtxt('C:\\Users\\srobe\\Desktop\\potential_10011.txt')
plt.contour(x,y,z)

#plt.show()
plt.savefig('C:\\Users\\srobe\\Desktop\\2b.png')
plt.close
plt.clf()

# L2 =  1.0985546875

plt.plot([0.4464], [0], marker='o', markersize=3, color="red")
plt.plot([1.0986], [0], marker='o', markersize=3, color="red")
plt.plot([-1.744], [0], marker='o', markersize=3, color="red")
plt.plot([0], [1.0], marker='o', markersize=3, color="red")
plt.plot([0], [-1.0], marker='o', markersize=3, color="red")


x1 = -(1/101)*1
x2 = (100/101)*1
plt.plot([x1], [0], marker='o', markersize=7, color="blue")
plt.plot([x2], [0], marker='o', markersize=7, color="blue")

cx = 100/(100+3)*1  #x1
cy = 0
rad = 1.0985546875-x2  # L2

circle= plt.Circle((x2,0), radius= rad, fill =False)
ax=plt.gca()
ax.add_patch(circle)
plt.axis('scaled')
#plt.show()
plt.savefig('C:\\Users\\srobe\\Desktop\\4.png')



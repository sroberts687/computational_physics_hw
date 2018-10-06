# -*- coding: utf-8 -*-
"""
HW3 Python Script

Sarah Roberts
"""

import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate


def Lagrange( n, x2 ):
 # implement Neville's algorithm, as described in Burden-Faire's
 # Numerical Analysis text
    k = [[0 for x in range(n+1)] for y in range(n+1)] 
    for i in range(0,n):
        k[i][0] = y[i]
     
    for l in range(1, 200):
        thisx = x2[l]
        for i in range(1, n):
            for j in range(1, i, 1):
                k[i][j] = ((thisx - x[i-j])*k[i][j-1] - (thisx-x[i])*k[i-1][j-1])
                k[i][j] = k[i][j] / (x[i] - x[i-j])
                
        y2[l] = k[i][j]
        plt.plot(x2, y2)


def fn( a ):
    return 1/(25*a*a + 1)





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

# Lagrange Polynomials -- neville's algorithm





x2 = np.linspace(-1, 1, 200)
y2 = np.linspace(-1,1,200)


#degree = 6, 8, 10
x = np.linspace(-1, 1, 7)
y = fn(x)
Lagrange(6, x2)


x = np.linspace(-1, 1, 9)
y = fn(x)
Lagrange(8, x2)

x = np.linspace(-1, 1, 11)
y = fn(x)
Lagrange(10, x2)


plt.plot(x,y)
plt.xlim([-0.75, 0.75])
plt.ylim([-0.1,1])
plt.show()
plt.close()


#plt.show()
##plt.savefig('C:\\Users\\srobe\\Desktop\\4.png')



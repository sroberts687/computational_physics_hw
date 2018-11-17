# -*- coding: utf-8 -*-
"""
HW5 Python Script

Sarah Roberts
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate

### Notes on traffic flow problem
### traffic flow
###     v = v_m ( 1 - p / p_m )   if p < p_m
###     v = 0                     if p >= p_m 
###     v_m is max speed 
###     p_m is max density
### Burger's Equation 
###     dp/dt = - d/dx((a + 1/2 * b * p)p)
###     a = v_m and b = -2*v_m/p_m
### We're actually looking to solve non-linear advection equation
###     dp/dt = -c(p)*dp/dx
###     c(p) = v_m(1-2*p/p_m)
###     p(x, t=0) = p_0(x)



def FTCS():
  
    #F(p) = p(x,t)*c(p(x,t))
    F[i] = p[i]* c(p[i]) # i is index in time
    p[i, n+1] = p[n, i] - /tau /(2*h)(F^n_{i+1}-F^n_{i-1}
  
  
    
    return someVar
    
def Lax():
    
    return someVar

def LaxWendroff():
    
    return someVar

def c(p, i, n):
    return vm*(1 - 2*p[i,n]/pm)


print("Homework Five")

#define some constants
vm = 1  # v_max
pm = 1  # p_max
p0 = 0.5  #p(x, t=0)

print("FTCS solution to the traffic problem")
print("3D plot of density vs. position and time")
print()

time = np.linspace(0, 100, 1)   # n
space = np.linspace(0, 100, 1)  # j

p = [[0 for x in range(space)] for y in range(time)] 
for j in range( 0, len(space) ):
    for n in range(0, len(time)):
        p[j, n+1] = -1*c(p) 




print("Lax solution to the traffic problem")
print("3D plot of density vs. position and time")
print()

print("Lax-Wendroff solution to the traffic problem")
print("3D plot of density vs. position and time")
print()

print()



#plt.plot(nVals, eErrorVals)
#plt.plot(nVals, rkErrorVals)
##plt.savefig('C:\\Users\\srobe\\Desktop\\eulerRKErrors.png')
#plt.close()


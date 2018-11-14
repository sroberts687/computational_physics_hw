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
### We're actually looking to solve non-linear advection equtation
###     dp/dt = -c(p)*dp/dx
###     c(p) = v_m(1-2*p/p_m)
###     p(x, t=0) = p_0(x)



def FTCS():
    
    return someVar
    
def Lax():
    
    return someVar

def LaxWendroff():
    
    return someVar


print("Homework Five")
print("FTCS solution to the traffic problem")
print("3D plot of density vs. position and time")
print()


print("Lax solution to the traffic problem")
print("3D plot of density vs. position and time")
print()

print("Lax-Wendroff solution to the traffic problem")
print("3D plot of density vs. position and time")
print()

print



#plt.plot(nVals, eErrorVals)
#plt.plot(nVals, rkErrorVals)
##plt.savefig('C:\\Users\\srobe\\Desktop\\eulerRKErrors.png')
#plt.close()


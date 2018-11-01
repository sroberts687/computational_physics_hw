# -*- coding: utf-8 -*-
"""
HW4 Python Script

Sarah Roberts
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate

def Trap(f,x):

    h = (x[len(x)-1] - x[0])/len(x)

    trapSum = 0
    for i in range(1, len(x)):
        trapSum += f(x[i-1]) + f(x[i])

    return h/2*trapSum

def Simp(f,x):
    
    h = (x[len(x)-1] - x[0])/len(x)
    
    simpSum = 0
    for i in range(0, len(x)-2):
        SimpSum += x[i] + 4*x[i+1] + x[i+2]
    
    simpSum = h/3*simpSum
    
    smallx = []
    smallx.append(x[0])
    smallx.append(x[1])
    simpSum += Trap(f,smallx)
    
    smallx[0] = x[len(x) - 1]
    smallx[1] = x[len(x)]
    simpSum += Trap(f,smallx)
    
    return simpSum


def f(x):
    return x**2 + 2*x + 2

def F(x): 
    return 1/3 * x**3 + x**2 + 2*x

n = 1000
x = np.linspace(-1, 1, n)
xIntApx = Trap(f,x)
xIntTrue = F(x[len(x)-1]) - F(x[0])

print("approx int is ", xIntApx, " for n = ", n) 
print("analytical int is ", xIntTrue)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100)

xIntApx = Simp(f,x)

print("approx int is ", xIntApx, " for n = ", n) 
print("analytical int is ", xIntTrue)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100)


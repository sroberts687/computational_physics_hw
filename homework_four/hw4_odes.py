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


# -*- coding: utf-8 -*-
"""
HW4 Python Script

Sarah Roberts
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate

def Trap(f,xmin, xmax):
    
    maxn = 1E4
    thresh = 1E-5       # 1E-7 (can get 0.01 % error, but slow)
    
    
    lastSum = 0
    thisSum = 1
    n = 1
    
    while abs(lastSum - thisSum) > thresh and n < maxn :
        lastSum = thisSum
        
        x = np.linspace(xmin, xmax, n)
    
        h = (x[len(x)-1] - x[0])/len(x)
    
        trapSum = 0
        for i in range(1, len(x)):
            trapSum += f(x[i-1]) + f(x[i])

        trapSum = h/2*trapSum
        
        thisSum = trapSum
            
        n += 1
        
    #print("n = ", n-1)
        
    return thisSum

def Simp(f,xmin, xmax):
    
    maxn = 1E4
    thresh = 1E-5       # 1E-7 (can get 0.01 % error, but slow)
    
    
    lastSum = 0
    thisSum = 1
    n = 3
    
    while abs(lastSum - thisSum) > thresh and n < maxn :
        lastSum = thisSum
        x = np.linspace(xmin, xmax, n)
         
        h = (x[len(x)-1] - x[0])/2*len(x)
    
        simpSum = 0
        for i in range(0, len(x)-3):
            simpSum += x[i] + 4*x[i+1] + x[i+2]
        
        simpSum = h/3*simpSum
        
        smallx = []
        smallx.append(x[0])
        smallx.append(x[1])
        simpSum += Trap(f,smallx[0], smallx[len(smallx)-1])
        
        smallx[0] = x[len(x) - 2]
        smallx[1] = x[len(x)-1]
        simpSum += Trap(f,smallx[0], smallx[1])
        
        thisSum = simpSum
        n += 1
    
    return simpSum


def g(x):
    return x**2 + 2*x + 2

def G(x): 
    return 1/3 * x**3 + x**2 + 2*x

def f(x):
    return 1/math.sqrt(2*math.pi)*math.e**((-1*(x-1)**2)/2)



print("Trapezoid Rule Test")

n = 1000
x = np.linspace(-1, 1, n)

xIntApx = Trap(g,-1, 1)
xIntTrue = G(x[len(x)-1]) - G(x[0])

print("approx int is ", xIntApx) 
print("analytical int is ", xIntTrue)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100)

print()
print("Simpson's Rule Test")
xIntApx = Simp(g,-1, 1)

print("approx int is ", xIntApx, " for n = ", n) 
print("analytical int is ", xIntTrue)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100)


print()
print("Part 1b")
print()


#for i in range(1, 10):
#    n = 10*i
#    x = np.linspace(-100, 100, n)
#    
#    intApx = Trap(f, x)
#    intTrue = 1.0
#    
#    print("approx int is ", xIntApx, " for n = ", n) 
#    print("analytical int is ", xIntTrue)
#    print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100)
#    print()
    









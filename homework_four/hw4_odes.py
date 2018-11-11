# -*- coding: utf-8 -*-
"""
HW4 Python Script

Sarah Roberts
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate

def Trap(f,xmin, xmax, makePlots):
    
    maxn = 1E4
    thresh = 1E-5       # 1E-7 (can get 0.01 % error, but slow)
    
    if makePlots:
        ns = []
        errs = []
    
    
    
    lastSum = 0
    thisSum = 1000
    
    # start at an even value -- otherwise fns symmetric about zero integrated 
    # on x = -a to x = +a will integrate to zero (as will translations of such
    # functions)
    
    n = 2       
    
    while abs(lastSum - thisSum) > thresh and n < maxn :
        lastSum = thisSum
        
        x = np.linspace(xmin, xmax, n)
    
        h = (x[len(x)-1] - x[0])/len(x)
    
        trapSum = 0
        for i in range(1, len(x)):
            trapSum += f(x[i-1]) + f(x[i])

        trapSum = h/2*trapSum
        
        thisSum = trapSum
            
        if makePlots:
            ns.append(n)
            errs.append(abs(lastSum - thisSum))
        
        n += 5
        
    #print("n = ", n-1)
    
    if makePlots:
        ns.pop(0)
        errs.pop(0)
        
        plt.plot(ns, errs)
        plt.show
    
    
    if (n-1 >= maxn):
        print("maxn reached in Trap()")
    
    #print("n = ", n)
    
    return [thisSum, n-5]

def Simp(f,xmin, xmax, makePlots):
    
    maxn = 1E4
    thresh = 1E-5       # 1E-7 (can get 0.01 % error, but slow)
    
        
    if makePlots:
        ns = []
        errs = []
    
    lastSum = 0
    thisSum = 1
    n = 5
    
    while abs(lastSum - thisSum) > thresh and n < maxn: #maxn :
        lastSum = thisSum
        
        h = (xmax - xmin)/n
        x = np.linspace(xmin, xmax, n)
        
        thisSum = 0        
              
        for i in range(0, len(x)):
            if i%2 == 0:
                thisSum += 2*f(x[i])
            else:
                thisSum += 4*f(x[i])

        thisSum *= (h/3.0)

        if makePlots:
            ns.append(n)
            errs.append(abs(lastSum - thisSum))

        #print(n, "/t", thisSum)
        
        n += 4
    
        
    if makePlots:
        ns.pop(0)
        errs.pop(0)
        
        plt.plot(ns, errs)
        plt.show
    
    if (n-1 >= maxn):
        print("maxn reached in Simp()")
    
    #print("n = ", n)
    
    return [thisSum, n - 4]


def g(x):
    return x**2 + 2*x + 2

def G(x): 
    return 1/3 * x**3 + x**2 + 2*x

def f(x):
    return 1/math.sqrt(2*math.pi)*math.e**((-1*(x-1)**2)/2)


def Euler(n, x0, makePlots):

    n = 50
    t = np.linspace(0,1,n)      # want to solve ode on t = 0, 1
    x = np.linspace(0,n,n)      # placeholders for output
    x[0] = 1     # initial condition x(t=0) = 1
    h = t[1] - t[0]
    
    for i in range(1, n):
        deriv = dxdt(x[i-1], t[i-1])
        x[i] = x[i-1] + h * deriv
    
    if makePlots:
#        plt.plot(t, x)
        plt.plot(t,dxdt(x,t))
        plt.plot(t, soln(t))
        plt.show

def dxdt(x,t):
    return 4*x - t + 1

def soln(t):
    e = math.e
    return 1/16*(4*t+19*e**(4*t)-3)    


print("Part 1a")
print("Calculate Int[x^2 + 2x + 2] from x = -1 to x = +1")
print()

n = 1000
x = np.linspace(-1, 1, n)
xIntTrue = G(x[len(x)-1]) - G(x[0])

print("analytical int is ", xIntTrue)

ary = Trap(g, -1 , 1, False)
xIntApx = ary[0]
thisN = ary[1]
print("approx int using the Trap rule is ", xIntApx) 
print("converged for n = ", thisN)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100, "%")

print()

print("Simp convered with ")
ary = Simp(g,-1, 1, False)
xIntApx = ary[0]
thisN = ary[1]
print("approx int using Simp's rule is ", xIntApx) 
print("converged for n = ", thisN)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100, "%")

print()
print("Part 1b")
print()

print("analytical int is 1.0")
xIntTrue = 1.0


ary = Trap(f, -100 , 100, True)
xIntApx = ary[0]
thisN = ary[1]
print("approx int using the Trap rule is ", xIntApx) 
print("converged for n = ", thisN)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100, "%")

print()

print("Simp convered with ")
ary = Simp(f,-100, 100, True)
xIntApx = ary[0]
thisN = ary[1]
print("approx int using Simp's rule is ", xIntApx) 
print("converged for n = ", thisN)
print("percent error is ", abs(xIntTrue - xIntApx)/xIntTrue * 100, "%")

print()
print("Note that Simpson's rule takes much less time to converge than the Trapezoidal rule.")
print()
print()

plt.gcf().clear()

print("Part 2")

Euler(50, 1, True)

n = 50
t = np.linspace(0,1,n+1)      # want to solve ode on t = 0, 1
x = np.linspace(0,n,n+1)      # placeholders for output
x[0] = 1     # initial condition x(t=0) = 1
h = t[1] - t[0]

kvals = [0,0,0,0,0]

for i in range(1, n+1):
	
    kvals[1] = h * dxdt(x[i-1], t[i-1])
    kvals[2] = h * dxdt(x[i-1] + h / 2.0, t[i-1] + kvals[1] / 2.0)
    kvals[3] = h * dxdt(x[i-1] + h / 2.0, t[i-1] + kvals[2] / 2.0)
    kvals[4] = h * dxdt(x[i-1] + h, t[i-1] + kvals[3])
    	
    #print(kvals[1], " ", kvals[2], " ", kvals[3], " ", kvals[4])

    if (i < n+1):
        x[i] = x[i-1] + (kvals[1] + 2.0 * (kvals[2] + kvals[3]) + kvals[4] ) / 6.0
        t[i] = t[i-1] + h
	
plt.plot(t, x)	










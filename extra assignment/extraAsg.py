# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import random

def g(x):   # g(x) = x^2 + 3x + 1
    return(x**2 + 3*x + 1)
def G(x):   # 1/3 x^3 + 3/2 x^2 + x
    return ((1/3)*x**3 + (3/2)*x**2 + x )


print("Computational Physics: Extra Assignment")
print("Planetary orbits with leapfrog")
print("\t Sarah Roberts")

m1 = 1.989*10**30       #kg     sun
m2 = 5.972 * 10 ** 24   #kg     earth
q = m1/m2

#r0 = (1.0 - ecc)*a/(1.0 + q)
#v0 = 29300
# # http://curious.astro.cornell.edu/our-solar-system/41-our-solar-system/the-earth/orbit/85-how-fast-does-the-earth-go-at-perihelion-and-aphelion-intermediate

r12 = 152095560883      #m (max distance b/w sun and earth)
G =  6.674*10**(-11)    # Cavendish const N*m^2/kg^2)

maxTime = 365 * 3       # three years

r1 = [] # sun
r1.append(0)
v1 = []
v1.append(0)

r2 = [] # earth
r2.append(r12)
v2 = []
v2.append(29300)    



time = np.linspace(0, maxTime, maxTime)       # time step is 12 h



for n in range (0, maxTime):
    
    r1.append(0)
    v1.append(0)
    r2.append(0)
    v2.append(0)
    
    dt = time[n] - time[n-1]
    
    
    #x1[n+1] = x1[n] + dt*vx1[n+1/2]
    r1[n+1] = r1[n] + dt*v1[n]
    #vx1[n + 3/2] = vx1[n + 1/2] + (G*m2/[r12**2])*((x2[n+1]-x1[n+1])/r12)a
    r12 = r1[n] - r2[n]
    a1 = G*m2*(r2[n]-r1[n]) / (r12**3)
    v1[n+1] = v1[n] + dt*a1
    
    r12 *= -1
    r2[n+1] = r2[n] + dt*v2[n]
    a2 = G*m1*(r1[n]-r2[n]) / (r12**3)
    v2[n+1] = v2[n] + dt*a2

r1.pop(0)
r2.pop(0)
#time.pop(0)

plt.plot(time, r1)
#plt.plot(time, r2)

print()
print()
print("End of program reached.")
print("Goodbye.")


















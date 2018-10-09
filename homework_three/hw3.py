# -*- coding: utf-8 -*-
"""
HW3 Python Script

Sarah Roberts
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#import scipy.interpolate

def fn( tmp ):
    return 1/(25*tmp*tmp + 1)

def lorent(a, v, v0):
    PI = 3.1415926535897932384
    return a / ( PI * (v - v0)*(v - v0) + a*a)

def dlda(a, v, v0):
    PI = 3.1415926535897932384
    return (PI * math.pow(v-v0,2) - a*a) / (math.pow(a*a + PI * math.pow(v - v0, 2), 2) )

def dldv0(a, v, v0): 
    PI = 3.1415926535897932384
    num = 2 * PI *a * (v - v0)
    denom = math.pow(a*a + PI * math.pow(v - v0, 2),2)
    return num / denom


def gaus(a, v, v0):
    const = 0.46971863935 #sqrt(ln(2)/PI)
    ln2 = 0.69314718056
    e = 2.718281828459
    exp = -1*(ln2)*(v-v0)*(v-v0)/(a*a)
    return 1 / a * const * math.pow(e,exp)
    
def dgda(a, v, v0):
    const = 0.46971863935 #sqrt(ln(2)/PI)
    ln2 = 0.69314718056
    num = -1 * ( const * math.pow(2,-1 * math.pow(v0 - v, 2) / (a*a)) )
    num = num * ( math.pow(a,2) - 2 * ln2 * math.pow(v0 - v, 2))
    denom = math.pow(a, 4)
    return num / denom
    
    
def dgdv0(a, v, v0):
    PI = 3.1415926535897932384
    ln2 = 0.69314718056
    num = -1 * (math.pow(ln2, 3/2) * (v0 - v) )
    num = num * math.pow(2, (1 - math.pow(v0 - v, 2) / (a*a)))
    denom = math.sqrt(PI) * math.pow(a,3)
    return num / denom


def chi2(a, v0, v, phi, method):
    chi = 0
    
    if method == 1:
        # use lorent
        for i in range(1, 100):
           chi2 = chi + math.pow((phi[i] - lorent(a, v[i], v0)),2)
    else:
        # use gaus
        for i in range(1, 100):
             chi2 = chi + math.pow((phi[i] - gaus(a, v[i], v0)),2)
        
    return 

def dchidal(p, a, v, v0):  # partial derivative of chi^2 wrt alpha for phi = lorentz(v)
    PI = 3.1415926535897932384
    temp  = 2 * ((2*a*a)/math.pow(a*a + PI * math.pow(v - v0, 2), 2) - 1/(a*a + PI *math.pow(v - v0,2)) )
    temp = temp * (p - a/(a*a + PI * math.pow(v - v0, 2) ) )
    return temp

def dchidv0l(p, a, v, v0): # partial derivative of chi^2 wrt v_0 for phi = lorentz(v)
    PI = 3.1415926535897932384
    num = -1*(4* PI * a * (v - v0) * (a*a * p - a + PI * p * math.pow(v0 - v, 2)))
    denom = math.pow(a*a + PI * math.pow(v0 - v, 2), 3)
    return num / denom

def dchidag(p, a, v, v0): # partial derivative of chi^2 wrt alpha for phi = gauss(v)
    ln2 = 0.69314718056
    c = 0.46971863935 #sqrt(ln(2)/PI)
    s = -1 * math.pow(v-v0, 2)/(a*a)
    t1 = 2*(p - (c*math.pow(2, s))/a)
    t2 = c*math.pow(2, s)/(a*a)
    t3 = c*ln2*math.pow(v- v0,2)*math.pow(2, 1+s)/math.pow(a,4)
    return t1* (t2 - t3)
    
def dchidv0g(p, a, v, v0): # partial derivative of chi^2 wrt v_0 for phi = gauss(v)
    ln2 = 0.69314718056
    c = 0.46971863935 #sqrt(ln(2)/PI)
    temp = c * ln2 * (v-v0)*math.pow( 2, 2-math.pow(v-v0, 2)/a*a)
    temp = temp * (p - c * math.pow(2, -1*math.pow(v-v0, 2)/a*a) / a)
    return temp / a*a*a

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


def error(p, a, v, v0, method):
    error = 0
    
    for i in range(0, 100):
        if method == 1:     #lorentz
            error = error + (y - lorent(a, v, v0))**2
        else:    # gauss
            error = error + (y - gaus(a, v, v0))**2

    return error


def gradient_descent(p, a, v, v0):
    n = 100     # num points in data file
    h = 0.01    # step size
    
    agrad = 0   
    v0grad = 0
    
    # loop over data points and search for direction of steepest descent    
    for i in range(0, n):
        
        # check for NaNs
        if(math.isnan(p[i])):
            print("phi(v)[", i, "] is nan")
            continue
        if(math.isnan(v[i])):
            print("v[", i, "] is nan")
            continue
        
        dchidalVal =  -1 / (2 * n) * dchidal(p[i], a, v[i], v0)
        dchidv0lVal = -1 / (2 * n) * dchidv0l(p[i], a, v[i], v0)
        
        agrad = agrad + dchidalVal
        v0grad = v0grad + dchidv0lVal
        
        anew = a - h*agrad
        v0new = v0 - h*v0grad
                
    return anew, v0new
  
     

# same as gradient_descent, but uses gaussian
def gradient_descent2(p, a, v, v0):
    n = 100     # num points in data file
    h = 0.01    # step size
    
    agrad = 0   
    v0grad = 0
    
    # loop over data points and search for direction of steepest descent    
    for i in range(0, n):
        
        # check for NaNs
        if(math.isnan(p[i])):
            print("phi(v)[", i, "] is nan")
            continue
        if(math.isnan(v[i])):
            print("v[", i, "] is nan")
            continue
        
        dchidagVal = dchidag(p[i], a, v[i], v0)
        dchidv0gVal = dchidv0g(p[i], a, v[i], v0) 
        
        agrad = agrad + dchidagVal
        v0grad = v0grad + dchidv0gVal
        
        anew = a - h*agrad
        v0new = v0 - h*v0grad
                
    return anew, v0new


def splines(n):
    
    # define x_js over which splines will be evaluated
    x3 = np.linspace(-1, 1, 200)
    y3 = [0]*200   # placeholder
    
    # define arrays to hold spline coefficients
    h = [0]*(n+1)
    alpha = [0]*(n+1)
    b = [0]*(n+1)
    c = [0]*(n+1)
    d = [0]*(n+1)
    a = y   # a = f(x) = y
    
    # define arrays to hold tridiag matrix vals
    l = [0]*(n+1)
    u = [0]*(n+1)
    z = [0]*(n+1)
    
    # define steps
    for i in range(0, n):       #NOTE: range(o, n) actually loops i = 0 --> i = n-1
        h[i] = x[i+1] - x[i]
    #   additional output for debugging
    #    print(i, h[i])
    
    # find the a_j vals
    
    for i in range(1, n):
        alpha[i] = (3 / h[i])*(a[i+1]-a[i])
        alpha[i] = alpha[i] - (3 / h[i-1])*(a[i] - a[i-1])
    
    # solve tridiag matrix  
    l[0] = 1
    l[n] = 1
    
    u[0] = 0
    
    z[0] = 0
    z[n] = 0
    x
    
    for i in range(1, n):
        l[i] = 2*(x[i+1]- x[i-1]) - h[i-1]*u[i-1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    
    # solve coefficients
    # note: loop variable decreases b/c we have to work from 
    # bottom row of matrix to the top
    c[n] = 0
    for i in range (n-1, 0, -1):
        c[i] = z[i] - u[i]*c[i+1]
        b[i] = (a[i+1] - a[i]) / h[i] - h[i]*(c[i+1] + 2*c[i]) / 3
        d[i]= (c[i+1] - c[i]) / (3 * h[i])
    
    
    
    
    # apply spline formula that was just constructed
    #    y3[i] = a_j + b_j(dx) + c_j(dx)^2 + d_j(dx)^3 when dx=x-x_j
    
    for i in range(0, 199):
        if x3[i] <= x[1]:
            t = 1
            
        elif x3[i] <= x[2] :
            t = 2
            
        elif x3[i] <= x[3]:
            t = 3
            
        elif x3[i] <= x[4]:
            t = 4
    
        elif x3[i] <= x[5]:
            t = 5
            
        elif x3[i] <= x[6]:
            t = 6
            
        elif x3[i] <= x[7]:
            t = 7
            
        elif x3[i] <= x[8]:
            t = 8
            
        elif x3[i] <= x[9]:
            t = 9
            
        elif x3[i] <= x[10]:
            t = 10
        
        y3[i] = a[t] + b[t]*(x3[i]-x[t]) + c[t]*((x3[i]-x[t])*(x3[i]-x[t]))
        y3[i] = y3[i] + d[t]*(x3[i]-x[t])*(x3[i]-x[t])*(x3[i]-x[t])
    
    return y3
    


            ##############################################
            #################### MAIN ####################
            ##############################################
            
print("HW 3 : Computational Physics")
print("\t S. Roberts")
print("\n")
print("Part 1: Levenberg-Marquardt")

# read in data file
data = np.genfromtxt('C:\\Users\\srobe\\source\\repos\\computational_physics_hw\\homework_three\\hw3_fitting.dat')
v = []
phi = []
err = []

for i in range(0, 100):
    v.append(data[i][0])
    phi.append(data[i][1])
    err.append(data[i][2])
    
#    g = chi(phi(v))
    
a = 18
v0 = 38.5
for i in range(0, 10000):
    a, v0 = gradient_descent(phi, a, v, v0)
    err = (phi, a, v, v0, 1)

phiNew = []
for i in range(0, 100):
    phiNew.append(lorent(a, v[i], v0))
    
# plot lorentzian
plt.plot(v, phi); plt.plot(v,phiNew)
plt.savefig('C:\\Users\\srobe\\Desktop\\12.png')
plt.close()
plt.clf()

# repeat for gaussian
a = 20
v0 = 48
for i in range(0, 10000):
    a, v0 = gradient_descent2(phi, a, v, v0)
    err = (phi, a, v, v0, 1)

phiNew = []
for i in range(0, 100):
    phiNew.append(gaus(a, v[i], v0))

# plot gaussian
plt.plot(v, phi); plt.plot(v,phiNew)
plt.show()
plt.savefig('C:\\Users\\srobe\\Desktop\\13.png')
plt.close()
plt.clf()

# plot raw data
plt.plot(v, phi); plt.plot(v,phiNew)
plt.savefig('C:\\Users\\srobe\\Desktop\\11.png')
plt.close()
plt.clf()

print("Part 2: Data Interpolation")

# Part 2.1

#initialize x and y
x = np.linspace(-1,1,200)
y = 1/(25*x*x+1)

plt.plot(x,y)
plt.savefig('C:\\Users\\srobe\\Desktop\\21.png')
#plt.show
plt.close()
#plt.clf()


# Part 2.2

# Lagrange Polynomials -- neville's algorithm
x2 = np.linspace(-1, 1, 200)
y2 = np.linspace(-1,1,200)


#degree = 6
x = np.linspace(-1, 1, 7)
y = fn(x)
Lagrange(6, x2)

# degree = 8
x = np.linspace(-1, 1, 9)
y = fn(x)
Lagrange(8, x2)

# degree = 10
x = np.linspace(-1, 1, 11)
y = fn(x)
Lagrange(10, x2)

# adjust bounds on the plot (this hides the "tails" from the Lagrange
# interpolants, but makes the behaviour around x=0 much easier to see).
plt.xlim([-0.75, 0.75])
plt.ylim([-0.1,1])
#plt.show()
plt.savefig('C:\\Users\\srobe\\Desktop\\22.png')



# Part 2.3

# Natural Cubic Splines

# define sets of 10 points -- interpolants
x = np.linspace(-1, 1, 11)
y = fn(x)

n = 10  #solving on 10 intervals --> need 11 values
x3 = np.linspace(-1, 1, 200)
y3 = splines(n)

plt.plot(x3, y3)
plt.ylim([-0.1,1.1])
#plt.show()

plt.savefig('C:\\Users\\srobe\\Desktop\\23.png')
plt.close()
plt.clf()


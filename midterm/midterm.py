import numpy as np
import matplotlib.pyplot as plt 
import random
import pandas as pd

def easy_function(x):
    return((3)*(x**2))

def hard_function(x):
    return((1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2))

def f(x):
    return x**2 + 2

def integrate(x1,x2,func,n):

    xvals = np.linspace(x1, x2, n)
    ymin = min(f(xvals)) - 1
    ymax = max(f(xvals)) + 1
    
    xout = []
    yout = []
    check = []
    
    area=(x2-x1)*(ymax-ymin )
    
    for i in range(n):
        x = random.uniform(x1,x2)
        xout.append(x)
        y = random.uniform(0,f(x2))
        yout.append(y)
        if abs(y)>abs(func(x)) or y<0:
          check.append(0)     
        else:
          check.append(1)
          
    #print(np.mean(check)*area)
    return(np.mean(check)*area,xout,yout,check)




print ("Computational Physics: Midterm Assignment")
print("\t Sarah Roberts")

#n = 100
x1 = -5
x2 = 5
y1 = f(x1)
y2 = f(x2)

#logical for development, if .true. then time-intensive code does not run
saveTime = True


#plot function
#xvals = np.linspace(x1, x2, 1000)
#plt.plot(xvals,f(xvals))
#plt.show()

print("int(f(x) from -1 to 1 is 4.666666666....") 
true = 4.66666666666666667
val = integrate(-1, 1, f, 100)[0]
print("estimate for n = 100 is ", val )
print("\t error is", abs(true-val)/true*100, "%")
val = integrate(-1,1, f, 1000)[0]
print("estimate for n = 1 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")

if saveTime == False:
    val1 = integrate(-1, 1, f, 1000000)[0]
    print("1st estimate for n = 1 000 000 is ",  val1)
    print("\t error is", abs(true-val1)/true*100, "%")
    val2 = integrate(-1, 1, f, 1000000)[0]
    print("2nd estimate for n = 1 000 000 is ",  val2)
    print("\t error is", abs(true-val2)/true*100, "%")
    val3 = integrate(-1, 1, f, 1000000)[0]
    print("3rd estimate for n = 1 000 000 is ",  val3)
    print("\t error is", abs(true-val3)/true*100, "%")
    print()
    val = (val1+val2+val3)/3
    print("avg of 3 estimates for n = 1 mil is ", val)
    print("\t error is", abs(true-val)/true*100, "%")


print()
print()
print("int(f(x) from -2 to 4 is 36....") 
true = 36.0
val = integrate(-2, 4, f, 1000)[0]
print("estimate for n = 1 000 is ", val )
print("\t error is", abs(true-val)/true*100, "%")
val = integrate(-2, 4, f, 10000)[0]
print("estimate for n = 10 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")
val = integrate(-2, 4, f, 1000000)[0]
print("estimate for n = 100 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")


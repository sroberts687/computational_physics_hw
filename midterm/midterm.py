'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
import numpy as np
import matplotlib as plt



import numpy as np
import matplotlib.pyplot as plt

def easy_function(x):
    return((3)*(x**2))

def hard_function(x):
    return((1/np.sqrt(2*np.pi))*np.exp(-(x**2)/2))

def f(x):
    return x**2 + 2

def integrate(x1,x2,func=easy_function,n=100000):
    n = 100
    x1 = -5
    x2 = 5
    y1 = f(x1)
    y2 = f(x2)
    xvals = np.linspace(x1, x2, n)
    yvals = f(xvals)
    
    for i in range(n):
        x = np.random(x1,x2)
        samplex.append(x)
        y = np.random(y1,y2)
        sampley.append(y)
        if abs(y)>abs(func(x)) or y<0:
          check.append(0)     
        else:
          check.append(1)
          
    print(np.mean(check)[0])
    return(np.mean(check)*area,xs,ys)


print ("Computational Physics: Midterm Assignment")
print("\t Sarah Roberts")

X=np.linspace(-20,20,1000)
plt.plot(X,easy_function(X))
plt.show()

plt.plot(X,hard_function(X))
plt.show()
print(integrate(0.3,2.5)[0])
print(integrate(0.3,2.5,hard_function)[0])

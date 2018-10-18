import numpy as np
import matplotlib as plt

def f(x):
    return x**2 + 2

print ("Computational Physics: Midterm Assignment")
print("\t Sarah Roberts")


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

print(integrate(0.3,2.5)[0])
print(integrate(0.3,2.5,hard_function)[0])

% https://barnesanalytics.com/monte-carlo-integration-in-python 

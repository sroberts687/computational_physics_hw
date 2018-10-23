import numpy as np
import matplotlib.pyplot as plt
import random

def g(x):   # g(x) = x^2 + 3x + 1
    return(x**2 + 3*x + 1)
def G(x):   # 1/3 x^3 + 3/2 x^2 + x
    return ((1/3)*x**3 + (3/2)*x**2 + x )

def f(x):
    return x**2 + -2

def F(x):
    return (1/3)*x**3-2*x

def integrate(x1,x2,func,n):
    
    integral = 0
    
    for i in range(0, n):
        integral += func(random.uniform(x1,x2))
    
    integral = (x2-x1) * integral / n
    
    return integral

# numerical derivatives
def NDeriv(idx, xvals):
    deriv = 0
    # see if we are at the front of the list
    if idx == 0:
        if ( idx == 0 and len(xvals) > 2):
            deriv = -3/2*xvals[0] + 2*xvals[1] - 1/2*xvals[2]
        elif ( idx == 0 and len(xvals) > 1 ):
            deriv = -1*xvals(0) + 1*xvals(1)
        else:
            #only one point in xvals -- so no deriv can be calculated
            deriv = 0
    # see if we are at the end of the list
    elif idx == len(xvals) and len(xvals == 2):
        deriv = -1* xvals[idx-1] + 1* xvals[idx]
    elif idx == len(xvals) and len(xvals) > 2:
        deriv = 1/2*xvals[idx-2] -2*xvals[idx-1] + 3/2*xvals[idx]
    elif len(xvals) >= 5:   # try five-point stencil
        deriv = 1/12*xvals[idx - 2] - 2/3*xvals[idx-1]
        + 2/3*xvals[idx+1] - 1/12*xvals[idx + 2]
    else:   # middle point of a list with three vals
        deriv = -1/2*xvals[idx-1] + 1/2*xvals[idx+1]


    # valid for first derivative only
    deriv /= abs(xvals[0] - xvals[1])       # this doesn't actually work
    return deriv

def TwoPtDeriv( y1, y2, dx):
    return (y2-y1)/dx

# INTELLIGENT SAMPLING
    # 1. divide integration domain into k regions
    # 2. select n_k num points for MC technique in eac h region
    # 3. apply monte carlo integration to each of the regions
def betterInt( a, b, func, n ):
    # define parameters
    threshold = 0.5
    epsilon = 0.08

    xValues = []
    divisionFinished = False
    xValues.append(a)              # xValues[0] = a
    xValues.append(a + epsilon)    # xValues[1] = a + epsilon
    
    i = 1
    while not divisionFinished:
        d1 = TwoPtDeriv(func(xValues[i-1]), func(xValues[i-1] + epsilon), epsilon)
        d2 = TwoPtDeriv(func(xValues[i]),  func(xValues[i] + epsilon), epsilon)
        if ( abs(d2 - d1) <= threshold):
            xValues.append(xValues[i])
            i += 1
            xValues[i] = xValues[i-1]+ epsilon
        else:
            xValues[i] += epsilon
        if xValues[i] >= b - epsilon:
            divisionFinished = True
        
    xValues.append(b)
    
    out = 0
    for i in range(0, len(xValues)-1):
        out += integrate(xValues[i], xValues[i+1], func, n)
        
    return out

print ("Computational Physics: Midterm Assignment")
print("\t Sarah Roberts")

#n = 100
x1 = -5
x2 = 5
y1 = f(x1)
y2 = f(x2)

# logical for development, if .true. then time-intensive code does not run
saveTime = False
# logical for development, if .true. extra code does run
debug = False

errors = []
nvals = []

true = F(1)-F(-1)
print("int(f(x) from -1 to 1 is ", true)
val = integrate(-1, 1, f, 100)
nvals.append(100)
errors.append(abs(true-val)/true*100)
print("estimate for n = 100 is ", val )
print("\t error is", abs(true-val)/true*100 , "%")


val = integrate(-1,1, f, 1000)
nvals.append(1000)
errors.append(abs(true-val)/true*100)
print("estimate for n = 1 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")

val = integrate(-1,1, f, 10000)
nvals.append(10000)
errors.append(abs(true-val)/true*100)
print("estimate for n = 10 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")

val = integrate(-1,1, f, 100000)
nvals.append(100000)
errors.append(abs(true-val)/true*100)
print("estimate for n = 100 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")


for i in range(0, len(errors)):
    errors[i] = abs(errors[i])
plt.subplot(2,1,1)
plt.plot(nvals, errors)
plt.xscale('log')
plt.show()


if debug == True:
    val1 = integrate(-1, 1, f, 1000000)
    print("1st estimate for n = 1 000 000 is ",  val1)
    print("\t error is", abs(true-val1)/true*100, "%")
    val2 = integrate(-1, 1, f, 1000000)
    print("2nd estimate for n = 1 000 000 is ",  val2)
    print("\t error is", abs(true-val2)/true*100, "%")
    val3 = integrate(-1, 1, f, 1000000)
    print("3rd estimate for n = 1 000 000 is ",  val3)
    print("\t error is", abs(true-val3)/true*100, "%")
    print()
    val = (val1+val2+val3)/3
    print("avg of 3 estimates for n = 1 mil is ", val)
    print("\t error is", abs(true-val)/true*100, "%")


print()
print()
true = F(4)-F(-2)
print("int(f(x) from -2 to 4 is ", true)
val = integrate(-2, 4, f, 100)
print("estimate for n = 100 is ", val )
print("\t error is", abs(true-val)/true*100, "%")
val = integrate(-2, 4, f, 1000)
print("estimate for n = 1 000 is ", val )
print("\t error is", abs(true-val)/true*100, "%")
val = integrate(-2, 4, f, 10000)
print("estimate for n = 10 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")
val = integrate(-2, 4, f, 1000000)
print("estimate for n = 100 000 is ", val)
print("\t error is", abs(true-val)/true*100, "%")




print()
print("Improvement: divide the domain into regions where the function ")
print("has less variance.  Integrate over these regions so that fewer ")
print("samples are needed, improving the speed of the calculation.  This")
print("method also lends itself well to parallelization, where division ")
print("of the domain could be run on seperate threads.  This is not ")
print("implemented here, because the overhead of creating threads in python")
print("would not be a good trade-off for the simple functions and small ")
print("regions defined in this driver program.")
print()


# first implement MC over the domain with a fixed number of intervals
k = 3
xa = -2
xb = 4
n = 10000
vals = []
step = (xb - xa) / k
thisA = xa
thisB = 0
for i in range(0, k) :
    thisB = thisA + step
    print("i = ", i)
    print("a = ", thisA )
    print("b = ", thisB)
    vals.append(integrate(thisA, thisB, g, n))
    print("int = ", vals[i])
    thisA = thisA + step
fixedStep = 0.0
for i in range(0, len(vals)):
    fixedStep = fixedStep + vals[i]
    
    
print()  
true = G(xb)-G(xa)
print("analytic int of g from", xa, " to ", xb, " is ", true ) 
res =   integrate(xa, xb, g, n*k)
print("MC w/o steps int of g from ", xa, " to ", xb, " is ", res )
print("\t error is", abs(true-res)/true*100, "%")

res = fixedStep
print("MC w/ fixed steps int of g from ", xa, " to ", xb, " is ", res )
print("\t error is", abs(true-res)/true*100, "%")

# this takes several minutes to run on my home computer, output is included below
#res =   integrate(xa, xb, g, 100000000)
#print("MC w/o steps int of g from ", xa, " to ", xb, " is ", res )
#print("\t error is", abs(true-res)/true*100, "%")

# MC w/o steps int of g from  -2  to  4  is  47.993325821624225
#         error is 0.013904538282849547 %

print()

res = betterInt(xa, xb, g, 50)
print("MC w/ adaptive steps int of g from ", xa, " to ", xb, " is ", res, "for n = 50")
print("\t error is", abs(true-res)/true*100, "%")

res = betterInt(xa, xb, g, 75)
print("MC w/ adaptive steps int of g from ", xa, " to ", xb, " is ", res, "for n = 75")
print("\t error is", abs(true-res)/true*100, "%")

res = betterInt(xa, xb, g, 100)
print("MC w/ adaptive steps int of g from ", xa, " to ", xb, " is ", res, "for n = 100")
print("\t error is", abs(true-res)/true*100, "%")

res = betterInt(xa, xb, g, 150)
print("MC w/ adaptive steps int of g from ", xa, " to ", xb, " is ", res, "for n = 150")
print("\t error is", abs(true-res)/true*100, "%")


print()
print()
print("End of program reached.")
print("Goodbye.")


















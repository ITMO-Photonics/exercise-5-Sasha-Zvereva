import numpy as np
import scipy.optimize as optimize

def f(x):
    return (x-3.)*(x*x+1.)
a=0.
b=7.
tolerance=1.e-3

if( f(a)*f(b)>0. ):
    print('Error: a and b should have opposite signs.')
else:
    while(0.5*(b-a) > tolerance):
        c = 0.5*(a+b)
        if( f(a)*f(c)<0. ):
            b=c
        else:
            a=c    
    print('result: ',0.5*(b+a))

x=np.linspace(0.,5.,100)

x_bisect = optimize.bisect (f, a, b)
print("bisect", x_bisect)
x_newton = optimize.newton (f, a)
print("newton", x_newton)
x_brentq = optimize.brentq (f, a, b)
print("brentq", x_brentq)


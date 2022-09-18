from math import *
def f(x):
    return x**3-4*x**2+1
def fprime(x):
    return 3*x**2-8*x
def newton(a,p):
    x=a
    n=0
    while abs(f(x))>=p:
        x=x-f(x)/fprime(x)
        n=n+1
    return x,n

print(newton(1,0.001))

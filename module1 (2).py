from math import *

def f(x):
    return(cos(x)-x)


def resol():
    x=0
    while f(x)>0:
        x=x+0.01
        print("x=",x,"  ","f(x)=",(cos(x)-x))

    return(x)


print(resol())

r=5.0235595626
print(r.__round__(2))

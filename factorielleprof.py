def Factorielle(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*Factorielle(n-1)

w=Factorielle(950)
print(w)

def factorielle2(t):
    f=1
    while t>0:
        f=f*t
        t-=1
    return f


z=factorielle2(950)
print(z)
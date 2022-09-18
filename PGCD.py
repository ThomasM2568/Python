def pgcd(a,b):
    n=c[0]
    d=c[1]
    r=a%b
    while r!=0:
            n=d
            d=r
            r=n%d
    return(d)

a=int(input())
b=int(input())
c=(a,b)
print(pgcd(a,b))
'''
#Ca ne marche pas
def pgcd_2(a,b):
    n,d,r=(c[0],[0],a%b)
    while r!=0:
        n,d,r=(d,r,n%d)
        return(d)

print(pgcd_2(a,b))
'''
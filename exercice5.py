compteur=0
def multi(x,n):
    global compteur
    compteur+=1

    if n==0:
        return 1
    elif n%2==0:
       valeur=pow(x**2,n/2)
       return valeur
    else:
        valeur=x*pow(x**2,((n-1)/2))
        return valeur

for o in range(9):
    print(multi(2,o))


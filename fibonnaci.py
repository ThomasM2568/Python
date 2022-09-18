def fibonnaci(n):
    global c
    c+=1
    if n==1 or n==2:
        return(1)
    return fibonnaci(n-1)+fibonnaci(n-2)

c=0
for i in range(6,11):
    print("fibonnaci de ",i,"->",fibonnaci(i))
    print("Compteur = ",c)


def fibonnaci_recursive(n,d):
    if n<3:
        return(1)
    if n in d:
        return(d.get(n))
    valeur_retournee = fibonnaci_recursive(n-1,d)+fibonnaci_recursive(n-2,d)
    d[n]=valeur_retournee
    return(valeur_retournee)

def fibonnaci2(n):
    dico_fibo={}
    return(fibonnaci_recursive(n,dico_fibo))


d={1:1,2:1}
print(fibonnaci_recursive(6,d))


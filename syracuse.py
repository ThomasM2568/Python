L=[]

def syracuse(n):
    if n==1 or n==1.0:
        return L
    else:

        if n%2==0:
            value=n/2
            L.append(value)
            syracuse(value)
        else:
            value=3*n+1
            L.append(value)
            syracuse(value)
        return L

t=int(input("Entrez la valeur de départ"))
print(syracuse(t))
print("Valeur de départ :"+str(t))


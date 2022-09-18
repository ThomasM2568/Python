
def limitant(a,b,nAi,nBi):
    x=0
    nA=nAi-a*x
    nB=nBi-b*x
    while nA>0 and nB>0:
        x+=0.1
    if valeurnA>0:
        print("A est limitant")
    elif valeurnB>0 and valeurnA>0:
        print("A et B sont limitants")
    else:
        print("B est limitant")
    return(nA,nB)


v1=float(input("Entrez le coefficient de a"))
v2=float(input("Entrez le coefficient de b"))
v3=float(input("Entrez la Quantité de matière de nAi"))
v4=float(input("Entrez la quantité de matière de nBi"))

print(limitant(v1,v2,v3,v4))

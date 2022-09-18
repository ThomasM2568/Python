a=float(input("Entrez le premier coefficient"))
b=float(input("Entrez le deuxième coefficient"))
nAi=float(input("Entrez la valeur en mol"))
nBi=float(input("Entrez la valeur en mol"))
x=0
nA=nAi-a*x
nB=nBi-b*x
while nA>0 or nB>0:
    x+=0.1

if nA==0:
        print("A est limitant")
elif nA==0 and nB==0:
        print("A et B sont dans les mêmes proportions")
elif nB==0:
        print("B est limitant")






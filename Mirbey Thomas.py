def equilateral(a,b,c):
    if a==b==c:
        return(1)
    elif a>100 or b>100 or c>100:
        return(2)
    else:
        return(0)


c1=float(input("Entrez la longueur du premier côté"))
c2=float(input("Entrez la longueur du second côté"))
c3=float(input("Entrez la longueur du troisième côté"))
print(equilateral(c1,c2,c3))

if equilateral(c1,c2,c3)==1:
    print("Le Triangle est équilatéral")
elif equilateral(c1,c2,c3)==2:
    print("Le triangle est trop grand!")
else:
    print("Le Triangle n'est pas équilatéral")
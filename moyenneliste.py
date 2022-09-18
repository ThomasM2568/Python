L1=[]
L2=[]
L3=[]
boucle1=int(input("Entrez le nombre de valeurs de la liste 1"))
boucle2=int(input("Entrez le nombre de valeurs de la liste 2"))

for notes in range(boucle1):

    L1.append(float(input("Entrez une valeur pour la liste L1.")))

for effectif in range(boucle2):

    L2.append(int(input("Entrez une valeur pour la liste L2.")))




for elem in L1 :
    elem_int=float(elem)
    L3+=[elem_int*float(x) for x in L2]
total=0
for y in L3 :
    total+=float(y)
moyenne=total/len(L3)

print("La moyenne de la liste L1 et L2 :",moyenne)
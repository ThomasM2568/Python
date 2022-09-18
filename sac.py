L=[[1,1,5,0],[2,2,3,0],[3,4,7,0],[4,5,4,0],[5,7,9,0],[6,8,14,0],[7,10,12,0]]

#Calcul de l'efficacité : valeur/masse, ce qui revient au prix au kg
for i in range(len(L)) :
    L[i][3]=L[i][2]/L[i][1]

#Tri croissant selon l'efficacité
n=len(L)
for i in range(1,n) :
    j=i-1
    while j!=-1 and L[j][3]>L[j+1][3] :
        temp=L[j]
        L[j]=L[j+1]
        L[j+1]=temp
        j=j-1

print(L)

#Remplissage du sac
masse_max=int(input("masse max du sac"))
valeur=0
masse=0

sac=[]
i=len(L)-1
while masse_max>0 and i>=0:
    if masse_max >= L[i][1] :
        masse_max -= L[i][1]
        masse += L[i][1]
        valeur += L[i][2]
        sac.append(L[i][0])
    i-=1

#Affichage de la solution trouvée
print(sac,"valeur totale :",valeur,"masse totale :",masse)

Liste=[4,3,6,5,9]
n=len(Liste)

def t(liste):

    for i in range(0,n-2):
        minimum=liste[i]
        posminimum=i

        for j in range(i+1,n-1):


            if Liste[j]<liste[posminimum]:
                posminimum=j
                minimum=liste[j]

        Liste[posminimum]=liste[i]
        Liste[i]=minimum

    print(Liste)
print(t(Liste))
print("compteur",compteur)

"---"

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]

tri_selection(tab)

print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("%d" %tab[i])

"---"

# Programme Python pour l'implémentation du tri par insertion
def tri_insertion(tab):
    # Parcour de 1 à la taille du tab
    for i in range(1, len(tab)):
        k = tab[i]
        j = i-1
        while j >= 0 and k < tab[j] :
                tab[j + 1] = tab[j]
                j -= 1
        tab[j + 1] = k
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
tri_insertion(tab)
print ("Le tableau trié est:")
for i in range(len(tab)):
    print ("% d" % tab[i])
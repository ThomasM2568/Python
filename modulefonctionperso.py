#Importation des librairies
#---------------------------
from collections import deque
#---------------------------
#Création des fonctions
#---------------------------
def Creer_file_vide():
     """0 argument attendu
     -------------
      """
     F=deque("")
     return F
#---------------------------
def Créer_une_pile(M):
     """1 argument attendu
     -------------
     Permet de créer une pile vide
      """
     global maxi
     liste=[]
     return liste
#---------------------------
def Est_vide(P):
     """1 liste attendue
     -------------
     Permet de vérifier si une pile est vide
      """

     if len(P)==0:
         return True
     else:
         return False
#---------------------------
def Est_pleine(P):

        """1 liste attendue
     -------------
     Permet de vérifier si une pile est pleine
      """
        if len(P)==maxi:
            return True
        else:
            return False
#---------------------------
def Empiler(P, d):
     """2 arguments attendus
     -------------
     Permet d'ajouter une valeur d à une liste P
      """
     if Est_pleine(P)==True:
        print('Impossible')
        return(P)
     else:
        P.append(d)
        print("la valeur a été rajoutée")
        return P
#---------------------------
def Depiler(P):
      """1 argument attendu
     -------------
     Permet de retirer la dernière valeur de la liste
      """
      if Est_vide(P)==True:
        print("Impossible ")
        return P
      else:
        P.pop()
        print("C'est Fait")
        return P
#---------------------------
acide="AGWPSGGASAGLAILWGASAIMPGALW"
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
h={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
def Compteur(acide):
    """1 argument attendu
     -------------
     Permet de compter le nombre d'apparition d'une lettre dans acide
      """
    for i in acide:
        for j in alp:
            if j==i:
                h[i]+=1
    for a in alp:
        if h[a]==0:
            h.pop(a)
    return(h)

#--------------------------

def tri_insertion(test):
     """1 argument attendu
     -------------
     Permet de trier les valeurs d'une liste donnée en argument dans l'ordre croissant
     Avec la méthode de tri par insertion
      """
    # Parcour de 1 à la taille du tab
     for i in range(1, len(test)):
        k = test[i]
        j = i-1
        while j >= 0 and k < test[j] :
                test[j + 1] = test[j]
                j -= 1
        test[j + 1] = k

     print ("Le tableau trié est:")
     for i in range(len(test)):
        print ("% d" % test[i])

#--------------------------
def tri_selection(tab):
    """1 argument attendu
     -------------
     Permet de trier les valeurs d'une liste donnée en argument dans l'ordre croissant
     Avec la méthode de tri par selection
      """
    for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j

       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
       print ("Le tableau trié est:")
       for i in range(len(tab)):
        print ("% d" % tab[i])
    return tab


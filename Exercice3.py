#Définition des fonctions
def Créer_une_pile(M):
    global maxi
    liste=[]
    return liste
#---------------------------
def Est_vide(P):
    if len(P)==0:
        return True
    else:
        return False
#---------------------------
def Est_pleine(P):
    if len(P)==maxi:
        return True
    else:
        return False
#---------------------------
def Empiler(P, d):
    if Est_pleine(P)==True:
        print('Impossible')
        return(P)
    else:
        P.append(d)
        print("la valeur a été rajoutée")
        return P
#---------------------------
def Depiler(P):
    if Est_vide(P)==True:
        print("Impossible ")
        return P
    else:
        P.pop()
        print("C'est Fait")
        return P
#---------------------------
#Execution du programme

maxi=int(input("Entrez une valeur maximale pour la longueur de la liste"))
Valeur=int(input("Entrez une valeur"))
T=[12,12,547,78,45,78]
print(Est_pleine(T))
print(Est_vide(T))
print(Empiler(T,Valeur))
print(Depiler(T))




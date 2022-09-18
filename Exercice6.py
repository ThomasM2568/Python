
global a
a=1
#---------------------------
def creer_file():
    file=[]
    return(file)
attente=creer_file()
#---------------------------
def clients_presents(nombre,liste):
        for i in range(1,nombre+1):
            client="Client"+str(i)
            liste.append(client)
        return liste
#---------------------------


def rajouter(liste):
    if a!=2:
        c='Client'+str(len(liste)+1)
        liste.append(c)
        print("Client ajouté")
        return liste
    else:
        print("Aucun client ne peut se joindre à la file")
#---------------------------
def retirer(liste):
    del liste[0]
    print("Client retiré")
    return liste
#---------------------------
def pleine(liste):
    global a
    if len(liste)==max:
        a+=1
        print(a)
#---------------------------

def vide(liste):
    global a
    if len(liste)!=2:
        a-=1

#---------------------------
nombre_client=int(input("Entrez le nombre de clients déjà présents"))
print(clients_presents(nombre_client,attente))
print(rajouter(attente))
print(retirer(attente))
print(pleine(attente))
print(vide(attente))
max=int(input("Entrez le nombre maximum de clients autorisés"))










import os.path
# Vérifier si le fichier existe ou non
if os.path.isfile('F:\LYCéE\1ere\nsi\annuaire.txt'):
    print("Fichier trouvé")
    fichier = open('annuaire.txt','r',encoding='utf-8')
    fichier.close()
else:
    print("Fichier non trouvé")
    fichier = open('annuaire.txt','x',encoding='utf-8')
    fichier.close()

annuaire={}


def chargement():
    global annuaire
    fichier4=open('annuaire.txt','r',encoding='utf-8')
    info=fichier4.readlines()
    fichier.close()
    for l in range(len(info)):
        infoa=info[l][0:-1]
        infob=infoa.split(';')
        annuaire[infob[0]]=infob[1]
    print(annuaire)

def ajouter(identite,numero):
    annuaire[identite]=numero
    return(annuaire)

def numero(identite):
    for key in annuaire:
        if key==identite:
            print ("Le numéro de ",id," est ",annuaire.get(key))
        else:
            print('error')

def recherche_par_nom(nom):
    for test in annuaire:
        if nom in test:
            print(test," a également le même nom, voici son numéro : ",annuaire.get(test))
        else:
            print("Personne n'a le même nom de famille")

def suppression(identite) :

    if identite in annuaire :

        del annuaire[identite]
    else:
        print("La personne n'est pas présente dans l'annuaire")

def sauvegarde():
    fichier2 = open("annuaire.txt", "w")
    for x in annuaire:
        texte=x+' ; '+annuaire.get(x)+'\n'
        fichier2.write(texte)

        fichier3 = open("annuaire.txt", "r")
        print(fichier3.read())
    fichier2.close()


t=''

while t!='stop':
    print(chargement())

    choix=int(input("Entrez un numéro , 1=Ajouter , 2=Recherche par Numero, 3=Recherche par nom, 4=Suppression"))
    if choix in (1,2,3,4):
        if choix==1:
            prenom=str(input("Entrez votre prenom"))
            nom=str(input("Entrez votre nom"))
            num=str(input("Entrez votre numéro"))
            id=nom+' '+prenom
            print(ajouter(id,num))
        elif choix==2:
            prenom=str(input("Entrez votre prenom"))
            nom=str(input("Entrez votre nom"))
            id=nom+' '+prenom
            print(numero(id))
        elif choix==3:
            prenom=str(input("Entrez votre prenom"))
            nom=str(input("Entrez votre nom"))
            id=nom+' '+prenom
            print(recherche_par_nom(id))
        else:
                prenom=str(input("Entrez votre prenom"))
                nom=str(input("Entrez votre nom"))
                id=nom+' '+prenom
                print(suppression(id))
    else:
        print("Merci d'entrer un choix de fonction valide")
    print(sauvegarde())
    t=str(input('Entrez stop si vous voulez arrêter'))
    print(annuaire)

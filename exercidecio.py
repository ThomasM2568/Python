
fichier = open('annuaire.txt','x',encoding='utf-8')
fichier.close()
annuaire={}


def chargement():
    fichier4 = open("annuaire.txt", "r")
    for x in fichier4:
        x.chain[0:-1]
        x.chain.spmit(';')
        annuaire.update(x)
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

def suppression(identite):
    if identite in annuaire:
        del annuaire[identite]
        print(identite," retiré avec succès, voici l'annuaire :",annuaire)
    else:
        print("Cette personne n'est pas dans l'annuaire")

def sauvegarde():
    fichier2 = open("annuaire.txt", "w")
    for x in annuaire:
        texte=x+' ; '+annuaire.get(x)+'\n'
        fichier2.write(texte)

        fichier3 = open("annuaire.txt", "r")
        print(fichier3.read())

    fichier2.close()
    fichier3.close()

t=''
while t!='stop':
    choix=int(input("Entrez un numéro , 1=Ajouter , 2=Recherche par Numero, 3=Recherche par nom, 4=Suppression"))
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
    t=str(input('Entrez stop si vous voulez arrêter'))

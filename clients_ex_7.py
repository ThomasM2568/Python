liste_client=[ {'Nom' : 'Dupont', 'Prénom' : 'Thomas' , 'Anniversaire' : '15-12'},
{'Nom' : 'Durand', 'Prénom' : 'Marie' , 'Anniversaire' : '23-07'},
{'Nom' : 'Durand', 'Prénom' : 'Georges' , 'Anniversaire' : '15-12'},
{'Nom' : 'Martin', 'Prénom' : 'Francine' , 'Anniversaire' : '20-03'},
{'Nom' : 'Lefebvre', 'Prénom' : 'Thomas' , 'Anniversaire' : '11-10'},
{'Nom' : 'Leroy', 'Prénom' : 'Juliette' , 'Anniversaire' : '20-03'},
{'Nom' : 'Hassani', 'Prénom' : 'Karim' , 'Anniversaire' : '15-02'},
{'Nom' : 'Fournier', 'Prénom' : 'Muriel' , 'Anniversaire' : '27-09'},
{'Nom' : 'Morel', 'Prénom' : 'Marcel' , 'Anniversaire' : '12-04'},
{'Nom' : 'Brunet', 'Prénom' : 'Georges' , 'Anniversaire' : '31-05'},
{'Nom' : 'Wang', 'Prénom' : 'Lilyn' , 'Anniversaire' : '20-03'},
{'Nom' : 'Leroy', 'Prénom' : 'Noëlle' , 'Anniversaire' : '13-06'}]

def affichage_client(liste_client):
    return liste_client

clients=affichage_client(liste_client)


def nouveau_client(nom,prenom,date):
    n_client={'Nom' : n_nom, 'Prénom' : n_prenom, 'Anniversaire' : n_date}
    liste_client.append(n_client)
    return liste_client



n_nom=str(input("Entrez votre nom"))
n_prenom=str(input("Entrez votre prénom"))
n_date=str(input("Entrez une date de naissance écrit comme ceci JJ-MM"))

print(nouveau_client(n_nom,n_prenom,n_date))


def client_anniversaire(date_naissance):

    for longueur_liste in range(len(liste_client)-1):
        if liste_client[longueur_liste]==date_naissance:
            print("Cette date correspond à ",liste_client['Prénom']," ",liste_client['Nom'],", vous avez rentré la date de naissance suivante :",date_anniversaire)
        else:
            print("Cette date de naissance ne correspond à personne")






def supprimer_client(nom,prenom):
    test={'Nom' : nom ,'Prénom' : prenom}
    for longueur_liste_2 in range(len(liste_client)-1):
        if test['Nom']==liste_client[longueur_liste_2]['Nom'] and test['Prénom']==liste_client[longueur_liste_2]['Prénom'] :
            del liste_client[longueur_liste_2]
            print("Client retiré avec succès")
            print(liste_client)
            break
        elif test['Nom']!=liste_client[longueur_liste_2]['Nom'] and test['Prénom']!=liste_client[longueur_liste_2]['Prénom'] :
            print("Une des informations n'est pas juste ou la personne n'est pas un client")
            print(liste_client)



nom_2=str(input("Entrez un nom à retirer"))
prenom_2=str(input("Entrez un prénom à retirer"))

print(client_anniversaire('12-04'))
supprimer_client(nom_2,prenom_2)

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

#client=liste_client[0]
#print(client['Nom'])

#for client in liste_client:
#    print(client['Nom'])


def clients_anniversaire(datenaissance):
    #print(datenaissance)
    trouve=False
    for client in liste_client:
        #print(client['Anniversaire'])
        if datenaissance == client['Anniversaire']:
            print (client['Nom'])
            trouve=True

    if trouve == False:
        print("*** date non trouvee")
    


def nouveau_client(nom,prenom,date,liste):
    nouveauclient={'Nom':nom,'Prénom':prenom,'Anniversaire':date}
    liste_client.append(nouveauclient)
    return liste

def supprimer_client(nom,prenom):
    n=0
    trouve=False
    for client in liste_client:
        
        if nom==client['Nom'] and prenom==client['Prénom']:
            del liste_client[n]
            trouve=False
            break
        
        n=n+1
    if trouve == False:
        print("*** client non trouve")



print (liste_client)
print (len(liste_client))
utilisateur_nom=str(input("Entrez un nom : ")) 
utilisateur_prenom=str(input("Entrez un prénom : "))

print(supprimer_client(utilisateur_nom,utilisateur_prenom))
print (liste_client)
print (len(liste_client))
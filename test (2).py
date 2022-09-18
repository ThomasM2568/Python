from Lib/colletions/__init___.py import *
Clients=[ {'Nom' : 'Dupont', 'Prénom' : 'Thomas' , 'Anniversaire' : '15-12'},
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

nom='Dupont'
prenom='Thomas'
date='15-12'
test=OrderedDict.fromkeys()
test.move_to_end

print(test)
for longueur_liste_2 in range(len(Clients)-1):
    if test==Clients[longueur_liste_2]:
        print("Yes")
    else:
        print("Pas yes")
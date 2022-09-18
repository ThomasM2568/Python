import jeu_batons as j
Partie=j.Jeu()
Partie.__init__()
nombre_batons=int(input("Entrez le nombre de bâtons à mettre dans le jeu"))
Partie.__partie_init__(nombre_batons)

while Partie.__get_nombre_bâtons__()>0:
    retirer=int(input("Entrez le nombre de bâton à retirer, ce nombre doit être entre 1 et 3"))
    if 1<nombre<3:
        Partie.__jouer__(retirer)
    else:
        retirer=int(input("Entrez le nombre de bâton à retirer, ce nombre doit être entre 1 et 3"))
        Partie.__jouer__(retirer)


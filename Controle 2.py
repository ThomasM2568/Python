n1=int(input("Joueur 1, entrez le nombre à trouver"))
tentatives=int(input("Entrez le nombre de tentatives maximum"))
n2=int(input("Joueur 2, entrez un nombre"))

compteur=0
tentatives-=1


while tentatives!=compteur or n1!=n2:
    if n1!=n2:
        if n2>n1:
            print("Trop grand")
            compteur+=1
            n2=int(input("Entrez un autre nombre"))
        elif n2<n1:
            print("Trop petit")
            compteur+=1
            n2=int(input("Entrez un autre nombre"))
    if n1==n2:
        print("Gagné en ",compteur+1," tentatives")
        break

    elif compteur==tentatives:
        print("Perdu, limité à ",tentatives+1,"tentatives")
        break

















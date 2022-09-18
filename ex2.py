class Pile:
    def __init__(self,m):
        self.__maxlen=m
        self.valeurs =[]
        self.__nombre_donnees=0
        Pile.__voir__(self)

    def __empiler__(self,valeur):
        if self.__maxlen>self.__nombre_donnees:
            self.valeurs.append(valeur)
            self.__nombre_donnees+=1
            return("Element rajouté la pile avec succès !")
        else:
            return("Impossible d'ajouter dans la pile car celle-ci est pleine !")
    def __depiler__(self):
        if self.__nombre_donnees!=0:
            self.valeurs.pop()
            self.__nombre_donnee-=1
            return("Le dernier élement de la pile a été dépilé avec succès !")
        else:
            return("Impossible de retirer le dernier élement car la pile est vide !")

    def __voir__(self):
        for i in range(len(self.valeurs)):
            print("|"+str(self.valeurs[i])+"|")
        return(self.valeurs)

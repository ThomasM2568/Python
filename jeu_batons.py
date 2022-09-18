from random import randint
class Jeu:
    """Classe qui permet de jouer
    au jeu du bâton
     -------------
    """
    def __init__(self):
        """Permet de lancer le jeu
        -------------
        """
        print('Jeu initialisé')

    def __partie_init__(self,__nombre_baton):
        """Le nombre de baton pour le jeu
        est demandé en argument et va permettre
        de remplir le jeu
        -------------
        """
        self.__baton=[]
        for i in range(__nombre_baton):
            self.__baton.append(1)
        print(self.__baton)
        self.__joue=randint(1,2)
        return("Le joueur "+str(self.__joue)+" commence")

    def __jouer__(self,nombre):
        """Un nombre de bâtons à retirer
        est attendu, on retire ce nombre
        au nombre de bâtons
        -------------
        """
        if len(self.__baton)==0:
            return("False")
        else:
            self.player=self.__joue
            for e in range(nombre):
                self.__baton.pop()
            if self.player==1:
                self.player+=1
            else:
                self.player-=1
        print("True")
        return(self.__baton)

    def __get_nombre_bâtons__(self):
        """permet de récuperer le nombre
        de bâtons du jeu
        -------------
        """
        return(len(self.__baton))

    def __get_joueur__(self):
        """permet de récuperer le nombre
        qui correspond au joueur qui doit jouer
        -------------
        """
        return(self.player)



class Robot:
    def __init__(self,position_initiale):
        self.__position=position_initiale
        print('Objet robot initialisé')
        self.__sous_tension__=False

    def __etat__(self):
        return(self.__sous_tension__)

    def __get_position__(self):
        return(self.__position)

    def __del__(self):
        print("Objet détruit")

    def __message__():
        print("Objet Robot initialisé")

    def __interrupteur__(self):
        if self.__sous_tension__==False:
            self.__sous_tension__=True
        else:
            self.__sous_tension__=False

    def __translation__(self,deplacement):
        if self.__sous_tension__==True:
            if self.__position<=10 and self.__position>=0:
                self.__position+=deplacement

            else:
                print("La position initiale n'est pas entre 0 et 10")
        else:
            print("Allumez déjà le robot avec la fonction interrupteur")





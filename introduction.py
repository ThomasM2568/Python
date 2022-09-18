class Robot:
    def __init__(self,position_initiale):

        self.__position=position_initiale
        print("Objet robot initialisé")

        def get_position(self):
            return(self.__position)

        def deplacer_robot(self,nouvelle_position):
            if 0<=nouvelle_position<=10:
                self.__position=nouvelle_position



robot1=Robot(5)
robot1.get_position()

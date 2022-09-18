from math import *
class vecteur:
    def init(self,x=0,y=0):
        self.__valeurx__=x
        self.__valeury__=y

        print( "vecteur créé")

    def norme(self,__valeurx__,__valeury__):
        self.__normev__=sqrt(__valeurx__**2 + __valeury__**2)
        return self.__normev__
    def somme(vecteur1x,vecteur1y,vecteur2x,vecteur2y):
        vecteur3x=vecteur2x+vecteur1x
        vecteur3y=vecteur2y+vecteur2y
        return vecteur3x,vecteur3y
    def difference(vecteur1x,vecteur1y,vecteur2x,vecteur2y):
        vecteur3x=vecteur1x-vecteur2x
        vecteur3y=vecteur1y-vecteur2y
        return vecteur3x,vecteur3y
    def multiplication(vecteur,reel):
        result=vecteur*reel
        return result
    def egalite(vecteur):
        if self.norme(__valeurx__,__valeury__)==vecteur:
            return(True)
        else:
            return(False)
    def colineaires(vecteur):
        if vecteur>self.norme(__valeurx__,__valeury__):
            if vecteur%self.norme(__valeurx__,__valeury__)!=True:
                print("les vecteurs sont colinéaires")
            else:
                print("Les vecteurs ne sont pas colinéaires")

















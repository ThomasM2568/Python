# Créé par renaud.joffrin, le 12/10/2020 en Python 3.7
from math import sqrt
class vecteur:
    def __init__(self,x=0,y=0):
        self.valeurx=x
        self.valeury=y


    def norme(self):
        norme=sqrt(self.valeurx**2+self.valeury**2)
        return(norme)


    def somme(self,vecteur1,vecteur2):
        self.valeurx=vecteur2.valeurx+vecteur1.valeurx
        self.valeury=vecteur2.valeury+vecteur1.valeury
        print(self.valeurx,self.valeury)

    def différence(self,vecteur1,vecteur2):
        self.valeurx=vecteur1.valeurx-vecteur2.valeurx
        self.valeury=vecteur1.valeury-vecteur2.valeury
        print(self.valeurx,self.valeury)

    def multiplication(self,fois):
        self.valeurx=self.valeurx*fois
        self.valeury=self.valeury*fois
        print(self.valeurx,self.valeury)


    def egalite(self,vecteur):
        if self.valeurx==vecteur.valeurx and self.valeury==vecteur.valeury:
            print("True")
        else:
            print("False")


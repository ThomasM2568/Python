class personne:
    def __init__(self,nom,prenom,adresse,numero):
        self.id=str(nom+" "+prenom)
        self.ad=str(adresse)
        self.num=str(numero)
        print (" Informations enregistrées")

    def __getinfo__(self):
        self.idfull=self.id+" "+self.ad+" "+self.num
        return(self.idfull)

class annuaire:
    def __init__(self,liste):
        self.an=liste
    def ajouter(self,identite):
        self.an.append(identite)
        return(self.an)
    def supprimer(self,identite):
        for i in range (len(self.an)):
            if identite == self.an[i]:
                del self.an[i]
                return("Personne supprimée de l'annuaire",self.an)
    def recherche(self,identite):
        for i in range (len(self.an)):
            if identite == self.an[i]:

                return(self.an[i])
        return("None")

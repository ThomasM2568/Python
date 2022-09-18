import doctest
def pourcentage(score,total):
    if type(score)!=int or type(score)!=float:
        return("Erreur de type sur score")
    if type(total)!=int or type(total)!=float:
        return("Erreur de type sur total")
    if score<0:
        return("Pas de valeurs négatives pour score")
    if total<=0:
        return('Pas de valeurs négatives ou nulles pour total')
    return(score/total)*100

doctest.testfile("tests_pourcentage.txt")



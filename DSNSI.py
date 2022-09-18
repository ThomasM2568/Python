import doctest as dt

def type_parametre(p):
    return(str(type(p)))

def presence_3_chiffres_min(mdp):
    chiffres=['0','1','2','3','4','5','6','7','8','9']
    nb=0
    for i in str(mdp):
        if i in chiffres:
            nb+=1
    if nb>=3:
        return(True)
    return(False)

def presence_maj(mdp):
    nb=0
    for i in mdp:
        if i.upper()==i:
            nb+=1
    if nb>0:
        return(True)
    return(False)

def nb_caracteres_speciaux(mdp):
    c=['&','#','@']
    nb=0
    for i in mdp:
        if i in c:
            nb+=1
    return(nb)

def presence_8_caracteres(mdp):
    if len(mdp)>=8 :#0->8
        return(True)
    return(False)

dt.testfile("DSNSI.txt")
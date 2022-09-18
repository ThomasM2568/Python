def coeff (genre):
    switcher = {
        'f': 1.04,
        'h': 1.23,
    }
    return switcher.get(genre, 0 )

def coeff2 (genre):
    if genre == 'f':
        return (1.04)
    else:
        if genre == 'h':
            return(1.23)

def clairence (age, creatininemie, poids, k):
    clcr=((140-age)/creatininemie)*poids*k
    return clcr

def insuffisance(clcr):
    if ( clcr > 70) :
        return ("normal")
    else:
        return ("insuffisance")


clcr1=clairence(35,100,75,coeff2('h'))
etat=insuffisance(clcr1)
print("clairence {clcr} résultat {etat}".format(clcr=clcr1, etat=etat))


clcr2=clairence(25,120,60,coeff('f'))
etat=insuffisance(clcr2)
print("clairence {clcr} résultat {etat}".format(clcr=clcr2, etat=etat))



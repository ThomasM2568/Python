def chemin_reccursif(p,i,j,d):

    if (i,j) in d:
        return(d.get(i,j))

    if i==len(p)-1 :
        d[(i,j)]=p[i][j]
        return p[i][j]

    cg = chemin_reccursif(p,i+1,j,d)
    cd = chemin_reccursif(p,i+1,j+1,d)
    c=p[i][j]+max(cg,cd)
    return(c)

def chemin():
    dico={}
    return(chemin_reccursif())
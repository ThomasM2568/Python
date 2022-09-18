d={}

def pgcb_recursif(image,i,j,d):
    l=((i),(j),0)

    d[image]=l

    return d

def pgcb(image,x,y):
    dico_pixels={}
    return pgcb_recursif(image,x,y,dico_pixels)




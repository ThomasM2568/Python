def f (xa,ya,xb,yb,xc,yc):    #On définit f avec les valeurs xa,ya,xb,yb,xc,yc
    xu=xb-xa                   #On définit xu=xb-xa
    yu=yb-ya                    #On définit yu=yb-ya
    xv=xc-xa                    #On définit xv=xc-xa
    yv=yc-ya                    #On définit yv=yv-ya
    return(xu,yu,xv,yv)

xu,yu,xv,yv=f(1,2,4,6,10,14)          #On définit xu, yu, xv, yv qui prennent les valeurs de ceux de la fonction


def det (xu,yu,xv,yv):           #On définit det
     det=xu*yv-yu*xv
     return(det)

print("U a pour coordonnées :",xu, ";",yu," et V a pour coordonnées :",xv,";",yv)


if det(xu,yu,xv,yv) == 0:           #On définit que si le résultat de det avec les valeurs de xu, yu, xv, yv est égal à 0
    print("Les vecteurs sont colinéaires")    #Les vecteurs sont colinéaires
else:
    print("Les vecteurs ne sont pas colinéaires")    #Sinon les vecteurs ne sont pas colinéaires







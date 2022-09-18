def det (xa,ya,xb,yb,xc,yc):
    det=(xa*yb-ya*xb)-(xa*yc-ya*xc)
    return(det)

print(det(1,2,4,6,10,14))

if det == 0:
    print("Les vecteurs sont colinéaires")
else:
    print("Les vecteurs ne sont pas colinéaires")

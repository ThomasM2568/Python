from tkinter import *
def deci_héxa(q):
    result = ""
    while q != 0 :
        r=q%16
        q=q//16
        result=str(r)+result
    if q==0:
        result='0'+result
    elif r==10:
        result='a'+result
    elif r==11:
        result='b'+result
    elif r==12:
        result='c'+result
    elif r==13:
        result='d'+result
    elif r==14:
        result='e'+result
    elif r==15:
        result='f'+result
    elif r==16:
        result='10'+result


    return(result)

a=int(input("Entrez la première valeur"))
b=int(input("Entrez la seconde valeur"))
c=int(input("Entrez la troisième valeur"))

if len(deci_héxa(a))==1:
    a='0'+str(a)
if len(deci_héxa(b))==1:
    b='0'+str(b)
if len(deci_héxa(c))==1:
    c='0'+str(c)

couleur='#'+str(a)+str(b)+str(c)

fenêtre=Tk()
fenêtre.configure(bg=couleur)
fenêtre.mainloop()

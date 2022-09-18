texte1="A FORCE D'ALLER EN AVANT, IL PARVINT AU POINT OU LE BROUILLARD DE LA FUSILLADE DEVENAIT  TRANSPARENT. SI BIEN QUE LES TIRAILLEURS DE LA LIGNE RANGES ET A L'AFFUT DERRIERE LEUR LEVEE DE PAVES, ET LES TIRAILLEURS DE LA BANLIEUE MASSES A L'ANGLE DE LA RUE, SE MONTRERENT SOUDAINEMENT  QUELQUE CHOSE QUI REMUAIT DANS LA FUMEE. AU MOMENT OU GAVROCHE DEBARRASSAIT DE SES CARTOUCHES UN SERGENT GISANT PRES D'UNE BORNE, UNE BALLE FRAPPA LE CADAVRE."

texte2="IL LUI SUFFIT ALORS D'Y APPROFONDIR SON AGONISANT FRANGIN POUR VOIR S'ACCOMPLIR SON FORFAIT QUI, PAR SURCROIT, PROFITA AU PAYS, PUISQU'UN MOIS PLUS TARD, TOUT UN CHACUN S'ACCORDAIT POUR NANTIR L'INTRIGANT FLUX QUI SOURDAIT DU PUITS D'UN FORT POUVOIR CURATIF, SURTOUT ANTICATARRHAL, MAIS S'APPLIQUANT AUSSI A L'ALBUGO, A L'ANCHILOPS, AUX BUBONS, AUX CALCULS, AUX CHALAZIONS, AU TRISMUS, AU PITYRIASIS, AU MAL BLANC, AU PRURIGO, AU MAL CADUC, AU GLOSSANTHRAX."

texte3="JE RENTRE CHEZ MOI. SUR LE TROTTOIR, UN HOMME SE PROMENE, SES DEUX MUSETTES REMPLIES DE LEGUMES ENTRE SES DOIGTS. JE SUIS DERRIERE LUI ET BRUSQUEMENT IL SE RETOURNE ET ME HURLE BONJOUR ! IL ME VOIT, JE LE VOIS. UNE PETITE SECONDE JE CROIS QUE C'EST LE PERE D'UNE COPINE. OR, COMME IL M'EST INCONNU, JE LE CONTOURNE. JE CONTINUE MON CHEMIN JUSQUE CHEZ MOI."

lettre={'B':0, 'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

for i in texte1:
    
    if i=='A' and 'A' not in lettre:
        lettre['A']=1
    elif i=='A' and 'A' in lettre:
        lettre['A']+=1

        
    if i=='B':
        lettre['B']+=1
    if i=='C':
        lettre['C']+=1
    if i=='D':
        lettre['D']+=1
    if i=='E':
        lettre['E']+=1
    if i=='F':
        lettre['F']+=1
    if i=='G':
        lettre['G']+=1
    if i=='H':
        lettre['H']+=1
    if i=='I':
        lettre['I']+=1
    if i=='J':
        lettre['J']+=1
    if i=='K':
        lettre['K']+=1
    if i=='L':
        lettre['L']+=1
    if i=='M':
        lettre['M']+=1
    if i=='N':
        lettre['N']+=1
    if i=='O':
        lettre['O']+=1
    if i=='P':
        lettre['P']+=1
    if i=='Q':
        lettre['Q']+=1
    if i=='R':
        lettre['R']+=1
    if i=='S':
        lettre['S']+=1
    if i=='T':
        lettre['T']+=1
    if i=='U':
        lettre['U']+=1
    if i=='V':
        lettre['V']+=1
    if i=='W':
        lettre['W']+=1
    if i=='X':
        lettre['X']+=1
    if i=='Y':
        lettre['Y']+=1
    if i=='Z':
        lettre['Z']+=1
print(lettre)    
    
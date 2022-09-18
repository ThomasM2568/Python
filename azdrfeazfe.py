if decalage>0:
                for c in range(0,len(motif))[::-1]:
                    print(c,mot[c],motif[c])
                    if mot[c]==motif[c]:
                        N+=1
                    else:
                        if x==0:
                            x=c
                            l1=l[:c]
                            l2=l[c:]
                            print(l1)

                decalage=len(mot)
                mot=''
                for v in range(len(motif)):
                    mot=mot+chaine[v+decalage]
                print(mot,len(mot))

            elif decalage<0:
                decalage=1
                mot=''
                for v in range(len(motif)):
                    mot=mot+chaine[v+decalage]
                print(mot)

            else:
                print("le decalage est de",decalage)
                mot=''
                for v in range(len(motif)):
                    mot=mot+chaine[v+decalage]
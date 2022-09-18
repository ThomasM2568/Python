text="FJUURTGDJGJFGMSWULYSWENBBBQOXVRBSDDJNUGHAJPGX"
clef="TERMINALE"
new_clef=""

while len(new_clef) < len (text):
    print("ddd")
    new_clef+=clef
    print(new_clef)

new_clef+=clef

new_clef=new_clef[0:len(text)]

print (new_clef)
print (text)

textcrypte=""

def xor(mot1,mot2):
    mot1=ord(mot1)
    mot2=ord(mot2)
    mot1=format(mot1,'08b')
    mot2=format(mot2,'08b')
    v3=""
    for i in range(len(mot1)):
        v1=int(mot1[i])
        v2=int(mot2[i])
        v3+=str(v1^v2)
    return(v3)

w=""
for i in range(len(text)):
    w+=str(xor(text[i],new_clef[i]))
print(w)

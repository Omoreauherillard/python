"""#Exercice 1
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢','⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅','⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵']

def affichagebaille(texte):
    texte=texte.upper()
    texteBraille=''
    for c in range(0,len(texte)):
        if texte[c]>=' ' and texte[c]<='Z':
            texteBraille+=brailles[ord(texte[c])-32]
    return texteBraille




texte=str(input("votre texte ?"))
print(affichagebaille(texte))
"""
"""#Exercice 2
chaine="touchard"
total=''
for i in range(len(chaine)):
    total+=chaine[i]+'*'
print(total)
"""
"""#Exercice 3
chaine="zorglub"
total=''
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]+''

print(total)
"""
"""#Exercice 4
chaine=str(input("chaine"))
total=''
for i in range(len(chaine)-1,-1,-1):
    total+=chaine[i]+''

print(chaine,total)
if chaine==total:
    print("good")
"""
"""#Exercice 5
def codecesar(phrase,cle):
    total=''
    for i in range(0,len(phrase)):
        ascii=ord(phrase[i])
        conv=ascii-65+cle
        caract=chr(conv+65)
        total+=caract+''
    return total

cle=int(input("clef"))
phrase=str(input("phrase"))
print(codecesar(phrase,cle))
"""
#Exercice 6
from string import ascii_uppercase as ascUp
vigenereTable = [ascUp[i:]+ascUp[:i] for i in range(len(ascUp))]
for ligne in range(0,len(vigenereTable)):
    print (ligne, vigenereTable[ligne])


def vigénère(vigenereTable,mot,cle):
    lettrecle=[]
    clef=cle.upper()
    for i in clef:
        lettrecle.append(i)
    lettremot=[]
    MOT=mot.upper()
    for i in MOT:
        lettremot.append(i)
    print(lettremot)






mot='Oscar'
cle=str(input("clé ?"))
vigénère(vigenereTable,mot,cle)
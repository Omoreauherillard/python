"""#Exercice 1
phrase="bonjour"
print(phrase[1:4])
"""
"""
chaine = "NE PARLEZ PAS SI FORT !"
print(chaine.lower())
chaine="nsi"
chaine=chaine.upper()
print(chaine)
"""
"""
w = "Washington"
t= "Touchard"
lycee= w+" "+t
print (lycee)
print (len(lycee))
"""
"""
chaine = "Bonjour"
for i in range(0, len(chaine)):
    print(chaine[i], end = '')

chaine = "Au revoir"
for c in chaine:
    print(c, end = '')
"""
"""
chaine=str(input("votre chaine ?"))
if chaine=='bonjour':
    print('hello')
else:
    print('j\'ai rien compris')
"""
"""
s = "Welcome"
print(s[-1])
print(s[-2])
"""
"""
s = "Welcome"
print(s[:6])
print(s[4:])
print(s[1:-1])
"""
"""
s = "Hello computer"
print(s.endswith("uter"))
print(s.startswith("good"))
print(s.find("comp"))
print(s.rfind("o"))
print(s.count("o"))
"""
"""
chaine = "\r  Bien le bonjour\t \t"
s = chaine.strip()
print(s)
"""
"""
ch = 'A'
print(ord(ch))
"""
"""
valeur=66
print(chr(valeur))
"""
"""
chaine = "10.5"
print(type(chaine))
valeur=float(chaine)
print(type(valeur))
print(valeur)
"""
"""#Exercice 2
def caractere(lettre,chaine):
    total=chaine.count(lettre)
    return total

phrase="Je m'appelle Emmanuel Macron"
print(caractere("e",phrase))

def caractere(lettre,chaine):
    total=0
    for i in chaine:
        if lettre==i:
            total+=1
    return total

print(caractere("e","Je m'appelle Emmanuel Macron"))
"""
"""#Exercice 3
def premiermot(chaine):
    n=0
    while chaine[n]!=" ":
        print(chaine[n], end="")
        n+=1

chaine="Bonjour je suis Oscar"
premiermot(chaine)
"""
"""#Exercice 4
chaine="Un peu"
chaine1="Beaucoup"
chaine2="Passionnément"
print(chaine +"\r" + chaine1 +"\r"+ chaine2)
"""
"""#Exercice 5.1

def semaine(semaine):
    total=semaine[0]
    for i in range(len(semaine)):
        total+="\r"+semaine[i]
    print(total)

semaine2=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
semaine(semaine2)
"""
"""#Exercice 5.2
def semaine(semaine):
    total=semaine[0]
    for i in semaine:
        total+="\r"+i
    print(total)

semaine2=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
semaine(semaine2)
"""
#Exercice 6






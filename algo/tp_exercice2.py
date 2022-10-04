"""#Exercice 1
for n in range(1,16,1):
    print(n)
"""
"""#Exercice 2
for n in range(15,0,-1):
    print(n)
"""
"""#Exercice 3
a=int(input("un nombre"))
b=int(input("un autre nombre(plus grand)"))
for n in range(a,b+1,1):
    print(n)
"""
"""#Exercice 4
a=int(input("Nombre"))
for i in range(a+1,a+11,1):
    print(i)
"""
"""#Exercice 5
a=int(input("Nombre"))
for i in range(1,10,1):
    b=a*i
    print(b)
"""
"""#Exercice 6
a=float(input("Nombre positif"))
b=float(input("Nombre positif"))
c=float(input("Nombre positif"))
d=float(input("Nombre positif"))
e=float(input("Nombre positif"))
f=max(a,b,c,d,e)
print("le nombre le plus grand est",f)
"""
"""#Exercice 7
valeur=0
max=0
while valeur>=0:
    valeur=float(input("Nombre"))
    if valeur>max:
        max=valeur
print(max)
"""
"""#Exercice 8
valeur=0
somme=0
while valeur>=0:
    valeur=float(input("nombre"))
    if valeur>=0:
        somme=somme+valeur
print("Somme:",somme)
"""
"""#Exercice 9
menu=0
while menu!="q":
    print("1: charger le fichier")
    print("2: sauvegarder le fichier")
    print("3: afficher les données")
    print("4: modifier les données")
    print("q: quitter")
    menu=input("Votre choix :")
    if menu=="1":
        print("Chargement ...")
    elif menu=="2":
        print("Sauvegarde")
    elif menu=="3":
        print("Affichage")
    elif menu=="4":
        print("Modification")
    elif menu=="q":
        print("Au revoir")
    else:
        print("Erreur 603 ")
"""
"""#Exercice 10
from random import*
nombre=randint(1,20)
valeur=0
while valeur!=nombre:
    valeur=int(input("Votre prédiction :"))
    if valeur>nombre:
        print("Prédiction trop grande")
    elif valeur<nombre:
        print("Prédiction trop petite")
    else:
        print("Bravo, exact")
"""
"""#Exercice 11
from random import*
nombre=randint(1,20)
valeur=0
coup=1
while valeur!=nombre:
    valeur=int(input("Votre prédiction :"))
    if valeur>nombre:
        print("Prédiction trop grande")
        coup=coup+1
    elif valeur<nombre:
        print("Prédiction trop petite")
        coup=coup+1
    else:
        print("Bravo, exact, vous avez trouvé en",coup,"coups")
"""
"""#Exercice 12
from random import*
a="0"
while a!="N":
    nombre=randint(1,2)
    valeur=0
    coup=1
    while valeur!=nombre:
        valeur=int(input("Votre prédiction :"))
        if valeur>nombre:
            print("Prédiction trop grande")
            coup=coup+1
        elif valeur<nombre:
            print("Prédiction trop petite")
            coup=coup+1
        else:
            print("Bravo, exact, vous avez trouvé en",coup,"coups")
            while a!="O" and a!="N":
                a=input("Voulez-vous rejouer ?")
                if a=="N":
                    print("Bye")
"""
#Exercice 13
from math import*
xa=float(input("Absisse de a"))
ya=float(input("Ordonnée de a"))
xb=float(input("Absisse de b"))
yb=float(input("Ordonnée de b"))
AB=sqrt((xa-xb)**2+(ya-yb)**2)
print("Distance AB :",AB)
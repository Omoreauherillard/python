# Créé par osca.moreauherillard, le 04/10/2022 en Python 3.7
"""#Exercice 1
def text():
    print("bonjour")

text()
"""
"""#Exercice 2
def text(prenom):
    print("bonjour", prenom)

text("Gérard")
"""
"""#Exrecice 3
def somme(a,b):
    return a+b

print(somme(13,18))
"""
"""#Exercice 4
def surface(largeur,longueur):
    return largeur*longueur

print(surface(4,5))
"""
"""#Exercice 5
def calcul(x):
    y=2*x**2-4*x+3
    return y

print(calcul(20015464))
"""
"""#Exrecice 6
from math import*
def conversionangle(radians):
    a=degrees(radians)
    return a

print(conversionangle(3*pi/2))
"""
"""#Exercice 7
def table(operande,valmin,valmax):
    for i in range(valmin,valmax+1):
        a=operande*i
        print(operande,"*",i,"=",a)
table(6,0,10)
"""
"""#Exercice 8
def rectangle(largeur, longueur):
    for j in range(1,longueur+1):
        for i in range(1,largeur+1):
            print("*", end=" ")
        print(" ")

rectangle(20,40)
"""
"""#Exerice 9
def triangle(longueur):
    for j in range(1,longueur+1):
        for i in range(1,j+1):
            print("*", end="")
        print(" ")

triangle(32)
"""
#Exercice 10
from math import *
def volume(rayon):
    a=(4*pi)*(rayon**3)/3
    print(a)

volume(3)




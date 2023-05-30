import time
import random

N=20000

def creationValeurs(N):
    tableau=[]
    VALEUR_MAX=100000
    for indice in range(0,N):
        valeur=random.randint(1,VALEUR_MAX)
        while valeur in tableau:
            valeur = random.randint(1, VALEUR_MAX)
        tableau.append(valeur)
    return tableau

def triselection(tableau):
    for i in range(0,len(tableau)-1):
        indmini=i
        for j in range(i+1,len(tableau)):
            if tableau[j]<tableau[indmini]:
                indmini=j
        if tableau[i]!=tableau[indmini]:
            temp=tableau[i]
            tableau[i]=tableau[indmini]
            tableau[indmini]=temp
    return tableau


tableau=creationValeurs(N)
debut = time.time()
print(triselection(tableau))
fin = time.time()
a=fin-debut
print(a)
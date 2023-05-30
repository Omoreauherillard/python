from pylab import*
import csv
fichier=open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnees=[]
for ligne in lecture_fichier:
    liste_donnees.append(dict(ligne))
fichier.close()

def liste_key(liste_donnees,key,choix):
    x=[]
    y=[]
    for donnees in liste_donnees:
        x.append(float(donnees[key]))
        y.append(float(donnees[choix]))
    plot(x,y)
    show()

choix=str(input("Une donnée ?"))
liste_key(liste_donnees,"Altitude m",choix)
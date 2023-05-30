import csv
fichier=open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnees=[]
for ligne in lecture_fichier:
    liste_donnees.append(dict(ligne))
fichier.close()

for donnees in liste_donnees:
    print("Durée :", donnees['Durée'],"Altitude :", donnees['Altitude m'])

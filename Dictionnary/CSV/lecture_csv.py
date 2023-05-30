import csv
fichier=open("donnes.csv","r")
lecture_fichier = csv.DictReader(fichier, delimiter=',')
liste_personnes = []
for ligne in lecture_fichier:
    liste_personnes.append(dict(ligne))
fichier.close()

for personne in liste_personnes :
    print(personne)
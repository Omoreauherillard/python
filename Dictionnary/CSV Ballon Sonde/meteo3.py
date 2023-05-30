import csv
fichier=open("ballon2019.csv", "r", encoding="utf-8")
lecture_fichier = csv.DictReader(fichier, delimiter=',')

liste_donnees=[]
for ligne in lecture_fichier:
    liste_donnees.append(dict(ligne))
fichier.close()

mintemp=100
for donnees in liste_donnees:
    if float(donnees["Temp Ext C"])<float(mintemp):
        mintemp=donnees["Temp Ext C"]
        horaire=donnees["Horaire"]
print("La température la plus froide est",mintemp,"et est atteinte à",horaire)



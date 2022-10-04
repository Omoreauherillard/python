"""
#Exercice 1
a=8
carre=a**2
print("La valeur de a=",a,"au carré est de", carre)
"""
"""
#Exercice 2
kilometre=100
miles=kilometre/1.609
print("La distance de", kilometre,"kilometre est de",miles,"miles")
"""
"""
#Exercice 3
a=45
b=67
print("Avant échange a=",a,"et b=",b)
temp=a
a=b
b=temp
print("Après l'échange a=",a,"et b=",b)
"""
"""
#Exercice 4
valeur_tva=20
prix_ht=40
tva=prix_ht*valeur_tva/100
prix_ttc=prix_ht+tva
print("Prix HT du produit:",prix_ht,"€")
print("Indice de la TVA en 2015:",valeur_tva,"%")
print("Valeur de la TVA:",tva,"€")
print("Prix TTC:",prix_ttc,"€")
"""
"""
#Exercice 5
a=3
b=-15
r=a*b
if r>0:
    print("Le produit de",a,"et",b,"est positif")
elif r<0:
    print("Le produit de",a,"et",b,"est négatif")
else:
    print("nope")
"""
"""

#Exercice 7
nb_valeur=120
a=1
b=0
for i in range(0,nb_valeur,1):
    a+=1
    b=b+a
print("la somme des nombres entiers de 0 à ",nb_valeur,"est:",b)
"""
"""
#Exercice 8
for a in range(0,11):
    for b in range(0,11):
        c=a*b
        print(c,end=" ")
    print()
"""

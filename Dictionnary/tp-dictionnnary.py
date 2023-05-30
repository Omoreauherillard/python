"""stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

for nom, num in stock.items():
    print(nom, '->',num)
    """
"""stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print('fraises' in stock.keys())
print('banane' in stock.keys())
print(7 in stock.values())
print(5 in stock.values())
print(3 in stock.values())
"""
"""stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
stock["fraises"]=20
print(stock)
stock["abricots"]=15
print(stock)
"""
"""stock = {'poires': 5, 'pommes': 10, 'fraises': 35}

print(stock)
del stock["fraises"]
print(stock)
valeur = stock.pop("pommes")
print(stock)
print(valeur)
"""
"""#Exercice 1
d={'nom':'Dupuis','prenom':'Jacque','age':30}
d["prenom"]="Jacques"
print(d)
for i,j in d.items():
    print(i, " : ",j)
print(d["prenom"], d["nom"], "a", d["age"],"ans")
"""
"""#Exercice 2
liste={'Croissants':6,'Pizza':2,'Café en grains (500gr)':3,'Riz (1kg)':1}
liste["Pizza"]+=1
print(liste)
for i,j in liste.items():
    print(i, "->",j)
"""
#Exercice 3
"""chaine="Je m'appelle Emmanuel Macron"
dict={}
for i in chaine:
    if i in dict.keys():
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
"""
"""#Exercice 4
def anagram(chaine1,chaine2):
    dict1={}
    for i in chaine1:
        if i in dict1.keys():
            dict1[i]=dict1[i]+1
        else:
            dict1[i]=1
    dict2={}
    for i in chaine2:
        if i in dict2.keys():
            dict2[i]=dict2[i]+1
        else:
            dict2[i]=1
    del dict1[" "]
    del dict2[" "]
    if dict1==dict2:
        return True
    else:
        return False

chaine1="le rechauffement climatique"
chaine2="ce fuel qui tache le firmament"
print(anagram(chaine1,chaine2))
"""
"""#Exercice 5
def rendumonnaie(somme,pieces):
    choisie={}
    for p in pieces:
        choisie[p]=0
        while p<=somme:
            somme-=p
            choisie[p]+=1
    return choisie

somme=780
pieces=[500,200,100,50,20,10,5,2,1]
print(rendumonnaie(somme,pieces))
"""













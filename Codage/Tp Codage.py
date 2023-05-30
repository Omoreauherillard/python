"""#Exercice 1
car='a'
print(car)

car = 'b'
print(ord(car))
print(ord(car)+2)

valeur=66
print(chr(valeur))

car = 'a'
valeur=ord(car)+2
print(valeur)
print(chr(valeur))

valeur=346
print(chr(valeur))
valeur=0x1f3
print(chr(valeur))"""
#Exercice 2
"""new_message =""
message = input("Veuillez saisir un texte en MAJUSCULE et terminer par ENTER")
print("Vous avez saisi ",message)

for n in message:
    code_initial = ord(n)
    if code_initial>=97 and code_initial<=122:
        code_new = code_initial-32
    elif code_initial<=96 and code_initial>=65:
        code_new=code_initial+32
    else:
        code_new=code_initial
    car_new = chr(code_new)
    print(car_new)
    new_message = new_message + car_new

print (new_message)"""
#Exercice 3
"""import os
fichier=open("texte.txt","w")
fichier.write("bonjour\n")
fichier.write("salut")
fichier.close()

fichier=open("texte.txt","a")
fichier.write("hasta luego")
fichier.close()

fichier=open("texte.txt","r")
chaine=fichier.read()
print(chaine)
fichier.close()"""
#Exercice 4
message="Spécialité NSI 2019-2020"

fichier1=open("Exemple_encodage_Latin1.txt",'w',encoding="latin-1")

fichier2=open("Exemple_encodage_UTF-8.txt",'w',encoding="utf-8")

fichier3=open("Exemple_encodage_UTF-8_BOM.txt",'w',encoding="utf-8-sig")

fichier1.write(message)
fichier2.write(message)
fichier3.write(message)

fichier1.close()
fichier2.close()
fichier3.close()







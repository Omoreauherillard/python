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
#Exercice 6
a=float(input("Nombre positif"))
b=float(input("Nombre positif"))
c=float(input("Nombre positif"))
d=float(input("Nombre positif"))
e=float(input("Nombre positif"))
if a>b and a>c and a>d and a>e:
    print(a,"est le nombre le plus grand")
elif b>a and b>c and b>d and b>e:
    print(b,"est le nombre le plus grand")
elif c>a and c>b and c>d and c>e:
    print(c,"est le nombre le plus grand")
elif d>a and d>b and d>c and d>e:
    print(d,"est le nombre le plus grand")
elif e>a and e>b and e>c and e>d:
    print(e,"est le nombre le plus grand")

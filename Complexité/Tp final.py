from pylab import*
x=[]
y=[]
epaisseur=0.0001
hauteur=384400000

def fonction(epaisseur,hauteur):
    totalhauteur=epaisseur
    nbpliages=0
    while totalhauteur<hauteur:
        totalhauteur=totalhauteur*2
        nbpliages+=1
        x.append(totalhauteur)
        y.append(nbpliages)
    print(totalhauteur)
    return nbpliages

print(fonction(epaisseur,hauteur))

plot(x, y)
show()
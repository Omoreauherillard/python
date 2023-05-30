#import pygal   #question 8

coefficients=[5,5,5,5,5,5,10,10,8,10,16,16,100]
notes=[12,11,13,8,16,12,12.5,9,14,15,11,19]
matieres=["Enseignement scientifique",
            "Histoire/géographie",
            "Langue vivante A ",
            "Langue vivante B ",
            "EPS",
            "Enseignement spécialité 1ere",
            "Bulletins scolaires",
            "Français anticipé (écrit et oral)",
            "Philosophie ",
            "Grand oral de Terminale",
            "Enseignement spécialité 1",
            "Enseignement spécialité 2"]


def calculMoyenne(coefficients,notes):
    somme=0
    totalcoef=0
    for i in range(len(notes)):
        somme+=coefficients[i]*notes[i]
        totalcoef+=coefficients[i]
    total=somme/totalcoef
    return total

def traitementBac(moyenne):
    print ("Votre moyenne est de",moyenne)
    if moyenne<8:
        print("Vous n'avez pas votre BAC")
    if moyenne>=8 and moyenne<10:
        print("Aller aux RATTRAPAGES")
    if moyenne>=10 and moyenne<12:
        print("Vous avez votre BAC")
    if moyenne>=12 and moyenne<14:
        print("Vous avez votre BAC avec mention assez bien")
    if moyenne>=14 and moyenne<16:
        print("Vous avez votre BAC avec mention bien")
    if moyenne>=16:
        print("Vous avez votre BAC avec mention très bien")


def rechercheNoteMin(notes):
    min=notes[0]
    for i in range(len(notes)):
        if notes[i]>min:
            min=notes[i]
    print("Votre note minimale est", min)



def rechercheNoteMax(notes):
    max=notes[0]
    for i in range(len(notes)):
        if notes[i]<max:
            max=notes[i]
    print("Votre note maximale est", max)

def rechercheNote(notes,matieres,laNote):
    compteur=0
    for i in range(len(notes)):
        if notes[i]==laNote:
            compteur+=1
            print("Vous avez un", laNote, "en",matieres[i])
    print("Vous avez", laNote, "dans", compteur, "matière(s)")

def changeNote(notes,matieres):
    for i in range(len(notes)):
        loop=False
        while loop==False:
            texte="Nouvelle note en "+ matieres[i]
            newnote=int(input(texte))
            if newnote>20 or newnote<0:
                print("Erreur")
            else:
                loop=True
                notes[i]=newnote


def tableauBac(coefficients,notes,matieres):
    print("{0:36}{1:6}{2:6}{3:7}".format("Matières","Coeff","Notes","Points"))
    for i in range(len(notes)):
        print("{0:36}{1:6}{2:6}{3:7}".format(matieres[i],coefficients[i],notes[i],coefficients[i]*notes[i]))





moyenne=calculMoyenne(coefficients,notes)
traitementBac(moyenne)
rechercheNoteMin(notes)
rechercheNoteMax(notes)
rechercheNote(notes,matieres,13)
#changeNote(notes,matieres)
tableauBac(coefficients,notes,matieres)



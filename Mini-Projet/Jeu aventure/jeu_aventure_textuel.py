# Créé par osca.moreauherillard, le 11/10/2022 en Python 3.7
def description(piece):
    if piece==1:
        print("Vous êtes dans l'entrée")
    if piece==2:
        print("Vous êtes dans les toilettes")
    if piece==3:
        print("Vous êtes dans la troisième chambre")
    if piece==4:
        print("Vous êtes dans le couloir")
    if piece==5:
        print("Vous êtes dans la salle à manger")
    if piece==6:
        print("Vous êtes dans la cuisine")
    if piece==7:
        print("Vous êtes dans le bureau")
    if piece==8:
        print("Vous êtes dans la salle de bain")
    if piece==9:
        print("Vous êtes dans la deuxième chambre")
    if piece==10:
        print("Vous êtes dans la première chambre")

def decision(direction,piece):
    print("Vous desirez aller au",direction)
    memopiece=piece
    if direction=="n":
        if piece==1:
            piece=4
        elif piece==2:
            piece=3
        elif piece==3:
            piece=10
        elif piece==4:
            piece=9
        elif piece==5:
            piece=8
        elif piece==6:
            piece=7
    elif direction=="s":
        if piece==10:
            piece=3
        elif piece==9:
            piece=4
        elif piece==8:
            piece=5
        elif piece==7:
            piece=6
        elif piece==4:
            piece=1
        elif piece==3:
            piece=2
    elif direction=="e":
        if piece==2:
            piece=1
        elif piece==3:
            piece=4
        elif piece==4:
            piece=5
        elif piece==5:
            piece=6
        elif piece==10:
            piece=9
        elif piece==9:
            piece=8
        elif piece==9:
            piece=8
    elif direction=="o":
        if piece==1:
            piece=2
        elif piece==6:
            piece=5
        elif piece==5:
            piece=4
        elif piece==4:
            piece=3
        elif piece==7:
            piece=8
        elif piece==8:
            piece=9
        elif piece==9:
            piece=10
    return piece

pieceactuelle=1
menu="O"
while menu!="q":
    description(pieceactuelle)
    print("Ou désirez-vous aller? -------------------------------------")
    print("n : Nord")
    print("s : Sud")
    print("e : Est")
    print("o : Ouest")
    print("q : Quitter")
    print("------------------------------------------------------------")
    menu=input("Votre choix ?")
    pieceactuelle=decision(menu,pieceactuelle)

print("Bye")
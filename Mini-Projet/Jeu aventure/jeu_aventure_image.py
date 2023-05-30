# Créé par osca.moreauherillard, le 11/10/2022 en Python 3.7
import pygame

pygame.init()
fenetre=pygame.display.set_mode((640,360))
pygame.display.set_caption("jeu d'aventure")
font=pygame.font.Font('freesansbold.ttf',20)
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("toilettes1.jpg")
image3=pygame.image.load("chambre.jpg")
image4=pygame.image.load("couloir1.jpg")
image5=pygame.image.load("salle-a-manger.jpg")
image6=pygame.image.load("cuisine.jpg")
image7=pygame.image.load("bureau.jpg")
image8=pygame.image.load("salle-de-bain.jpg")
image9=pygame.image.load("chambre1.jpg")
image10=pygame.image.load("chambre2.jpg")
text1=font.render("Vous vous trouvez dans le vestibule", True, (0,255,0))
text2=font.render("Vous vous trouvez dans les toilettes", True, (0,255,0))
text3=font.render("Vous vous trouvez dans le couloir", True, (0,255,0))
text4=font.render("Vous vous trouvez dans la salle à manger", True, (0,255,0))
text5=font.render("Vous vous trouvez dans la cuisine", True, (0,255,0))
text6=font.render("Vous vous trouvez dans le bureau", True, (0,255,0))
text7=font.render("Vous vous trouvez dans la salle de bain", True, (0,255,0))
text8=font.render("Vous vous trouvez dans la chambre 1", True, (0,255,0))
text9=font.render("Vous vous trouvez dans la chambre 2", True, (0,255,0))
text10=font.render("Vous vous trouvez dans la chambre 3", True, (0,255,0))

def description(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(0,300))
    if piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(0,300))
    if piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,300))
    if piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(0,300))
    if piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(0,300))
    if piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(0,300))
    if piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(0,300))
    if piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(0,300))
    if piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(0,300))
    if piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(0,300))

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


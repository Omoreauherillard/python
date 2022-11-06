#Programme réalisé par Moreau--Hérillard, Oscar, 1G1
import pygame

FOND=(110,5,5)

pygame.init()
fenetre = pygame.display.set_mode((1000,650))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.SysFont ("Impact", 30)
image1=pygame.image.load("piece\\bureau.jpg")
image2=pygame.image.load("piece\\couloir.jpg")
image3=pygame.image.load("piece\\salle-commune.jpg")
image4=pygame.image.load("piece\\cour.png")
image5=pygame.image.load("piece\\grande-salle.jpg")
image6=pygame.image.load("piece\\dortoirs.jpg")
image7=pygame.image.load("piece\\cours-sortilege.jpg")
image8=pygame.image.load("piece\\escaliers.jpg")
image9=pygame.image.load("piece\\cours-potion.jpg")
image10=pygame.image.load("piece\\cours-divination.jpg")
image11=pygame.image.load("piece\\cours-botanique.jpg")
image12=pygame.image.load("piece\\cabane-hagrid.jpg")
image13=pygame.image.load("piece\\foret-interdite.png")
image14=pygame.image.load("piece\\salle-sur-demande.jpg")
image15=pygame.image.load("clef.png")
image16=pygame.image.load("carte\\carte1.png")
image17=pygame.image.load("carte\\carte2.png")
image18=pygame.image.load("carte\\carte3.png")
image19=pygame.image.load("carte\\carte4.png")
image20=pygame.image.load("carte\\carte5.png")
image21=pygame.image.load("carte\\carte6.png")
image22=pygame.image.load("carte\\carte7.png")
image23=pygame.image.load("carte\\carte8.png")
image24=pygame.image.load("carte\\carte9.png")
image25=pygame.image.load("carte\\carte10.png")
image26=pygame.image.load("carte\\carte11.png")
image27=pygame.image.load("carte\\carte12.png")
image28=pygame.image.load("carte\\carte13.png")
image29=pygame.image.load("carte\\carte14.png")
text1 = font.render("Bureau de Dumbledore", True, (0, 0, 0), (FOND))
text2 = font.render("Couloir", True, (0, 0, 0), (FOND))
text3 = font.render("Salle Commune Gryffondor", True, (0, 0, 0), (FOND))
text4 = font.render("Cour Intérieure", True, (0, 0, 0), (FOND))
text5 = font.render("Grande Salle", True, (0, 0, 0), (FOND))
text6 = font.render("Dortoirs", True, (0, 0, 0), (FOND))
text7 = font.render("Cours de Sortilège", True, (0, 0, 0), (FOND))
text8 = font.render("Escaliers", True, (0, 0, 0), (FOND))
text9 = font.render("Cours de Potion", True, (0, 0, 0), (FOND))
text10 = font.render("Cours de Divination", True, (0, 0, 0), (FOND))
text11 = font.render("Cours de Botanique", True, (0, 0, 0), (FOND))
text12 = font.render("Cabane d'Hagrid", True, (0, 0, 0), (FOND))
text13 = font.render("Forêt Interdite", True, (0, 0, 0), (FOND))
text14 = font.render("Salle sur Demande", True, (0, 0, 0), (FOND))

def secret(cleff,piece):
    if piece==13:
        cleff=1
        print("Vous avez trouvé une clé secrète")
    return cleff

def descriptionpiece(piece,cleff):
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==12:
        fenetre.blit(image12,(0,0))
        fenetre.blit(text12,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==13:
        fenetre.blit(image13,(0,0))
        fenetre.blit(text13,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==14:
        fenetre.blit(image14,(0,0))
        fenetre.blit(text14,(25,600))
        if cleff==1:
            fenetre.blit(image15,(775,455))
    elif piece==16:
        fenetre.blit(image16,(150,125))
    elif piece==17:
        fenetre.blit(image17,(150,125))
    elif piece==18:
        fenetre.blit(image18,(150,125))
    elif piece==19:
        fenetre.blit(image19,(150,125))
    elif piece==20:
        fenetre.blit(image20,(150,125))
    elif piece==21:
        fenetre.blit(image21,(150,125))
    elif piece==22:
        fenetre.blit(image22,(150,125))
    elif piece==23:
        fenetre.blit(image23,(150,125))
    elif piece==24:
        fenetre.blit(image24,(150,125))
    elif piece==25:
        fenetre.blit(image25,(150,125))
    elif piece==26:
        fenetre.blit(image26,(150,125))
    elif piece==27:
        fenetre.blit(image27,(150,125))
    elif piece==28:
        fenetre.blit(image28,(150,125))
    elif piece==29:
        fenetre.blit(image29,(150,125))

def decision(direction,piece,cleff):
    print("Vous désirez allez au",direction)
    memopiece=piece
    if direction=='n':
        if piece==1:
            piece=2
        elif piece==2:
            piece=3
        elif piece==4:
            piece=5
        elif piece==7:
            piece=8
        elif piece==8:
            piece=9
        elif piece==10:
            piece=11
        elif piece==12:
            piece=4
    elif direction=='s':
        if piece==2:
            piece=1
        elif piece==3:
            piece=2
        elif piece==4:
            piece=12
        elif piece==5:
            piece=4
        elif piece==8:
            piece=7
        elif piece==9:
            piece=8
        elif piece==11:
            piece=10
    elif direction=='e':
        if piece==1:
            piece=4
        elif piece==4:
            piece=7
        elif piece==2:
            piece=5
        elif piece==3:
            piece=6
        elif piece==5:
            piece=8
        elif piece==8:
            piece=10
        elif piece==9:
            piece=11
        elif piece==12:
            piece=13
        elif piece==14:
            piece=2
    elif direction=='o':
        if piece==4:
            piece=1
        elif piece==7:
            piece=4
        elif piece==8:
            piece=5
        elif piece==5:
            piece=2
        elif piece==6:
            piece=3
        elif piece==11:
            piece=9
        elif piece==10:
            piece=8
        elif piece==13:
            piece=12
        elif piece==2:
            if cleff==1:
                piece=14
                print("Bravo, vous avez découvert la salle secrète !")
    elif direction=='c':
        if piece==1:
            piece=16
        elif piece==2:
            piece=17
        elif piece==3:
            piece=18
        elif piece==4:
            piece=19
        elif piece==5:
            piece=20
        elif piece==6:
            piece=21
        elif piece==7:
            piece=22
        elif piece==8:
            piece=23
        elif piece==9:
            piece=24
        elif piece==10:
            piece=25
        elif piece==11:
            piece=26
        elif piece==12:
            piece=27
        elif piece==13:
            piece=28
        elif piece==14:
            piece=29
    elif direction=='r':
        if piece==16:
            piece=1
        if piece==17:
            piece=2
        if piece==18:
            piece=3
        if piece==19:
            piece=4
        if piece==20:
            piece=5
        if piece==21:
            piece=6
        if piece==22:
            piece=7
        if piece==23:
            piece=8
        if piece==24:
            piece=9
        if piece==25:
            piece=10
        if piece==26:
            piece=11
        if piece==27:
            piece=12
        if piece==28:
            piece=13
        if piece==29:
            piece=14
    elif direction=='q':
        print("Méfait Accompli")
    elif memopiece==piece:
        print("Déplacement impossible")
    return piece

pieceactuelle=4
clef=0
loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            pieceactuelle=decision(event.unicode,pieceactuelle,clef)
            clef=secret(clef,pieceactuelle)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False
    descriptionpiece(pieceactuelle,clef)
    pygame.display.flip()
pygame.quit()

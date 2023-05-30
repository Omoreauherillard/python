import pygame

LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Scrolling")
font = pygame.font.Font('freesansbold.ttf', 20)
frequence = pygame.time.Clock()

texteX=LARGEUR
texteY=100
vecteurX=-1
vecteurY=5
colornumber=2
color=VERT

def afficheTexte(x,y,txt,color):
    texteAfficher = font.render(str(txt), True, color)
    fenetre.blit(texteAfficher,(x,y))

def defilementTexte():
    global texteX,texteY,vecteurX,vecteurY
    texteX+=vecteurX
    texteY+=vecteurY
    if texteX==-235:
        texteX=LARGEUR
    elif texteY>HAUTEUR-5:
        vecteurY=vecteurY*-1
        changementcolor()
    elif texteY<0-5:
        vecteurY=vecteurY*-1

def changementcolor():
    global colornumber,color
    if colornumber==3:
        colornumber=1
    else:
        colornumber+=1
    if colornumber==1:
        color=ROUGE
    elif colornumber==2:
        color=VERT
    elif colornumber==3:
        color=BLEU




loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False


    fenetre.fill((0,0,0))
    afficheTexte(texteX,texteY,'Lycée Gabriel Touchard',color)
    defilementTexte()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()


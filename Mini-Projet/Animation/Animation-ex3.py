import pygame

LARGEUR=256
HAUTEUR=256
ROUGE=(255,0,0)
VERT=(0,255,0)
BLEU=(0,0,255)

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Balle")
font = pygame.font.Font('freesansbold.ttf', 20)
frequence = pygame.time.Clock()

RAYONBALLE=10
balleX=LARGEUR//2
balleY=HAUTEUR//2
vecteurBalleX=0
vecteurBalleY=0

def afficheBalle():
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    global balleX,balleY
    balleX=balleX+vecteurBalleX
    balleY=balleY+vecteurBalleY

def TestCollisionMur():
    global balleX,balleY,vecteurBalleX,vecteurBalleY
    if balleX>LARGEUR-RAYONBALLE:
        balleX=LARGEUR-RAYONBALLE
    elif balleY>LARGEUR-RAYONBALLE:
        balleY=HAUTEUR-RAYONBALLE
    elif balleX<0+RAYONBALLE:
        balleX=0+RAYONBALLE
    elif balleY<0+RAYONBALLE:
        balleY=0+RAYONBALLE

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        vecteurBalleY=-1
    elif keys[pygame.K_DOWN]:
        vecteurBalleY=1
    elif keys[pygame.K_RIGHT]:
        vecteurBalleX=1
    elif keys[pygame.K_LEFT]:
        vecteurBalleX=-1
    else:
        vecteurBalleY=0
        vecteurBalleX=0

    #fenetre.fill((0,0,0))
    afficheBalle()
    deplacementBalle()
    TestCollisionMur()
    frequence.tick(60)
    pygame.display.update()
pygame.quit()

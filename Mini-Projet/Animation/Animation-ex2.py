import pygame

LARGEUR=256
HAUTEUR=256
ROUGE=(255,0,0)
VERT=(0,255,0)
BLEU=(0,0,255)

pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Affichage")
font = pygame.font.Font('freesansbold.ttf', 20)
frequence = pygame.time.Clock()

RAYONBALLE=50
balleX=LARGEUR//2
balleY=HAUTEUR//2
vecteurBalleX=2
vecteurBalleY=1


def afficheBalle():
    pygame.draw.circle(fenetre, ROUGE, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    global balleX,balleY
    balleX+=vecteurBalleX
    balleY+=vecteurBalleY

def TestCollisionMur():
    global balleX,balleY,vecteurBalleX,vecteurBalleY
    if balleX>LARGEUR-RAYONBALLE:
        vecteurBalleX=vecteurBalleX*-1
    elif balleX<0+RAYONBALLE:
        vecteurBalleX=vecteurBalleX*-1
    elif balleY>HAUTEUR-RAYONBALLE:
        vecteurBalleY=vecteurBalleY*-1
    elif balleY<0+RAYONBALLE:
        vecteurBalleY=vecteurBalleY*-1

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False

    fenetre.fill((0,0,0))
    afficheBalle()
    deplacementBalle()
    TestCollisionMur()
    frequence.tick(60)
    pygame.display.update()
pygame.quit()


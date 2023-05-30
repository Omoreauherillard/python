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


def afficheCercle(x,y,rayon):
    pygame.draw.circle(fenetre, ROUGE, (x,y), rayon)

def afficheRectangle(x,y,largeur,hauteur):
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])

def afficheTexte(x,y,txt):
    texteAfficher = font.render(str(txt), True, VERT)
    fenetre.blit(texteAfficher,(x,y))


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                loop = False

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheCercle(200,200,50)
    afficheRectangle(50,10,80,30)
    afficheTexte(20,150,'bye')
    frequence.tick(60)
    pygame.display.update()
pygame.quit()


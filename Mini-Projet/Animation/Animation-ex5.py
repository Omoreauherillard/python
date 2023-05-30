import pygame

LARGEUR=256       #hauteur de la fenêtre
HAUTEUR=256      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Affichage")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame
mouseX=0
mouseY=0


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
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            color=fenetre.get_at((mouseX, mouseY))[:3]
            print(color)

    mouseX, mouseY = pygame.mouse.get_pos()

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheCercle(30,100,10)
    afficheRectangle(100,150,20,70)
    afficheTexte(100,50,str(mouseX)+' '+str(mouseY))
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()


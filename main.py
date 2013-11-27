import pygame, sys, os
from bebete import *
from pygame.locals import *
from util import *
from classIntro import *

pygame.init()

screen = pygame.display.set_mode((1024, 768), FULLSCREEN)
fond = pygame.image.load("fond.jpg").convert()
#pygame.display.toggle_fullscreen()
continuer = 1
intro = Intro(screen)
intro.start()

cursor = (0, 0)
bebete = Bebete()

cellulesLvl1 = list()
cellulesLvl1.append(Cellule((773, 456), 1))
objectifLvl1 = 1

cellulesLvl2 = list()
cellulesLvl2.append(Cellule((737, 232), 1))
cellulesLvl2.append(Cellule((240, 410), 1))
objectifLvl2 = 2

cellulesLvl3 = list()
cellulesLvl3.append(Cellule((600, 280), 1))
cellulesLvl3.append(Cellule((214, 454), 1))
cellulesLvl3.append(Cellule((830, 400), 1))
objectifLvl3 = 3

cellulesLvl4 = list()
cellulesLvl4.append(Cellule((776, 283), 1))
cellulesLvl4.append(Cellule((275, 436), 2))
objectifLvl4 = 3

cellulesLvl5 = list()
cellulesLvl5.append(Cellule((260, 260), 1))
cellulesLvl5.append(Cellule((926, 95), 1))
cellulesLvl5.append(Cellule((830, 190), 1))
cellulesLvl5.append(Cellule((850, 390), 1))
objectifLvl5 = 4

cellulesLvl6 = list()
cellulesLvl6.append(Cellule((745, 171), 1))
cellulesLvl6.append(Cellule((172, 292), 2))
cellulesLvl6.append(Cellule((257, 530), 2))
cellulesLvl6.append(Cellule((800, 375), 2))
objectifLvl6 = 5

cellulesLvl7 = list()
cellulesLvl7.append(Cellule((166, 553), 1))
cellulesLvl7.append(Cellule((845, 85), 1))
cellulesLvl7.append(Cellule((840, 327), 1))
cellulesLvl7.append(Cellule((835, 472), 1))
cellulesLvl7.append(Cellule((454, 454), 2))
cellulesLvl7.append(Cellule((220, 304), 4))
objectifLvl7 = 7

cellules = list()
cellules.append(cellulesLvl1)
cellules.append(cellulesLvl2)
cellules.append(cellulesLvl3)
cellules.append(cellulesLvl4)
cellules.append(cellulesLvl5)
cellules.append(cellulesLvl6)
cellules.append(cellulesLvl7)

currentLvl = 0

objectif = list()
objectif.append(objectifLvl1)
objectif.append(objectifLvl2)
objectif.append(objectifLvl3)
objectif.append(objectifLvl4)
objectif.append(objectifLvl5)
objectif.append(objectifLvl6)
objectif.append(objectifLvl7)

font = pygame.font.Font(None, 36)

while continuer:
    text = font.render(str(objectif[currentLvl]), 1, (10, 10, 10))
    for event in pygame.event.get():
      	if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0
        if event.type == MOUSEMOTION:
        	cursor = event.pos
    bebete.update(cursor)
    screen.blit(fond, (0, 0))
    for cellule in cellules[currentLvl]:
        screen.blit(cellule.getSurface(), cellule.getPos())
        if collision(bebete.getRayon(), cellule.getRayon(), bebete.getPos(), cellule.getPos()):
            bebete.addCellules(cellules[currentLvl][cellules[currentLvl].index(cellule)].getPoids())
            del(cellules[currentLvl][cellules[currentLvl].index(cellule)])
    bebetePos = bebete.getPos()
    if bebetePos[1] > 686 and bebetePos[0] < 687 and bebetePos[0] > 393 and objectif[currentLvl] == bebete.getPoids():
        currentLvl += 1
        del(bebete)
        bebete = Bebete()
    #elif bebetePos[1] > 686 and bebetePos[0] < 687 and bebetePos[0] > 393 and objectif[currentLvl] < bebete.getPoids():
        #break
    if currentLvl > 6:
        continuer = 0
    bebete.display(screen)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos[1] = textpos[1] + 700
    screen.blit(text, textpos)
    pygame.display.flip()
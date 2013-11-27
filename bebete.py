import pygame, math
from cellule import *
from vecteur import *

class Bebete:
	def __init__(self):
		self.surface = pygame.image.load("tete.png")
		self.diametre = self.surface.get_width()
		self.rayon = self.diametre / 2
		self.angle = 0.0
		self.cellules = list()
		self.pos = (512, 388)
		pygame.mouse.set_pos((512, 388))
		self.addCellules(0)

	def display(self, screen):
		for cellule in self.cellules:
			screen.blit(cellule.getSurface(), cellule.getPos())
		screen.blit(self.surface, self.pos)

	def update(self, curseur):
		if curseur == self.pos:
			return None
		oldPos = self.pos
		norme = math.sqrt((self.pos[0] - curseur[0]) ** 2 + (self.pos[1] - curseur[1]) ** 2)
		coef = 0
		if norme < self.diametre:
			self.pos = curseur
			coef = norme / self.diametre
		else:
			coef = self.diametre / norme
			vecteurX = (curseur[0] - self.pos[0]) * coef
			vecteurY = (curseur[1] - self.pos[1]) * coef
			self.pos = (oldPos[0] + vecteurX, oldPos[1] + vecteurY)
		for cellule in self.cellules:
			savePos = cellule.getPos()
			vecteurX = (oldPos[0] - savePos[0]) * coef
			vecteurY = (oldPos[1] - savePos[1]) * coef
			cellule.setPos((savePos[0] + vecteurX, savePos[1] + vecteurY))
			oldPos = savePos

	def addCellules(self, poids):
		poidsBebete = 0
		for cellule in self.cellules:
			poidsBebete += cellule.getPoids()
		s = str(bin(poidsBebete + poids))[2:]
		if len(self.cellules) == 0:
			self.cellules.append(Cellule((self.pos[0] - self.diametre, self.pos[1]), 0))
		if len(s) > len(self.cellules) :
			for i in range(0, len(s) - len(self.cellules)):
				self.cellules.append(Cellule((self.cellules[-1].getPos()[0] - self.diametre, self.cellules[-1].getPos()[1]), 0))
		print(s)
		for i in range(0, len(s)):
			if s[len(s) - i - 1] == "0":
				self.cellules[i].setPoids(0)
			else:
				self.cellules[i].setPoids(2 ** i)

	def getRayon(self):
		return self.rayon

	def getPos(self):
		return self.pos

	def getPoids(self):
		poids = 0
		for cellule in self.cellules:
			poids += cellule.getPoids()
		return poids
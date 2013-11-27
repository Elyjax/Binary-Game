import pygame

images = dict()
#images[0] = pygame.image.load("0.png").convert()
# images[1] = pygame.image.load("1.bmp")
# images[2] = pygame.image.load("2.bmp")
# images[4] = pygame.image.load("4.bmp")
# images[8] = pygame.image.load("8.bmp")
# images[16] = pygame.image.load("16.bmp")

class Cellule:
	def __init__(self, pos, poids):
		self.pos = pos
		self.poids = poids
		self.rayon = 21 # A CHANGER
		self.image = pygame.image.load(str(self.poids) + ".png")
	def getSurface(self):
		return self.image

	def getVector(self):
		return self.vector

	def setPos(self, pos):
		self.pos = pos

	def getPos(self):
		return self.pos

	def getRayon(self):
		return self.rayon

	def setPoids(self, poids):
		self.poids = poids
		self.image = pygame.image.load(str(self.poids) + ".png")

	def getPoids(self):
		return self.poids
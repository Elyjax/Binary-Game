import math

class Vecteur:
	def __init__(self, x, y):
		self.x = x
		self.y = y


	def add(self, v):
		# ajoute un vecteur a celui ci
		x = x + v.x
		y = y + v.y


	def sub(self, v):
		# soustrait un vecteur a celui ci
		x = x - v.x
		y = y - v.y

	def multBy(self, n):
		# homothetie d'un vecteur (scale) par multiplication
		self.x = self.x * n
		self.y = self.y * n

	def divBy(self, n):
		# homothetie d'un vecteur (scale) par division
		self.x = self.x / n
		self.y = self.y / n

	def magnitude(self):
		#retourne la magnitude d'un vecteur
		return math.sqrt(self.x * self.x + self.y * self.y)

	def normalize(self):
		# normalise un vecteur (sa longueur = 1)
		m = self.magnitude()
		if m != 0:
			self.divBy(m)

	def setMag(self, n):
		self.normalize()
		self.multBy(n)


	def invert(self):
		self.x = -self.x
		self.y = -self.y
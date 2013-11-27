import sys, pygame
from pygame.locals import *

import classIntro


class Intro:
	def __init__(self, screen):
		self.screen = screen
		splashscreen = pygame.image.load("splash.jpg").convert()
		self.screen.blit(splashscreen, (0,0))
		pygame.display.flip()

	def start(self):
		while 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit(0)
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						sys.exit(0)
				elif event.type == MOUSEBUTTONUP:
					return 0

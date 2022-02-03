import pygame
import timeit
from pygame.locals import(RLEACCEL, K_w, K_s, K_a, K_d, K_ESCAPE, KEYDOWN, QUIT)
import asyncio
pygame.init()

class Entities(pygame.sprite.Sprite):
	def __init__(self):
		super(Entities, self).__init__()
		self.supported = True
		self.gravity= .1
		self.vertspeed=0
		self.facing=None
		allGroup.add(self)
	def blitme(self):
		if self.facing=='right':
			screen.blit(self.surf, self.rect)
		elif self.facing=='left':
			screen.blit(self.flippedSurf, self.rect)
		else:
			raise

class Player(Entities):
	def __init__(self):
		super(Player, self).__init__()
		self.surf=pygame.image.load("StandingBines.png")
		self.surf.set_colorkey((255,255,255),RLEACCEL)
		self.rect=self.surf.get_rect()
		self.facing='right'
		self.flippedSurf=pygame.transform.flip(self.surf, True, False)
		playerGroup.add(self)
	def update(self, keys):
		if keys[K_w]:
			if self.supported==True:
				self.vertspeed=-5
				self.supported=False
		if keys[K_s]:
			self.rect.move_ip(0, 5)
		if keys[K_a]:
			self.rect.move_ip(-5, 0)
			self.facing='left'
		if keys[K_d]:
			self.rect.move_ip(5, 0)
			self.facing='right'
		self.rect.move_ip(0, self.vertspeed)
		self.vertspeed+=self.gravity
		if self.rect.left < 0: self.rect.left = 0 
		if self.rect.right > screenSize[0]: self.rect.right= screenSize[0]
		if self.rect.top < 0: self.rect.top = 0
		if self.rect.bottom > screenSize[1]: self.rect.bottom = screenSize[1]
		for each in terrainGroup:
			if pygame.sprite.collide_rect(bines, each):
				self.supported=True
				self.vertspeed=0

class Terrain(Entities):
	def __init__(self, img):
		super(Terrain, self).__init__()
		self.surf=pygame.image.load(img)
		self.rect=self.surf.get_rect()
		self.facing='right'
		terrainGroup.add(self)


terrainGroup=pygame.sprite.Group()
allGroup=pygame.sprite.Group()
playerGroup=pygame.sprite.Group()

bines=Player()
screenSize = (1800, 1000)
screen = pygame.display.set_mode(screenSize)

testPlatform=Terrain('platform.png').surf
testGround=pygame.transform.scale(Terrain('platform.png').surf, (1800, 100),)
running=True
while running:
	for event in pygame.event.get():
		if event.type==KEYDOWN:
			if event.key == K_ESCAPE:
				running=False
		elif event.type == QUIT:
				running=False
	pressedKeys=pygame.key.get_pressed()

	bines.update(pressedKeys)

	
	screen.fill((0,0,0))
	bines.blitme()
	screen.blit(testPlatform, (900, 500))
	screen.blit(testGround, (0, 950))
	pygame.display.flip()
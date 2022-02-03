import pygame
from settings import tileSize
from support import importFolder
class Entities(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Tile(Entities):
    def __init__(self, pos, size):
        super().__init__()
        self.image=pygame.Surface((size,size))
        self.rect=self.image.get_rect(topleft=pos)
        self.image.fill('grey')
    def update(self, xShift):
        self.rect.x += xShift

class Player(Entities):
    def __init__(self, pos):
        super().__init__()
        #player assets
        self.importCharacterAssets()
        self.frameIndex=0
        self.animationSpeed=0.15
        self.image=self.animations['idle'][self.frameIndex]
        self.rect=self.image.get_rect(topleft=pos)
        self.supported=False
        # player movement
        self.direction=pygame.math.Vector2(0,0)
        self.speed=8
        self.gravity=0.8
        self.jumpSpeed = -16
    def importCharacterAssets(self):
        characterPath='./assets/character/'
        self.animations = {'idle':[],'run':[], 'jump':[],'fall':[]}
        for each in self.animations.keys():
            fullPath= characterPath+each
            self.animations[each] = importFolder(fullPath)
    def getInput(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.jump()
        elif keys[pygame.K_a]:
            self.direction.x=-1
        elif keys[pygame.K_s]:
            pass
        elif keys[pygame.K_d]:
            self.direction.x=1
        else:
            if self.direction.x>0:
                self.direction.x-=.1
            if self.direction.x<0:
                self.direction.x+=.1
    def applyGravity(self):
        self.direction.y+=self.gravity
        self.rect.y+=self.direction.y
    def jump(self):
        if self.supported:
            self.direction.y=self.jumpSpeed
            self.supported=False
    def update(self):
        self.getInput()

class Coin(Entities):
    def __init__(self, pos):
        super().__init__()
        self.image=pygame.Surface((32,32))
        self.image.fill('gold')
        self.rect=self.image.get_rect(topleft=pos)

import pygame
from entities import Tile, Player, Coin
from settings import tileSize, screenWidth

class LevelHandler:
    def __init__(self, levelData, surface):
        self.displaySurface=surface
        self.setupLevel(levelData)
    def setupLevel(self, layout):
        self.tiles=pygame.sprite.Group()
        self.player=pygame.sprite.Group()
        self.coins=pygame.sprite.Group()
        for rowIndex, row in enumerate(layout):
            for columnIndex, column in enumerate(row):
                if column == "X":
                    self.tiles.add(Tile((columnIndex*64,rowIndex*64), tileSize))
                if column == "P":
                    self.player.add(Player((columnIndex*64, rowIndex*64)))
                if column == "C":
                    self.coins.add(Coin((columnIndex*64, rowIndex*64)))
    def scroll_x(self):
        playersprite = self.player.sprites()[0]
        player_x = playersprite.rect.centerx
        direction_x = playersprite.direction.x
        if player_x < screenWidth/4 and direction_x < 0:
            self.tiles.update(8)
            playersprite.speed=0
        elif player_x > 3*screenWidth/4 and direction_x > 0:
            self.tiles.update(-8)
            playersprite.speed=0
        else:
            self.tiles.update(0)
            playersprite.speed=8
    def horizontalMovementCollision(self):
        playerSprite=self.player.sprites()[0]
        playerSprite.rect.x+=playerSprite.direction.x*playerSprite.speed
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(playerSprite.rect):
                if playerSprite.direction.x<0:
                    playerSprite.rect.left=sprite.rect.right
                if playerSprite.direction.x>0:
                    playerSprite.rect.right=sprite.rect.left
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(playerSprite.rect):
                sprite.kill()
    def verticalMovementCollision(self):
        playerSprite=self.player.sprites()[0]
        playerSprite.applyGravity()
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(playerSprite.rect):
                if playerSprite.direction.y<0:
                    playerSprite.rect.top=sprite.rect.bottom
                    playerSprite.direction.y=0
                if playerSprite.direction.y>0:
                    playerSprite.rect.bottom=sprite.rect.top
                    playerSprite.direction.y=0
                    playerSprite.supported=True
    def run(self):
        self.tiles.draw(self.displaySurface)
        self.coins.draw(self.displaySurface)
        self.player.draw(self.displaySurface)
        self.tiles.update(0)
        self.player.update()
        self.horizontalMovementCollision()
        self.verticalMovementCollision()
        self.scroll_x()
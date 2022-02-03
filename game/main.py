import pygame, os, sys, datetime
from settings import *
from level1 import *
from levelHandling import LevelHandler
pygame.init()
screen=pygame.display.set_mode((screenWidth, screenHeight))
clock=pygame.time.Clock()
level=LevelHandler(levelMap, screen)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)
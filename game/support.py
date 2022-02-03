from os import walk
import pygame
def importFolder(path):
    surfaceList=[]
    for _,__,imgFiles in walk(path):
        for img in imgFiles:
            imgPath=path+'/'+img
            imageSurface=pygame.image.load(imgPath).convert_alpha()
            surfaceList.append(imageSurface)
    return surfaceList
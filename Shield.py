import pygame
import random
from Power import *
from Player import *
pygame.init()
import time


class Shield:
    def __init__(self,x,y,rad,speed):
        self.x = x
        self.y = y
        self.rad = rad
        self.speed = speed
    def draw(self,window):
            pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(self.x - 25,self.y -25, 150, 20))
            
shield = Shield(p1.x,p1.y, 50, 2)




def collision2(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False

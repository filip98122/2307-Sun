import pygame
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
        self.rect = pygame.Rect(self.x - 95,self.y - 95, 190, 20)
    def draw(self,window):
        self.rect = pygame.Rect(self.x - 95,self.y - 95, 190, 20)
        pygame.draw.rect(window, pygame.Color("Red"), self.rect)
    
    def move(self,x,y):
        self.x = x
        self.y =y
    
            
shield = Shield(p1.x,p1.y, 50, 2)




def collision2(rect1 : pygame.Rect,rect2):
    if rect1.colliderect(rect2):
        return True
    return False

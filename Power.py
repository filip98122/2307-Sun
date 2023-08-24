import pygame
import random
from Rain import *
import math
from Player import *
from Player import *
from Cloud import *

l_clouds = []
for i in range(3):
    kloud = Cloud(random.randint(700,900),random.randint(100,400), random.randrange(-4,-2), pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    l_clouds.append(kloud)

p1 = Player(200,935,100,100,50,0,0,4.5)

pygame.init()

def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True

class Power:
    def __init__(self,x,y,speed,r,active):
        self.x = x
        self.y = y
        self.speed = speed
        self.r = r
        self.color = pygame.Color(255,0,238)
        self.active = active
    def draw(self,window):
        pygame.draw.circle(window, pygame.Color(self.color), (self.x,self.y),self.r)
    def move(self):
        self.y += self.speed

power = Power(kloud.x,kloud.y,3.5,75,0)
        
import pygame
import random
from Rain import *
from Power import *
pygame.init()


def spawnrain(x,y, l_raindrops):
    raindrop = None
    for r in l_raindrops:
        if r.active == 0:
            raindrop = r
            break
        
    if raindrop == None:
        raindrop = Rain(x,y - 10,5,4,pygame.Color(58,213,255))
        l_raindrops.append(raindrop)
        
    raindrop.x = x
    raindrop.y = y
    raindrop.radius = 5
    raindrop.active = 1
    raindrop.color = pygame.Color(58,213,255)
    raindrop.speed = 4
    return l_raindrops


class Cloud:
    def __init__(self,x,y,speed,color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.size = random.randint(20,60)
        self.grayness = random.randint(1,54)
    def draw(self,window):
        
        if self.size > 50:
            self.speed = -4.5
        
        if self.size > 35 and self.size < 45:
            self.speed = -3
        
        if self.size < 30:
            self.speed = -1.5
        
        if self.x >= 1104:
            if self.grayness > 0:
                self.grayness = random.randint(1,54)
        
        if self.grayness >= 55:
            self.grayness = 0
        
        self.color = pygame.Color(255 - self.grayness,255 - self.grayness,255 - self.grayness)
        
        pygame.draw.circle(window, pygame.Color(self.color), (self.x - self.size * 0.3, self.y), self.size) # Draws a cloud
        pygame.draw.circle(window, pygame.Color(self.color), (self.x + self.size * 0.6, self.y - 20), self.size) # Draws a cloud
        pygame.draw.circle(window, pygame.Color(self.color), (self.x + self.size * 1.4, self.y), self.size) # Draws a cloud
        pygame.draw.circle(window, pygame.Color(self.color), (self.x + self.size * 0.6, self.y), self.size) # Draws a cloud
        
        pass
    
    def move(self, l):
        self.x += self.speed
        
        if self.x <= -105:
            self.x = 1105
        
        randrop = random.randint(0,1000)
        
        if randrop <= 10:
            if self.grayness >= 0:
                l = spawnrain(self.x + random.randint(0,30),self.y, l)
        return l
        pass
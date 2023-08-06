import pygame
pygame.init()


class Sun:
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.active = 0 
        self.speed = speed
        
    def draw(self,window):
        pygame.draw.circle(window, pygame.Color("Yellow"), (self.x,self.y), 75) # Draws the sun
            
    def move(self):
        if self.active == 0:
            return
        
        self.y += self.speed
        if self.y < -85:
            self.y = 1081
            
    def make(self):    
            pass
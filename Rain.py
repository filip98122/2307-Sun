import pygame
pygame.init()



class Rain:
    def __init__(self,x,y,radius,speed,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.color = color
        self.active = 1

    def draw(self,window):
        if self.active == 0:
            return
        
        self.color = pygame.Color(58,213,255)
        
        pygame.draw.circle(window,(self.color), (self.x,self.y), 5) # Draws a raindrop

    def move(self):
        if self.active == 0:
            return
        self.y += self.speed
        
        if self.y >= 1000:
            self.active = 0
            self.y = 0
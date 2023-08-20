import pygame
pygame.init()
class Player:
    dx = 0
    dy = 0
    def __init__(self,x,y,width,height,radius,px,py,speed) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.radius = radius
        self.px = px
        self.py = py
        self.speed = speed
        self.rect = pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, 100, 100)
        
    def move(self, keys):
        self.dx = 0
        self.dy = 0
        if self.x > 50:
            if keys[pygame.K_LEFT]:
                self.dx =- 1
                
        if self.x < 950:
            if keys[pygame.K_RIGHT]:
                self.dx += 1
                
        if self.y > 50:
            if keys[pygame.K_UP]:
                self.dy -= 1
        
        if self.y < 935:
            if keys[pygame.K_DOWN]:
                self.dy += 1
        self.x += self.speed * self.dx
        self.y += self.speed * self.dy
    
    def draw(self, window):
        pygame.draw.rect(window, pygame.Color("Red"), pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, 100, 100)) # Draws a rectangle
        pass
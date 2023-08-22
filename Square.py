import pygame
pygame.init()


class Square:
    dx = 7.5
    dy = 7.5
    redness = 10
    def __init__(self,x,y,speed, color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.rect3 = pygame.Rect(self.x, self.y, 75, 75)
        
    def draw(self, window):
        if self.redness > 250:
            self.redness = 0
        self.color = pygame.Color(self.redness,0 ,0)
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, 75, 75))
        
    def move(self, keys, player):
        self.keys = keys
        self.player = player
        
        # Bounce the ball of window edges
        if self.x <= 0:
            self.dx = 7.5
            self.redness+=25

        
        if self.x >= 900:
            self.dx = -7.5
            self.redness+=25

            
        if self.y <= 0:
            self.dy = 7.5
            self.redness+=25

            
        if self.y >= 900:
            self.dy = -7.5
            self.redness+=2
        
        
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
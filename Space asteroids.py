import pygame
import math

pygame.font.init()
pygame.init()


my_font = pygame.font.SysFont('Comic Sans MS', 20)
window = pygame.display.set_mode((1000,1000),flags=pygame.SCALED, vsync=1) # Makes window

def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True

class Player:
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def draw(self,window):
        pygame.draw.rect(window, pygame.Color("White"), pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, 100, 100)) # Draws a rectangle
        pass
    def move(self):
        self.dx = 0
        self.dy = 0
        if self.x > 75:
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
                
        if self.x < 975:
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
                
        if self.x > 75:
            if keys[pygame.K_a]:
                self.x -= self.speed
                
        if self.x < 975:
            if keys[pygame.K_d]:
                self.x += self.speed

clock = pygame.time.Clock()
p1 = Player(500,900,150,50,5.5)
                
while True:
    window.fill("Blue" ) # Resets window
    
    keys = pygame.key.get_pressed()
                
    if keys[pygame.K_ESCAPE]:
        exit()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    
    #moves player
    p1.move()
    
    
    
    
    
    #draws player
    p1.draw(window)
    
    pygame.display.update() # Updates window
    clock.tick(60)
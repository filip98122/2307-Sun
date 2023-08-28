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
        
    def move(self):
        
        if self.x > 82:
            if keys[pygame.K_a] == False:
                if keys[pygame.K_LEFT]:
                    self.x -= self.speed
                
        if self.x < 985:
            if keys[pygame.K_d] == False:
                if keys[pygame.K_RIGHT]:
                    self.x += self.speed
                
        if self.x > 82:
            if keys[pygame.K_LEFT] == False:
                if keys[pygame.K_a]:
                    self.x -= self.speed
                
        if self.x < 985:
            if keys[pygame.K_RIGHT] == False:
                if keys[pygame.K_d]:
                    self.x += self.speed

class Laser:
    def __init__(self,x,y,speed,width,height,active,color):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height
        self.active = active
        self.color = color
        self.rect = pygame.draw.rect(window, pygame.Color("White"), pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, 100, 100))
    
    def draw(self,window):
        pygame.draw.rect(window, pygame.Color("White"), pygame.Rect(self.x - self.width / 2, self.y - self.height / 2, 20, 100)) # Draws a rectangle
    def move(self):
        self.y -= self.speed
        


clock = pygame.time.Clock()
p1 = Player(500,900,175,25,5.5)


l_lasers = []
for i in range(1):
    lasers = Laser(p1.x - 100,900,7.5,20,100,0,pygame.Color(171,3,49))
    l_lasers.append(lasers)


a = 1
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

    for i in l_lasers:
        if lasers.y <= 60:
            lasers.active = 0
            lasers.y = p1.y
            lasers.x = p1.x
            a = 1
        
        if keys[pygame.K_SPACE]:
            lasers.active = 1
        
        if keys[pygame.K_SPACE]:
            if a == 1:
                lasers.x = p1.x - 40
                lasers.y = p1.y
                a -= 1 
        
        if lasers.active == 1:
            lasers.move()
    
    
    
    
    
    
    #draws player
    p1.draw(window)
    
    
    for i in l_lasers:
        if lasers.active == 1:
            lasers.draw(window)
    
    
    pygame.display.update() # Updates window
    clock.tick(60)
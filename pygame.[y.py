import pygame
import random
pygame.init()


window = pygame.display.set_mode((1000,1000)) # Makes window




class Player:
    dx = 0
    dy = 0
    def __init__(self,x,y,speed) -> None:
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, keys):
        self.dx = 0
        self.dy = 0
        if self.x > 0:
            if keys[pygame.K_LEFT]:
                self.dx =- 1
                
        if self.x < 900:
            if keys[pygame.K_RIGHT]:
                self.dx += 1
                
        if self.y > 0:
            if keys[pygame.K_UP]:
                self.dy -= 1
        
        if self.y < 900:
            if keys[pygame.K_DOWN]:
                self.dy += 1
        self.x += self.speed * self.dx
        self.y += self.speed * self.dy
    
    def draw(self, window):
        pygame.draw.rect(window, pygame.Color("Blue"), pygame.Rect(self.x, self.y, 100, 100)) # Draws a rectangle
        pass

class ball:
    dx = 1
    dy = 1
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y 
        self.speed = speed
        
    def draw(self, window):
        pygame.draw.rect(window, pygame.Color("Gray"), pygame.Rect(self.x, self.y, 75, 75))
        
    def move(self, keys, player):
        
        if self.x <= 0:
            self.dx = 1
        
        if self.x >= 900:
            self.dx = -1
            
        if self.y <= 0:
            self.dy = 1
            
        if self.y >= 900:
            self.dy = -1
        
        
        
        
        
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        
        pass

p1 = Player(0,0,1)

l = []

for i in range(3):
    playa = ball(random.randint(100,900),random.randint(100,900), random.randrange(1,2))
    l.append(playa)

while True:

    window.fill("Red") # Resets window
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        exit()
        
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Move player
    p1.move(keys)
            
    # Move non player objects
    for play in l:
        play.move(keys, p1)


    # Draw non player objects
    for play in l:
        play.draw(window)

    # Draw player
    p1.draw(window)


    pygame.display.flip() # Updates window
    
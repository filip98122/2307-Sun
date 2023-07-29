import pygame
import random
pygame.init()

window = pygame.display.set_mode((1000,1000)) # Makes window

class Player:
    dx = 0
    dy = 0
    def __init__(self,x,y,width,height,px,py,speed) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.px = px
        self.py = py
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
        pygame.draw.rect(window, pygame.Color("Red"), pygame.Rect(self.x, self.y, 100, 100)) # Draws a rectangle
        pass

class square:
    dx = 7.5
    dy = 7.5
    redness = 10
    def __init__(self,x,y,speed, color):
        self.x = x
        self.y = y 
        self.speed = speed
        self.color = color
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

class sun:
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

class cloud:
    dx = -0.20
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
        
    def draw(self,window):
        pygame.draw.circle(window, pygame.Color("White"), (self.x - 20, self.y), 45) # Draws a cloud
        pygame.draw.circle(window, pygame.Color("White"), (self.x + 40, self.y - 20), 50) # Draws a cloud
        pygame.draw.circle(window, pygame.Color("White"), (self.x + 90, self.y), 45) # Draws a cloud
        pygame.draw.circle(window, pygame.Color("White"), (self.x + 40, self.y), 45) # Draws a cloud
        
        pass
    
    def move(self):
        self.x += self.speed
    
        pass
sunce = sun(500,150, -6)
oblak = cloud(900,random.randint(150,300),-2.5)
p1 = Player(200,900,100,100,0,0,4.5)
kocka = square(random.randint(50,875),random.randint(50,875),3,0)

l = []

for i in range(3):
    playa = square(random.randint(100,900),random.randint(100,900), random.randrange(1,2), pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    l.append(playa)

cooldown = 30
clock = pygame.time.Clock()




while True:
    window.fill("Blue") # Resets window
    
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

    #draws sun
    cooldown -= 1
    if cooldown < 0:
        if keys[pygame.K_s]:
            cooldown = 15
            if sunce.active == 1:
                sunce.active = 0
            else:
                sunce.active = 1
    sunce.move()
    sunce.draw(window)
    
    pygame.draw.circle(window, pygame.Color("Green"), (200, 1000), 150) # Draws a hill
    pygame.draw.circle(window, pygame.Color("Green"), (750, 1075), 150) # Draws a hill
    pygame.draw.circle(window, pygame.Color("Green"), (500, 1075), 250) # Draws a hill
    pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(-1,985, 1000, 989)) # Draws the grass
    pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(-1,990, 1000, 1001)) # Draws the dirt
    pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(750,650, 100, 350)) # Draws the log of the tree
    pygame.draw.circle(window, pygame.Color("Green"), (800, 660), 150) # Draws the leavs
    
    
    
    
    #draws cloud
    oblak.move()
    oblak.draw(window)
    if oblak.x < - 200:
        oblak.x = 1200
        oblak.y = random.randint(150,300)

    #random.randint(150,200)
    
    # Draw non player objects
    for play in l:
        play.draw(window)

    # Draw player
    p1.draw(window)

    pygame.display.flip() # Updates window
    clock.tick(60)

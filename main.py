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
        
        if self.y < 885:
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
    
    def move(self):
        self.x += self.speed
        
        self.randrop = random.randint(0,3000)
        
        if self.randrop <= 10:
            self
        
        if self.x <= -105:
            self.x = 1105
        
        
        pass

class rain:
    def __init__(self,x,y,speed,color):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.active = 1

    def draw(self,window):
        if self.active == 0:
            return
        
        self.color = pygame.Color(58,213,255)
        
        pygame.draw.circle(window,(self.color), (self.x,self.y), 5) # Draws a raindrop
        if self.y >= 985:
            self.active = 0
            self.y = 0
            
    def move(self):
        if self.active == 0:
            return
        self.y += self.speed
        
        if self.y >= 985:
            self.active = 0
            self.y = 0
            
        pass

cloudx = random.randint(700,900)
cloudy = random.randint(150,300)

kisa = rain(cloudx,cloudy - 10,4,pygame.Color(58,213,255))
sunce = sun(500,150, -6)
p1 = Player(200,900,100,100,0,0,4.5)
kocka = square(random.randint(50,875),random.randint(50,875),3,0)

l_squares = []
for i in range(3):
    playa = square(random.randint(100,900),random.randint(100,900), random.randrange(1,2), pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    l_squares.append(playa)

l_clouds = []
for i in range(3):
    kloud = cloud(random.randint(700,900),random.randint(150,300),random.randint(-4,-2),pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    l_clouds.append(kloud)

l_raindrops = []
for i in range(1):
    raindrop = rain(300,0,4,pygame.Color(58,213,255))
    l_raindrops.append(raindrop)

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
    
    #moves cloud
    for kloud in l_clouds:
        kloud.move()
    
    if keys[pygame.K_r]:
        raindrop = None
        for r in l_raindrops:
            if r.active == 0:
                raindrop = r
                break
        
        if raindrop == None:
            raindrop = rain(100,0,4,pygame.Color(58,213,255))
            l_raindrops.append(raindrop)
        
        raindrop.x = 100
        raindrop.y = 0
        raindrop.active = 1
        raindrop.color = pygame.Color(58,213,255)
        raindrop.speed = 4
    
    #moves raindrop
    for raindrop in l_raindrops:
        raindrop.move()
        
    #draws raindrop
    for raindrop in l_raindrops:
        raindrop.draw(window)
    
    # Move player
    p1.move(keys)
            
    # Move non player objects
    for play in l_squares:
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
    pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(750,650, 100, 350)) # Draws the log of the tree
    pygame.draw.circle(window, pygame.Color("Green"), (800, 660), 150) # Draws the leavs
    pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(-1,985, 1000, 989)) # Draws the grass
    pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(-1,990, 1000, 1001)) # Draws the dirt
    
    
    #draws cloud
    for kloud in l_clouds:
        kloud.draw(window)
    
    # Draw non player objects
    for play in l_squares:
        play.draw(window)

    # Draw player
    p1.draw(window)
    
    print(f'Raindrops: {len(l_raindrops)}')

    pygame.display.flip() # Updates window
    clock.tick(60)

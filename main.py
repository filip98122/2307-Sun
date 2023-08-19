import pygame
import math
import random
import time


from Rain import *
from Cloud import *
from Sun import *
from Player import *
from Square import *
from Power import *
from Shield import *

shieldactive = 0
myscore = 0

pygame.font.init()
pygame.init()


my_font = pygame.font.SysFont('Comic Sans MS', 20)
window = pygame.display.set_mode((1000,1000),flags=pygame.SCALED, vsync=1) # Makes window


kisa = Rain(100,0,5,4,pygame.Color(58,213,255))
sunce = Sun(500,150, -6)
p1 = Player(200,935,100,100,50,0,0,5.5)
kocka = Square(random.randint(50,875),random.randint(50,875),3,0)

l_squares = []
for i in range(3):
    playa = Square(random.randint(100,900),random.randint(100,900), random.randrange(1,2), pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    l_squares.append(playa)

l_clouds = []
for i in range(3):
    kloud = Cloud(random.randint(700,900),random.randint(100,400), random.randrange(-4,-2), pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    l_clouds.append(kloud)

l_raindrops = []
for i in range(1):
    raindrop = Rain(300,0,5,4,pygame.Color(58,213,255))
    l_raindrops.append(raindrop)

cooldown = 30
clock = pygame.time.Clock()

def collison(x1,y1,r1,x2,y2,r2):
    dx = x2 - x1
    dy = y2 - y1
    dist  = dx * dx + dy * dy
    dist = math.sqrt(dist)
    
    if dist > r1 + r2:
        return False
    else:
        return True
        
def spawnrain(x,y):
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

ranbush = random.randint(300,850)
rantreex = random.randint(200,800)
ranflour = random.randint(100,900)

myhealth = 20
def debugMode(window, player,l,myscore):
    
    text_surface = my_font.render(f"Player pos: {(player.x, player.y)}", True, (0, 0, 0))
    window.blit(text_surface, (0,0))
    text_surface = my_font.render(f"Raindrops: {l} ", True, (0, 0, 0))
    window.blit(text_surface, (0,50))
    text_surface = my_font.render(f"Your Health: {myhealth} ", True, (0, 0, 0))
    window.blit(text_surface, (0,100))
    text_surface = my_font.render(f"Your score: {myscore} ", True, (0, 0, 0))
    window.blit(text_surface, (0,150))
    text_surface = my_font.render(f"Your Highscore: {highscore} ", True, (0, 0, 0))
    window.blit(text_surface, (0,200))


try:
    f = open("highscore.txt", "r")
    highscore = int(f.read())
    f.close()
except:
    f = open("highscore.txt", "w")
    f.close()
    highscore = -1


while True:
    window.fill("Blue") # Resets window
    
    shield = Shield(p1.x,p1.y, 50, 2)
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        exit()
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    
    if collison(p1.x,p1.y,p1.radius,power.x,power.y,power.r) == True:
        power.active = 0
        power.y = 1079
        shieldactive = 1
    
    #moves cloud
    for kloud in l_clouds:
        l_raindrops = kloud.move(l_raindrops)
    
    if keys[pygame.K_r]:
        spawnrain(0,0)
    
    # Collide rain drops
    for raindrop in l_raindrops:
        if collison(p1.x,p1.y,p1.radius,raindrop.x,raindrop.y,raindrop.radius) == True:
            raindrop.active = 0
            myscore += 1
            raindrop.y = 0
    
    #moves raindrop
    for raindrop in l_raindrops:
        raindrop.move()   
        if raindrop.y >= 980 and raindrop.active == True:
            myhealth -= 1
            raindrop.y = 0
            raindrop.active = False
    
    if myhealth <= 0:
        if myscore > highscore:
            f = open("highscore.txt","w")
            f.write(int(myscore))
            f.close()
        exit()
    
    if power.y >= 910:
        power.speed = 0
    
    # Move player
    p1.move(keys)
    
    # Move power
    if power.active >= 1:
        power.move()
            
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
    
    if myscore == 20:
        if myhealth <= 20:
            myhealth += 20
            raindrop.speed = 10
            
    pygame.draw.circle(window, pygame.Color("Green"), (ranbush - 200, 1025), 150) # Draws a bush
    pygame.draw.circle(window, pygame.Color("Green"), (ranbush, 1000), 100) # Draws a bush
    pygame.draw.circle(window, pygame.Color("Green"), (ranbush + 100, 1025), 125) # Draws a bush
    pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(rantreex,650, 100, 350)) # Draws the log of the tree
    pygame.draw.circle(window, pygame.Color("Green"), (rantreex + 50, 660), 150) # Draws the leavs
    pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(-1,985, 1000, 989)) # Draws the grass
    pygame.draw.rect(window, pygame.Color("Brown"), pygame.Rect(-1,990, 1000, 1001)) # Draws the dirt
    pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(ranflour,900, 50, 95)) # Draws the flour
    pygame.draw.circle(window, pygame.Color("Red"), (ranflour + 25,930),50)#draws the pedals of the flour
    pygame.draw.circle(window, pygame.Color("Yellow"), (ranflour + 25,930),25)#draws the bulb of the flour
    #draws cloud
    for kloud in l_clouds:
        kloud.draw(window)
    
        for raindrop in l_raindrops:
            raindrop.draw(window)
    
    for i in l_raindrops:
        pass
    
    if shieldactive == 1:
        shield.draw(window)
    
    # Draw non player objects
    for play in l_squares:
        play.draw(window)
    
    #Draw Power
    power.draw(window)
    
    # Draw player
    p1.draw(window)
    
    print(f'Raindrops: {len(l_raindrops)}')
    debugMode(window,p1,len(l_raindrops),myscore)
    pygame.display.update() # Updates window
    clock.tick(60)

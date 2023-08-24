import pygame
pygame.init()
window = pygame.display.set_mode((1000,1000),flags=pygame.SCALED, vsync=1)

my_font = pygame.font.SysFont('Comic Sans MS', 20)

mytext = text_surface = my_font.render(f" Play ", True, (0, 0, 0))
window.blit(text_surface, (0,250))

class Button:
    def __init__(self,rect, text, rectColor,textColor):
        self.rect = rect
        self.text = text
        self.rectColor = rectColor
        self.textColor = textColor
        
    def draw(self):
        pygame.Rect(750 - width,750 - height,250,250)
    

width = 250
height = 250

boton = Button(pygame.Rect(750 - width,750 - height,250,250),mytext, pygame.Color("Red"), pygame.Color("Blue"))



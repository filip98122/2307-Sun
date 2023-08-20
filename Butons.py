import pygame
pygame.init()

class Button:
    def __init__(self,rect, text, rectColor,textColor):
        self.rect = rect
        self.text = text
        self.rectColor = rectColor
        self.textColor = textColor
        
    def draw(self,window):
        pygame.draw.rect(window, self.rectColor, self.rect)
            
            
    
    
boton = Button(pygame.Rect(200,200,400,200), pygame.Color("Red"), pygame.Color("Blue"))



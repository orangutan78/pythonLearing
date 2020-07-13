import pygame
from pygame.locals import *
######################################################
pygame.init()
######################################################
def draw_X(x,y):
    
######################################################
x=1
while x:
    for event in pygame.event.get():
        if event.type == QUIT:
            x=0
        elif event.type==MOUSEBUTTONDOWN:
            #print(pygame.mouse.get_pressed())
            x,y=pygame.mouse.get_pos()
            print(x,y)
            draw_X(x,y)
    pygame.display.set_caption('井字棋')
    screen = pygame.display.set_mode([600, 600])
    screen.fill((255,255,255))
    pygame.draw.line(screen,(0,0,0),(200,0),(200,600),5)
    pygame.draw.line(screen,(0,0,0),(400,0),(400,600),5)
    pygame.draw.line(screen,(0,0,0),(0,200),(600,200),5)
    pygame.draw.line(screen,(0,0,0),(0,400),(600,400),5)
    pygame.display.update()
import pygame
from pygame.locals import *
import sys
######################################################
pygame.init()
e=1
a=1
o1=1
o2=1
o3=1
######################################################
form=[[1,1,1],[1,1,1],[1,1,1]]
######################################################
def draw_X(x,y):
    global form
    global a
    a=2
    if x in range(200) and y in range(200) and form[0][0]==1:
        pygame.draw.line(screen,(0,0,0),(50,50),(150,150),5)
        pygame.draw.line(screen,(0,0,0),(150,50),(50,150),5)
        form[0][0]==0
    if x in range(200) and y in range(200,400) and form[1][0]==1:
        pygame.draw.line(screen,(0,0,0),(50,250),(150,350),5)
        pygame.draw.line(screen,(0,0,0),(150,250),(50,350),5)
        form[1][0]==0
    if x in range(200) and y in range(400,600) and form[2][0]==1:
        pygame.draw.line(screen,(0,0,0),(50,450),(150,550),5)
        pygame.draw.line(screen,(0,0,0),(150,450),(50,550),5)
        form[2][0]==0
    if x in range(200,400) and y in range(200) and form[0][1]==1:
        pygame.draw.line(screen,(0,0,0),(250,50),(350,150),5)
        pygame.draw.line(screen,(0,0,0),(350,50),(250,150),5)
        form[0][1]==0
######################################################
def draw_O(x,y):
    global form
    global a
    a=1
    if x in range(200) and y in range(200) and form[0][0]==1:
        pygame.draw.circle(screen,(0,0,0),(100,100),50,5)
        form[0][0]=0
######################################################
pygame.display.set_caption('井字棋')
screen = pygame.display.set_mode([600, 600])
screen.fill((255,255,255))
pygame.draw.line(screen,(0,0,0),(200,0),(200,600),5)
pygame.draw.line(screen,(0,0,0),(400,0),(400,600),5)
pygame.draw.line(screen,(0,0,0),(0,200),(600,200),5)
pygame.draw.line(screen,(0,0,0),(0,400),(600,400),5)
while e:
    for event in pygame.event.get():
        if event.type == QUIT:
            e=0
        elif event.type==MOUSEBUTTONDOWN:
            if a==1:
                x,y=pygame.mouse.get_pos()
                draw_X(x,y)
            elif a==2:
                x,y=pygame.mouse.get_pos()
                draw_O(x,y)               
    pygame.display.update()
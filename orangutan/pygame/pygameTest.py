import pygame
from pygame.locals import *
from sys import exit
bg_image_file="orangutan/img/dola1.jpg"
mouse_image_file="orangutan/img/alo.jpg"
pygame.init()

FPS=60
fpsClock=pygame.time.Clock()

SCREEN_SIZE=(640,480)
#screen=pygame.display.set_mode((640,480),FULLSCREEN,32)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
pygame.display.set_caption("图像载入学习")
bg=pygame.image.load(bg_image_file)
mouse_image=pygame.image.load(mouse_image_file).convert_alpha()#提高blit速度
img_rect=mouse_image.get_rect()
speed=[5,5]
fullscreen=False
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        pygame.display.set_caption("Window resize to" + str(event.size))
     

    if event.type==KEYDOWN:
        if event.key==K_F1:
            fullscreen=not fullscreen
            if fullscreen:
                #screen=pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN,32)
                screen= pygame.display.set_mode(SCREEN,DOUBLEBUF| HWSURFACE | FULLSCREEN, 32)
            else:
                screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
        if event.key==K_LEFT:
            x-=1
    '''if event.type==MOUSEMOTION:
            x,y=pygame.mouse.get_pos()
    '''
    img_rect = img_rect.move(speed)

    if img_rect.left<0 or img_rect.right>640:
        speed[0]=-speed[0]
    if img_rect.top<0 or img_rect.bottom>480:
        speed[1]=-speed[1]
    #x-=mouse_image.get_width()/2
    #y-=mouse_image.get_height()/2
    screen.blit(bg,(0,0))
    screen.blit(mouse_image,img_rect)
    #pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(FPS)
    
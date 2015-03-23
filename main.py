import pygame
import time
import os

pygame.init()

white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
lightgrey = (210,210,210)
darkgrey = (100,100,100)
menu1 = pygame.image.load('1.JPG')
menu2 = pygame.image.load('2.JPG')
menu3 = pygame.image.load('3.JPG')
menu4 = pygame.image.load('4.JPG')
menu5 = pygame.image.load('5.JPG')
menu6 = pygame.image.load('6.JPG')
menu7 = pygame.image.load('7.JPG')
menu8 = pygame.image.load('8.JPG')
menu9 = pygame.image.load('9.JPG')

TitleText = pygame.font.Font('freesansbold.ttf',70)
SubText = pygame.font.Font('freesansbold.ttf', 20)

display = pygame.display.set_mode((800,600))
display.fill(white)

def text(font,text,center):
    textsurf = font.render(text,True,black)
    textrect = textsurf.get_rect()
    textrect.center = center
    display.blit(textsurf, textrect)

def rect(color, x, y, width, height):
    pygame.draw.rect(display,color,(x,y,width,height))

def render(image,x,y,w,h):
    image = pygame.transform.scale(image,(800,600))
    RECT = pygame.Rect(x,y,w,h)
    display.blit(image,RECT)

def circle(color, x, y, radius):
    pygame.draw.circle(display, color, (x,y), radius)

def button(text,x,y,w,h,tx,ty):
    mouse = pygame.mouse.get_pos()
    click = pygame.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        rect(lightgrey,x,y,w,h)
        circle(lightgrey, x,y+20,20)
        circle(lightgrey, x+w, y+20,20)
        
    else:
        rect(darkgrey,200,250,400,40)
        circle(darkgrey, 200,270,20)
        circle(darkgrey, 600, 270,20)
    text(SubText, 'New Game', (400,270))
    

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        render(menu1,0,0,800,600)
        rect(darkgrey, 150,50,500,100)
        circle(darkgrey, 150,100,50)
        circle(darkgrey, 650,100,50)
        text(TitleText, 'Hungry Cities', (400,100))

        if 180+440 > mouse[0] > 180 and 250+40 > mouse[1] > 250:
            rect(lightgrey,200,250,400,40)
            circle(lightgrey, 200,270,20)
            circle(lightgrey, 600, 270,20)
            if int(click[0]) == 1:
                print('I tried!')
            
        else:
            rect(darkgrey,200,250,400,40)
            circle(darkgrey, 200,270,20)
            circle(darkgrey, 600, 270,20)
        text(SubText, 'New Game', (400,270))

        if 180+440 > mouse[0] > 180 and 300+40 > mouse[1] > 300:
            rect(lightgrey,200,300,400,40)
            circle(lightgrey, 200,320,20)
            circle(lightgrey, 600, 320,20)
            if int(click[0]) == 1:
                print('Error 404: does not exist')
        else:
            rect(darkgrey,200,300,400,40)
            circle(darkgrey, 200,320,20)
            circle(darkgrey, 600, 320,20)
        text(SubText, 'Options', (400,320))


        if 180+440 > mouse[0] > 180 and 350+40 > mouse[1] > 350:
            rect(lightgrey,200,350,400,40)
            circle(lightgrey, 200,370,20)
            circle(lightgrey, 600, 370,20)
            text(SubText, 'Exit', (400,370))
            if int(click[0]) == 1:
                break
        else:
            rect(darkgrey,200,350,400,40)
            circle(darkgrey, 200,370,20)
            circle(darkgrey, 600, 370,20)
            text(SubText, 'Exit', (400,370))

        
        pygame.display.update()
    print('exit?')
    pygame.quit()
    os._exit(1)

def game():
    pass


def gamemenu():
    pass


menu()

import pygame
import time
import os
# todo list:
#make function for buttons that works?
#re-make png images
#idk

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('HungryCities')
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
grass = pygame.image.load('grass.jpg')
default_tracks_NS = pygame.image.load('tracksNS.png').convert_alpha()
default_tracks_EW = pygame.image.load('tracksEW.png').convert_alpha()
tier_NS = pygame.image.load('tierNS.png').convert_alpha()
tier_EW = pygame.image.load('tierEW.png').convert_alpha()

TitleText = pygame.font.Font('freesansbold.ttf',70)
SubText = pygame.font.Font('freesansbold.ttf', 20)


display.fill(white)

class city:
    def __init__(self):
        self.scrap = 0
        self.metal = 0
        self.inventory = {}
        self.fuel = 500
        self.food = 100
        self.population = 50
        self.tiers = {}
        self.engine = ['default_engine',20,80,1] #name, topSpeed, weight,FuelPerTick
        self.jaw = ['default_jaw', 20,10] #name, eatSpeed, weight
        self.tracks = ['default_tracks',1000] #name, weightCapacity
        self.posX = 300
        self.posY = 200
        self.velocity = [0,'SOUTH'] #speed, direction       


def text(font,text,center):
    textsurf = font.render(text,True,black)
    textrect = textsurf.get_rect()
    textrect.center = center
    display.blit(textsurf, textrect)

def rect(color, x, y, width, height):
    pygame.draw.rect(display,color,(x,y,width,height))

def render(image,x,y,w,h):
    image = pygame.transform.scale(image,(w,h))
    RECT = pygame.Rect(x,y,w,h)
    display.blit(image,RECT)

def circle(color, x, y, radius):
    pygame.draw.circle(display, color, (x,y), radius)   

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
                game()
            
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

def playerrender(xMov,Ymov,player,cameraX,cameraY):
    player.posX += xMov
    player.posY += Ymov
    
    direction = player.velocity[1]

    if direction == 'NORTH' or direction == 'SOUTH':
        render(default_tracks_NS,player.posX-cameraX,player.posY-cameraY,100,100)
    else:
        render(default_tracks_EW,player.posX-cameraX,player.posY-cameraY,100,100)
    if direction == 'NORTH' or direction == 'SOUTH':
        render(tier_NS,player.posX + 5-cameraX,player.posY + 5-cameraY,90,80)
    else:
        render(tier_EW,player.posX+ 5-cameraX,player.posY+ 5-cameraY,90,80)

    if player.posX > 600 + cameraX:
        cameraX += player.velocity[0]
    elif player.posX < 100+ cameraX:
        cameraX -= player.velocity[0]
    if player.posY > 400+ cameraY:
        cameraY += player.velocity[0]
    elif player.posY < 100+ cameraY:
        cameraY -= player.velocity[0]

    return cameraX,cameraY

def gamerender(xMov,yMov,player,cameraX,cameraY):
    render(grass,int(0-cameraX),int(0-cameraY),1000,1000)
    cameraX,cameraY = playerrender(xMov,yMov,player,cameraX,cameraY)
    

    pygame.display.update()
    return cameraX,cameraY

def invbutton(x,y):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+75 > mouse[0] > x and y+75 > mouse[1] > y:
        rect(lightgrey,x,y,75,75)
        if int(click[0]) == 1:
            return True
    else:
        rect(grey,x,y,75,75)

def inv(player):
    potato = False
    
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    os._exit(1)
                if event.key==pygame.K_i:
                    potato = True
            if event.type==pygame.KEYUP:
                pass
        if potato == True:
            break
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        rect(darkgrey,50,50,700,500)
        if 750>mouse[0]>700 and 100>mouse[1]>50:
            rect(lightgrey,700,50,50,50)
            if int(click[0]) == 1:
                break
        else:
            rect(grey,700,50,50,50)
    
        
        button1 = invbutton(55,50)
        button2 = invbutton(135,50)
        button3 = invbutton(215,50)
        button4 = invbutton(295,50)
        button5 = invbutton(375,50)
        button6 = invbutton(455,50)
        button7 = invbutton(535,50)
        button8 = invbutton(615,50)

        slot1 = invbutton(55,150)
        slot2 = invbutton(135,150)
        slot3 = invbutton(215,150)
        slot4 = invbutton(295,150)
        slot5 = invbutton(375,150)
        slot6 = invbutton(455,150)
        slot7 = invbutton(535,150)
        slot8 = invbutton(615,150)
        print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
        print('░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░')
        print('░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░')
        print('░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░')
        print('░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░')
        print('░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░')
        print('░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░')
        print('░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░')
        print('░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░')
        print('░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░')
        print('░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░')
        print('░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░')
        print('░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░')
        print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')

        pygame.display.update()
        
    
    

def game():
    Running = True
    moveUp=moveDown=moveLeft=moveRight=inventory=False
    north=south=east=west=0
    player = city()
    Clock = pygame.time.Clock()
    cameraX = 0
    cameraY = 0
    while Running:
        Clock.tick(20)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    os._exit(1)
                if event.key==pygame.K_UP:
                    moveUp=True
                if event.key==pygame.K_DOWN:
                    moveDown=True
                if event.key==pygame.K_LEFT:
                    moveLeft=True
                if event.key==pygame.K_RIGHT:
                    moveRight=True
                if event.key==pygame.K_i:
                    inv(player)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    moveUp=False
                if event.key==pygame.K_DOWN:
                    moveDown=False
                if event.key==pygame.K_LEFT:
                    moveLeft=False
                if event.key==pygame.K_RIGHT:
                    moveRight=False
        if moveUp and player.velocity[0] < 5:
            north+=1
        else:
            if north > 0:
                north -= 1
        if moveDown and player.velocity[0] < 5:
            south+=1
        else:
            if south > 0:
                south -= 1
        if moveLeft and player.velocity[0] < 5:
            west+=1
        else:
            if west > 0:
                west -=1
        if moveRight and player.velocity[0] < 5:
            east+=2
        else:
            if east > 0:
                east -=1

        xMov = east - west
        yMov = south - north
        player.velocity[0] = abs(xMov) + abs(yMov)
        print(str(player.velocity))
        
        if xMov > 0:
            player.velocity[1] = 'EAST'
        elif xMov < 0:
            player.velocity[1] = 'WEST'
        if yMov > 0:
            player.velocity[1] = 'SOUTH'
        elif yMov < 0:
            player.velocity[1] = 'NORTH'
        
        cameraX,cameraY = gamerender(xMov,yMov,player,cameraX,cameraY)

def gamemenu():
    pass


menu()

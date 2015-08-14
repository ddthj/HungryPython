import pygame
import time
import os
import random
# todo list:
#make function for buttons that works?
# finish minimenu for object targeting
# make bullet image and get gun shooting

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('HungryCities')
white = (255,255,255)
black = (0,0,0)
grey = (128,128,128)
lightgrey = (210,210,210)
darkgrey = (100,100,100)
menu1 = pygame.image.load('1.JPG')
grass = pygame.image.load('grass.jpg')
default_tracks_NS = pygame.image.load('tracksNS.png').convert_alpha()
default_tracks_EW = pygame.image.load('tracksEW.png').convert_alpha()
tier_NS = pygame.image.load('tierNS.png').convert_alpha()
tier_EW = pygame.image.load('tierEW.png').convert_alpha()

TitleText = pygame.font.Font('freesansbold.ttf',70)
SubText = pygame.font.Font('freesansbold.ttf', 20)
MiniText = pygame.font.Font('freesansbold.ttf',18)


display.fill(white)

class city:
    def __init__(self,engine,house,farm,Napoleon_Cannon):
        self.scrap = 0
        self.metal = 0
        self.inventory = [engine,house,farm,engine,engine,engine,Napoleon_Cannon,'none','none','none','none','none','none','none','none','none','none']
        self.fuel = 500
        self.food = 1000
        self.population = 0
        self.jaw = 5 #eatSpeed
        self.tracks = ['default_tracks',1000] #name, weightCapacity
        self.posX = 300
        self.posY = 200
        self.velocity = [0,'SOUTH'] #speed, direction
        self.topSpeed = 0
        self.popCapacity = 0
        self.weight = 0
        self.health = 1000
        self.target = 'none'

class engine:
    def __init__(self,speed,weight,fuel):
        self.name = ''
        self.topSpeed = speed
        self.weight = weight
        self.fuelUse = fuel
        self.pic = pygame.image.load('engine.png')
        self.value = 200
        self.health = 400

class house:
    def __init__(self,capacity):
        self.name = ''
        self.capacity = 10
        self.weight = 10
        self.pic = pygame.image.load('house.png')
        self.value = 70
        self.health = 100

class farm:
    def __init__(self):
        self.production = 11
        self.capacity = 400
        self.pic = pygame.image.load('farm.png')
        self.value = 30
        self.health = 50

class scrap:
    def __init__(self):
        self.amount = random.randint(50,200)
        self.x = random.randint(0,2000)
        self.y = random.randint(0,2000)
        self.pic = pygame.image.load('pile.png')
class cog:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.life = 10
        if z == 1:
            self.pic = pygame.image.load('cog.png')
        elif z == 2:
            self.pic = pygame.image.load('fuel.png')

class Napoleon_Cannon:
    def __init__(self):
        self.damage = 10
        self.health = 250
        self.fire_delay = 10
        self.pic = pygame.image.load('fuel.png')
        self.weight = 100
        self.value = 300

class Bullet1:
    def __init__(self,x,y,movx,movy):
        self.x = x
        self.y = y
        self.movx = movx
        self.movy = movy
        self.speed = 50
        
def text(font,text,center):
    textsurf = font.render(text,True,black)
    textrect = textsurf.get_rect()
    textrect.center = center
    display.blit(textsurf, textrect)

def text2(font,text,x,y):
    textsurf = font.render(text,True,black)
    textrect = textsurf.get_rect()
    textrect.x = x
    textrect.y = y
    display.blit(textsurf,textrect)
    
    

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
    inventory = player.inventory
    
    direction = player.velocity[1]
    if direction == 'NORTH' or direction == 'SOUTH':
        render(default_tracks_NS,player.posX-cameraX,player.posY-cameraY,100,100)       
    else:
        render(default_tracks_EW,player.posX-cameraX,player.posY-cameraY,120,100)
        
    if direction == 'NORTH' or direction == 'SOUTH':
        render(tier_NS,player.posX + 5-cameraX,player.posY -cameraY,90,80)
        
        if inventory[8] != 'none':
            render(inventory[8].pic,player.posX-cameraX+54,player.posY-cameraY-15,35,35)
        if inventory[9] != 'none':
            render(inventory[9].pic,player.posX-cameraX+54,player.posY-cameraY+3,35,35)
        if inventory[10] != 'none':
            render(inventory[10].pic,player.posX-cameraX+54,player.posY-cameraY+21,35,35)
        if inventory[11] != 'none':
            render(inventory[11].pic,player.posX-cameraX+54,player.posY-cameraY+39,35,35)
        if inventory[12] != 'none':
            render(inventory[12].pic,player.posX-cameraX+10,player.posY-cameraY-15,35,35)
        if inventory[13] != 'none':
            render(inventory[13].pic,player.posX-cameraX+10,player.posY-cameraY+3,35,35)
        if inventory[14] != 'none':
            render(inventory[14].pic,player.posX-cameraX+10,player.posY-cameraY+21,35,35)
        if inventory[15] != 'none':
            render(inventory[15].pic,player.posX-cameraX+10,player.posY-cameraY+39,35,35)
            
    else:
        render(tier_EW,player.posX-cameraX,player.posY-cameraY-5,120,80)
        
        if inventory[8] != 'none':
            render(inventory[8].pic,player.posX-cameraX+1,player.posY-cameraY-1,30,35)
        if inventory[9] != 'none':
            render(inventory[9].pic,player.posX-cameraX+30,player.posY-cameraY-1,30,35)
        if inventory[10] != 'none':
            render(inventory[10].pic,player.posX-cameraX+60,player.posY-cameraY-1,30,35)
        if inventory[11] != 'none':
            render(inventory[11].pic,player.posX-cameraX+90,player.posY-cameraY-1,30,35)
        if inventory[12] != 'none':
            render(inventory[12].pic,player.posX-cameraX+1,player.posY-cameraY+32,30,35)
        if inventory[13] != 'none':
            render(inventory[13].pic,player.posX-cameraX+30,player.posY-cameraY+32,30,35)
        if inventory[14] != 'none':
            render(inventory[14].pic,player.posX-cameraX+60,player.posY-cameraY+32,30,35)
        if inventory[15] != 'none':
            render(inventory[15].pic,player.posX-cameraX+90,player.posY-cameraY+32,30,35)

    if player.posX > 600 + cameraX:
        cameraX += player.velocity[0]
    elif player.posX < 100+ cameraX:
        cameraX -= player.velocity[0]
    if player.posY > 400+ cameraY:
        cameraY += player.velocity[0]
    elif player.posY < 100+ cameraY:
        cameraY -= player.velocity[0]

    return cameraX,cameraY

def gamerender(xMov,yMov,player,cameraX,cameraY,simobjects,minimin,mcordx,mcordy):
    render(grass,int(0-cameraX),int(0-cameraY),1000,1000)
    render(grass,int(1000-cameraX),int(0-cameraY),1000,1000)
    render(grass,int(0-cameraX),int(1000-cameraY),1000,1000)
    render(grass,int(1000-cameraX),int(1000-cameraY),1000,1000)

    for item in simobjects:
        if str(item).find('scrap') != -1:
            render(item.pic,int(item.x - cameraX),int(item.y - cameraY),int(100),int(100))
    
    
    cameraX,cameraY = playerrender(xMov,yMov,player,cameraX,cameraY)
    for item in simobjects:
        if str(item).find('cog') != -1:
            render(item.pic,int(item.x - cameraX),int(item.y - cameraY),int(50),int(50))

    if minimin == True:
        minimenu(mcordx,mcordy)
    

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

def invbutton2(x,y,z):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+100 > mouse[0] > x and y+30 > mouse[1] > y:
        rect(lightgrey,x,y,100,30)
        text2(MiniText,str(z),x,y)
        if int(click[0]) == 1:
            return True
    else:
        rect(grey,x,y,100,30)
        text2(MiniText,str(z),x,y)

def inv(player,simobjects):
    potato = False
    tier1button=True
    tier2button=craftbutton=button1=button2=button3=button4=button5=button6=button7=button8=button9=button10=button11=button12=button13=button14=button15=button16=False
    window = ''
    craftwindow = ''
    select = False
    selected = 0
    oldtime = time.time()
    while 1:
        newtime = time.time()
        player,simbojects,oldtime = gametick(player,simobjects,oldtime,newtime)
        scrap = player.scrap
        metal = player.metal
        inventory = player.inventory
        food = player.food
        pop = player.population
        fuel = player.fuel

        
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
            return inventory
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        rect(darkgrey,50,50,700,500)
        rect(grey,55,400,400,150)
        text2(MiniText,'Scrap: ',80,420)
        text2(MiniText,'Metal: ',80,440)
        text2(MiniText,'Fuel: ',80,460)
        text2(MiniText,'Food: ',80,480)
        text2(MiniText,'Population: ',80,500)

        text2(MiniText,str(scrap),200,420)
        text2(MiniText,str(metal),200,440)
        text2(MiniText,str(fuel),200,460)
        text2(MiniText,str(food),200,480)
        text2(MiniText,str(pop),200,500)        
        
        if 750>mouse[0]>700 and 100>mouse[1]>50:
            rect(lightgrey,700,50,50,50)
            if int(click[0]) == 1:
                return inventory
        else:
            rect(grey,700,50,50,50)
        
        button1 = invbutton(55,50)
        if inventory[0] != 'none':
            render(inventory[0].pic,55,50,75,75)
            
        button2 = invbutton(135,50)
        if inventory[1] != 'none':
            render(inventory[1].pic,135,50,75,75)
            
        button3 = invbutton(215,50)
        if inventory[2] != 'none':
            render(inventory[2].pic,215,50,75,75)
            
        button4 = invbutton(295,50)
        if inventory[3] != 'none':
            render(inventory[3].pic,295,50,75,75)
            
        button5 = invbutton(375,50)
        if inventory[4] != 'none':
            render(inventory[4].pic,375,50,75,75)
            
        button6 = invbutton(455,50)
        if inventory[5] != 'none':
            render(inventory[5].pic,455,50,75,75)
            
        button7 = invbutton(535,50)
        if inventory[6] != 'none':
            render(inventory[6].pic,535,50,75,75)
            
        button8 = invbutton(615,50)
        if inventory[7] != 'none':
            render(inventory[7].pic,615,50,75,75)

        if window == '1':
            button9 = invbutton(55,200)
            if inventory[8] != 'none':
                render(inventory[8].pic,55,200,75,75)
                
            button10 = invbutton(135,200)
            if inventory[9] != 'none':
                render(inventory[9].pic,135,200,75,75)
                
            button11 = invbutton(215,200)
            if inventory[10] != 'none':
                render(inventory[10].pic,215,200,75,75)
                
            button12 = invbutton(295,200)
            if inventory[11] != 'none':
                render(inventory[11].pic,295,200,75,75)
                
            button13 = invbutton(55,280)
            if inventory[12] != 'none':
                render(inventory[12].pic,55,280,75,75)
                
            button14 = invbutton(135,280)
            if inventory[13] != 'none':
                render(inventory[13].pic,135,280,75,75)
                
            button15 = invbutton(215,280)
            if inventory[14] != 'none':
                render(inventory[14].pic,215,280,75,75)
                
            button16 = invbutton(295,280)
            if inventory[15] != 'none':
                render(inventory[15].pic,295,280,75,75)
        elif window == 'craft':
            cat1 = invbutton2(55,130,'Craft')
            cat2 = invbutton2(160,130,'Upgrade')
            cat3 = invbutton2(265,130,'Smelt')
            if cat1 == True:
                craftwindow = '1'
            elif cat2 == True:
                craftwindow = '2'
            elif cat3 == True:
                craftwindow = '3'


            if craftwindow == '3':
                smelt = invbutton(55,170)
                if smelt == True and select == False:
                    limbo = inventory[16]
                    inventory[16] = 'none'
                    select = True
                    selected = 16
                    smelt = False
                    time.sleep(.1)
                if smelt == True and select == True:
                    inventory[selected] = inventory[16]
                    inventory[16] = limbo
                    select = False
                    time.sleep(.1)
                smeltscrap = invbutton2(55,260,'Recycle')
                if smeltscrap == True and inventory[16] != 'none':
                    smeltscrap == False
                    player.scrap += inventory[16].value
                    inventory[16] = 'none'
                if inventory[16] != 'none':
                    render(inventory[16].pic,55,170,75,75)
                

        if button1 == True and select == False:
            limbo = inventory[0]
            inventory[0] = 'none'
            select = True
            selected = 0
            button1 = False
            time.sleep(.1)
        elif button2 == True and select == False:
            limbo = inventory[1]
            inventory[1] = 'none'
            select = True
            selected = 1
            button2 = False
            time.sleep(.1)
        elif button3 == True and select == False:
            limbo = inventory[2]
            inventory[2] = 'none'
            select = True
            selected = 2
            button3 = False
            time.sleep(.1)
        elif button4 == True and select == False:
            limbo = inventory[3]
            inventory[3] = 'none'
            select = True
            selected = 3
            button4 = False
            time.sleep(.1)
        elif button5 == True and select == False:
            limbo = inventory[4]
            inventory[4] = 'none'
            select = True
            selected = 4
            button5 = False
            time.sleep(.1)
        elif button6 == True and select == False:
            limbo = inventory[5]
            inventory[5] = 'none'
            select = True
            selected = 5
            button6 = False
            time.sleep(.1)
        elif button7 == True and select == False:
            limbo = inventory[6]
            inventory[6] = 'none'
            select = True
            selected = 6
            button7 = False
            time.sleep(.1)
        elif button8 == True and select == False:
            limbo = inventory[7]
            inventory[7] = 'none'
            select = True
            selected = 7
            button8 = False
            time.sleep(.1)

        elif button9 == True and select == False:
            limbo = inventory[8]
            inventory[8] = 'none'
            select = True
            selected = 8
            button9 = False
            time.sleep(.1)
        elif button10 == True and select == False:
            limbo = inventory[9]
            inventory[9] = 'none'
            select = True
            selected = 9
            button10 = False
            time.sleep(.1)
        elif button11 == True and select == False:
            limbo = inventory[10]
            inventory[10] = 'none'
            select = True
            selected = 10
            button11 = False
            time.sleep(.1)
        elif button12 == True and select == False:
            limbo = inventory[11]
            inventory[11] = 'none'
            select = True
            selected = 11
            button12 = False
            time.sleep(.1)
        elif button13 == True and select == False:
            limbo = inventory[12]
            inventory[12] = 'none'
            select = True
            selected = 12
            button13 = False
            time.sleep(.1)
        elif button14 == True and select == False:
            limbo = inventory[13]
            inventory[13] = 'none'
            select = True
            selected = 13
            button14 = False
            time.sleep(.1)
        elif button15 == True and select == False:
            limbo = inventory[14]
            inventory[14] = 'none'
            select = True
            selected = 14
            button15 = False
            time.sleep(.1)
        elif button16 == True and select == False:
            limbo = inventory[15]
            inventory[15] = 'none'
            select = True
            selected = 15
            button16 = False
            time.sleep(.1)
        

                
        '''
        elif window == '2':
            slot9 = invbutton(55,200)
            slot10 = invbutton(135,200)
            slot11 = invbutton(215,200)
            slot12 = invbutton(295,200)
            slot13 = invbutton(55,280)
            slot14 = invbutton(135,280)
            slot15 = invbutton(215,280)
            slot16 = invbutton(295,280)
        '''



        if button1 == True and select == True:
            inventory[selected] = inventory[0]
            inventory[0] = limbo
            select = False
            time.sleep(.1)
        elif button2 == True and select == True:
            inventory[selected] = inventory[1]
            inventory[1] = limbo
            select = False
            time.sleep(.1)
        elif button3 == True and select == True:
            inventory[selected] = inventory[2]
            inventory[2] = limbo
            select = False
            time.sleep(.1)
        elif button4 == True and select == True:
            inventory[selected] = inventory[3]
            inventory[3] = limbo
            select = False
            time.sleep(.1)
        elif button5 == True and select == True:
            inventory[selected] = inventory[4]
            inventory[4] = limbo
            select = False
            time.sleep(.1)
        elif button6 == True and select == True:
            inventory[selected] = inventory[5]
            inventory[5] = limbo
            select = False
            time.sleep(.1)
        elif button7 == True and select == True:
            inventory[selected] = inventory[6]
            inventory[6] = limbo
            select = False
            time.sleep(.1)
        elif button8 == True and select == True:
            inventory[selected] = inventory[7]
            inventory[7] = limbo
            select = False
            time.sleep(.1)

        elif button9 == True and select == True:
            inventory[selected] = inventory[8]
            inventory[8] = limbo
            select = False
            time.sleep(.1)
        elif button10 == True and select == True:
            inventory[selected] = inventory[9]
            inventory[9] = limbo
            select = False
            time.sleep(.1)
        elif button11 == True and select == True:
            inventory[selected] = inventory[10]
            inventory[10] = limbo
            select = False
            time.sleep(.1)
        elif button12 == True and select == True:
            inventory[selected] = inventory[11]
            inventory[11] = limbo
            select = False
            time.sleep(.1)
        elif button13 == True and select == True:
            inventory[selected] = inventory[12]
            inventory[12] = limbo
            select = False
            time.sleep(.1)
        elif button14 == True and select == True:
            inventory[selected] = inventory[13]
            inventory[13] = limbo
            select = False
            time.sleep(.1)
        elif button15 == True and select == True:
            inventory[selected] = inventory[14]
            inventory[14] = limbo
            select = False
            time.sleep(.1)
        elif button16 == True and select == True:
            inventory[selected] = inventory[15]
            inventory[15] = limbo
            select = False
            time.sleep(.1)
        

        tier1button = invbutton(600,200)
        tier2button = invbutton(600,280)
        craftbutton = invbutton(600, 360)
        if tier1button == True:
            window = '1'
        elif tier2button == True:
            window = '2'
        elif craftbutton == True:
            window = 'craft'

        '''
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
        '''
        pygame.display.update()
        

def gametick(player,simobjects,oldtime,newtime):
    speed = 0
    popcap = 0
    fueluse = 0

    if oldtime + 1 < newtime:
        for i in range(8,15):
            #print(str(player.inventory[i]))
            if str(player.inventory[i]).find('engine') != -1:
                speed += player.inventory[i].topSpeed
                if player.velocity[0] > 0:
                    fueluse += player.inventory[i].fuelUse
            elif str(player.inventory[i]).find('house') != -1:
                popcap += player.inventory[i].capacity
            elif str(player.inventory[i]).find('farm') != -1:
                player.food += player.inventory[i].production
            elif str(player.inventory[i]).find('Napoleon_Cannon') != -1 and player.target != 'none':
                pass
                
                
        player.fuel -= fueluse
        player.topSpeed = speed
        player.popCapacity = popcap
        if player.fuel <= 0:
            player.fuel = 0
            player.topSpeed = 0

        if player.food > 2*player.population and player.population < player.popCapacity:
            player.population +=1
        if player.food < 2.9 * player.population and player.population >0:
            player.population -= 1
        if player.population > player.popCapacity:
            diff = player.population - player.popCapacity
            player.population -= diff
        if player.food - player.population > 0:
            player.food -= player.population
        else:
            player.food = 0
        oldtime = newtime

    for item in simobjects:
        if str(item).find('scrap') != -1:
            #print(item)
            if item.amount <= 0:
                simobjects.remove(item)
        if str(item).find('cog') != -1:
            item.y -= item.life
            item.x += random.randint(-3,3)
            item.life -= 1
            if item.life <= 0:
                simobjects.remove(item)

    return player,simobjects,oldtime

def simstart(simobjects):
    for i in range(0,20):
        name = str('pile'+str(i))
        name = scrap()
        simobjects.append(name)
    #print(str(simobjects))

    return simobjects
        
def eatfood(simobjects,player):
    playerX = player.posX
    playerY = player.posY
    speed = player.jaw
    for i in range(0,len(simobjects)):
        item = simobjects[i]
        if str(item).find('scrap') != -1:
            scrapX = item.x
            scrapY = item.y
            if scrapX + 100 > playerX > scrapX - 100 and scrapY + 100 > playerY > scrapY - 100:
                if item.amount >=speed:
                    item.amount -=speed
                    wat = random.randint(0,1)
                    if wat == 1:
                        player.scrap += speed
                        name = str('cog' + str(i))
                        name = cog(int(scrapX + 10),int(scrapY+10),1)
                        simobjects.append(name)
                    else:
                        player.fuel += speed
                        name = str('cog' + str(i))
                        name = cog(int(scrapX + 10),int(scrapY+10),2)
                        simobjects.append(name)
                else:
                    wat = random.randint(0,1)
                    if wat == 1:
                        player.scrap += item.amount
                        item.amount = 0
                        name = str('cog' + str(i))
                        name = cog(int(scrapX + 10),int(scrapY+10),1)
                        simobjects.append(name)
                    else:
                        player.fuel += item.amount
                        item.amount
                        name = str('cog' + str(i))
                        name = cog(int(scrapX + 10),int(scrapY+10),2)
                        simobjects.append(name)
    

def game():
    minimin = False
    simobjects = []
    simobjects = simstart(simobjects)
    Running = True
    moveUp=moveDown=moveLeft=moveRight=inventory=food=False
    north=south=east=west=0
    
    player = city(engine(5,100,5),house(10),farm(),Napoleon_Cannon())
    
    Clock = pygame.time.Clock()
    cameraX = 0
    cameraY = 0
    oldtime = time.time()
    while Running:
        Clock.tick(20)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                os._exit(1)
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
                    player.inventory = inv(player,simobjects)
                if event.key==pygame.K_f:
                    eatfood(simobjects,player)
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    moveUp=False
                if event.key==pygame.K_DOWN:
                    moveDown=False
                if event.key==pygame.K_LEFT:
                    moveLeft=False
                if event.key==pygame.K_RIGHT:
                    moveRight=False
        if moveUp and player.velocity[0] < player.topSpeed:
            north+=1
        else:
            if north > 0:
                north -= 1
        if moveDown and player.velocity[0] < player.topSpeed:
            south+=1
        else:
            if south > 0:
                south -= 1
        if moveLeft and player.velocity[0] < player.topSpeed:
            west+=1
        else:
            if west > 0:
                west -=1
        if moveRight and player.velocity[0] < player.topSpeed:
            east+=2
        else:
            if east > 0:
                east -=1

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        xMov = east - west
        yMov = south - north
        player.velocity[0] = abs(xMov) + abs(yMov)
        #print(str(player.velocity))
        
        if xMov > 0:
            player.velocity[1] = 'EAST'
        elif xMov < 0:
            player.velocity[1] = 'WEST'
        if yMov > 0:
            player.velocity[1] = 'SOUTH'
        elif yMov < 0:
            player.velocity[1] = 'NORTH'

        newtime = time.time()
        player,simobjects,oldtime = gametick(player,simobjects,oldtime,newtime)
        cameraX,cameraY = gamerender(xMov,yMov,player,cameraX,cameraY,simobjects,minimin,mcordx,mcordy)
        if minimin == True:
            minimenu(mouse)
        if int(click[0]) == 1:
            for item in simobjects:
                if item.x - 300 < int(mouse[0]) and item.x +300 > int(mouse[0]) and item.y - 300 < int(mouse[1]) and item.y + 300 > int(mouse[1]):
                    minimin = True
                    mcordx = mouse[0]
                    mcordy = mouse[1]
                else:
                    minimin = False

def gamemenu():
    pass

def minimenu(x,y):
    print('hi')
    rect(grey,x,y,200,200)
    


menu()

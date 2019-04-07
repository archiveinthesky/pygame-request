import pygame
import pyganim
import time

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
clock.tick(60)

bgread = open('background.txt', 'r')
bgtxt = bgread.read().splitlines()
bgs = []
for bgobt in bgtxt:
    bgs.append(pygame.image.load(bgobt))
obread = open('objects.txt', 'r')
obtxt = obread.read().splitlines()
obs = []
objs = []
for obt in obtxt:
    obs.append(pygame.image.load(obt))

global run
run = True




bgno = 0
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
run = 1
screenmode = 1



textfont = pygame.font.Font("texts/brushpen.ttc", 40)


class background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bgs[0].convert()
        self.image.set_alpha(255)
        self.image.set_colorkey(pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect()
        self.bgno = 2
        self.alpha = 255

    def update(self):
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def updateimage(self, currentbgno, blitx, blity, resizex, resizey):
        self.bgno = currentbgno
        if resizex == 0 and resizey == 0:
            self.image = bgs[self.bgno].convert()
        else:
            self.image = pygame.transform.scale(bgs[self.bgno],(resizex,resizey)).convert()
        self.alpha = 0
        self.image.set_colorkey(pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = blitx
        self.rect.y = blity

    def fadeout(self):
        self.alpha = self.alpha - 10
        self.update()

    def fadein(self):
        self.alpha = self.alpha + 10
        self.update()


bg = background()
bg.updateimage(2, 0, 0,0,0)
bg.alpha = 255


class objects(pygame.sprite.Sprite):
    def __init__(self, x, y, image, resizex, resizey):
        pygame.sprite.Sprite.__init__(self)
        if resizex == 0 and resizey == 0:
            self.image = obs[image].convert()
        else:
            self.image = pygame.transform.scale(obs[image], (resizex, resizey)).convert()
        self.image.set_alpha(0)
        self.image.set_colorkey(pygame.Color(255, 255, 255))
        self.alpha = 255
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False

    def update(self):
        self.detectmouse()
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def detectmouse(self):#''''''
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 :
            self.click = True

    def fadeout(self):
        self.alpha = self.alpha - 10
        self.update()

    def fadein(self):
        self.alpha = self.alpha + 10
        self.update()


startgame = objects(300, 650, 0, 510, 202)
objs.append(startgame)
startgame.alpha = 255

menu = objects(650,150,1,0,0)
menufullscreencheck = objects(950,425,2,0,0)
menufullscreencheckbox = objects(950,425,3,0,0)
menuleavegame = objects(680,550,4,450,180)




class textdisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.txtarray= []

    def load(self,doc):
        scriptread = open('texts/stage' + str(doc) + 'text.txt', 'r', encoding = 'utf8')
        global script
        script = scriptread.read().splitlines()
    def renew(self,line):
        self.txtarray = []
        self.line = script[line]
        self.current = 1
        self.goal = len(self.line)
    def update(self):
        if self.current == self.goal:
            screen.blit(textfont.render(self.line, False, (255, 255, 255)),(0,850))

        else:
            self.current = self.current + 1
            screen.blit(textfont.render(self.line[:self.current], False, (255, 255, 255)),(0,850))


txtdis = textdisplay()


txtdis.load(0)
txtdis.renew(0)
class Gamesys():
    def __init__(self):

        global textbar, objectbar, updatelist, fadelist, menushow
        textbar = background()
        textbar.updateimage(0, 0, 840,1920,250)

        objectbar = background()
        objectbar.updateimage(1, 0, 0,360,800)

        self.currentstage = '00'

        updatelist = []

        fadelist = []

        self.menushow = 0
        self.menuendexecute = False
        self.menufullscreen = False
        self.mouseclick = False

    def currentstagedetect(self):
        if self.currentstage == '00':
            updatelist.append(bg)
            updatelist.append(startgame)
            fadelist.append(bg)
            fadelist.append(startgame)
            if startgame.click == True:
                self.currentstage01()

    def update(self):
        for updateobjects in updatelist:
            updateobjects.update()
        if startgame.click == True and self.currentstage == '00':
            startgame.click = False
            self.currentstage01()
        if self.menushow == 1:
            self.menu()

    def fadeout(self):
        for fadeoutobjects in fadelist:
            fadeoutobjects.fadeout()

    def fadein(self):
        for fadeinobjects in fadelist:
            fadeinobjects.fadein()


    def fullscreen(self):
        menufullscreencheckbox.click = False
        updatelist.remove(menufullscreencheckbox)
        updatelist.append(menufullscreencheck)
        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    def resizeable(self):
        menufullscreencheckbox.click = False
        updatelist.remove(menufullscreencheck)
        updatelist.append(menufullscreencheckbox)
        screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)





    def menu(self):
        if self.menufullscreen == False and menufullscreencheckbox.click == True:
            menufullscreencheckbox.click = False
            self.menufullscreen = True
            menufullscreencheckbox.click = False
            self.fullscreen()

        if self.menufullscreen == True and menufullscreencheck.click == True:
            menufullscreencheck.click = False
            self.menufullscreen = False
            self.resizeable()
            menufullscreencheck.click = False
            time.sleep(0.2)
        if menuleavegame.click == True:
            run = False
            pygame.quit()
            exit()

    def whilerepeat(self):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouseclick = True
            else:
                self.mouseclick = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F10:
                    if self.menushow == 0:
                        updatelist.append(menu)
                        updatelist.append(menuleavegame)
                        if self.menufullscreen == False:
                            updatelist.append(menufullscreencheckbox)
                        elif self.menufullscreen == True:
                            updatelist.append(menufullscreencheck)
                        self.menu()
                        self.menushow = 1
                    elif self.menushow == 1:
                        self.menushow = 0
                        updatelist.remove(menu)
                        updatelist.remove(menuleavegame)
                        if self.menufullscreen == False:
                            updatelist.remove(menufullscreencheckbox)
                        elif self.menufullscreen == True:
                            updatelist.remove(menufullscreencheck)
                        self.whilerepeat()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
        system.update()
        pygame.display.update()





    def currentstage01(self):
        self.currentstage == '01'

        updatelist.remove(startgame)
        fadelist.remove(startgame)
        for i in range(30):
            screen.fill((0, 0, 0))
            self.fadeout()
            pygame.display.update()
        bg.updateimage(3, 0, 0 ,1920, 1080)
        for i in range(30):
            screen.fill((0, 0, 0))
            self.fadein()
            pygame.display.update()
        for i in range(300):
            self.whilerepeat()
        for i in range(30):
            screen.fill((0, 0, 0))
            self.fadeout()
            pygame.display.update()
        self.currentstage02()

    def currentstage02(self):
        self.currentstage = '02'
        bg.updateimage(4, 0, 0, 0, 0)
        updatelist.append(textbar)
        fadelist.append(textbar)

        for i in range(30):
            screen.fill((0, 0, 0))
            self.fadein()
            pygame.display.update()

        txtdis.renew(0)
        updatelist.append(txtdis)
        self.whilerepeat()
        while self.mouseclick == False:
            self.whilerepeat()
        txtdis.renew(1)
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        print('continue')
        bg.updateimage(5,0,0,0,0)
        for i in range(30):
            screen.fill((0,0,0))
            self.fadein()
            self.whilerepeat()
        txtdis.renew(2)

        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        txtdis.renew(3)
        print('3')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        for i in range(30):
            screen.fill((0,0,0))
            self.fadeout()
            self.whilerepeat()
        bg.updateimage(6,0,0,0,0)
        for i in range(30):
            screen.fill((0,0,0))
            self.fadein()
            self.whilerepeat()
        txtdis.renew(4)

        print('4')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        txtdis.renew(5)

        print('5')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        txtdis.renew(6)

        print('6')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()

        for i in range(30):
            screen.fill((0,0,0))
            self.fadeout()
            self.whilerepeat()
        bg.updateimage(7,0,0,0,0)
        for i in range(30):
            screen.fill((0,0,0))
            self.fadein()
            self.whilerepeat()
        txtdis.renew(4)


        txtdis.renew(7)
        print('7')
        time.sleep(0.2)
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()
        txtdis.renew(8)

        print('8')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        txtdis.renew(9)

        print('9')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()
        txtdis.renew(10)

        print('10')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()
        txtdis.renew(11)

        print('11')
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()
        txtdis.renew(12)
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()
        txtdis.renew(13)
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
                self.whilerepeat()
        txtdis.renew(14)
        self.whilerepeat()
        time.sleep(0.2)
        self.whilerepeat()
        while pygame.mouse.get_pressed()[0] == 0:
            self.whilerepeat()
        for i in range(30):
            screen.fill((0,0,0))
            self.fadeout()
            self.whilerepeat()
        bg.updateimage(8,0,0,0,0)

        self.currentstage = '10'
        self.currentstage10()

    def currentstage10(self):
        print('Entering Escape')
        bg.updateimage(9,0,0,0,0)
        updatelist.remove(textbar)
        updatelist.remove(txtdis)
        for i in range(25):
            screen.fill((0,0,0))
            bg.alpha = bg.alpha + i * 25.5
            self.whilerepeat()
        for i in range(180):
            self.whilerepeat()
        for i in range(25):
            screen.fill((0,0,0))
            bg.alpha = bg.alpha - i * 25.5
            self.whilerepeat()
        bg.alpha = -45
        textbar.alpha = -45
        objectbar.alpha = -45
        bg.updateimage(10,352,0,1568,840)

        fadelist.append(objectbar)
        for i in range(30):
            screen.fill((0,0,0))
            self.fadein()
            self.whilerepeat()
        updatelist.append(textbar)
        updatelist.append(txtdis)
        updatelist.append(objectbar)
        print(updatelist)
system = Gamesys()

system.currentstagedetect()
clock.tick(60)

while run:
    system.whilerepeat()
import pygame
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



bgno = 0
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
screenmode = 1

textfont = pygame.font.Font("texts/brushpen.ttc", 40)


'''pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play()'''
class background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bgs[0].convert()
        self.image.set_alpha(255)
        self.image.set_colorkey(pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect()
        self.bgno = 2
        self.alpha = 255
        self.responses = [1,1]

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
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = blitx
        self.rect.y = blity

    def detectmouse(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            self.hover = True
        else:
            self.hover = False

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
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.alpha = 255
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.click = False
        self.assignment = False
        self.responses = [1,1]
        self.hover = False

    def update(self):
        self.detectmouse()
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def detectmouse(self):#''''''
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            self.hover = True
        else:
            self.hover = False
        if self.rect.collidepoint(pygame.mouse.get_pos()) and system.mouseclick == True:
            self.click = True
        else:
            self.click = False

    def fadeout(self):
        self.alpha = self.alpha - 10
        self.update()

    def fadein(self):
        self.alpha = self.alpha + 10
        self.update()
    def assign(self, mission):
        self.assignment = mission
    def assignrespond(self, responcestart, responceend):
        self.responses = [responcestart, responceend]
    def respond(self):  
        txtdis.dpmultiline(self.responses[0], self.responses[1])
startgame = objects(300, 650, 0, 510, 202)
objs.append(startgame)
startgame.alpha = 255

menu = objects(550,150,1,766,887)
menufullscreencheck = objects(1010,455,2,100,80)
menufullscreencheckbox = objects(1010,455,3,80,80)


menuleavegame = objects(730,550,4,450,180)




class textdisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.txtarray= []
        self.passwordmode = False
        self.lines = 1
        self.currentdisplayline = 1
    def load(self,doc):
        scriptread = open('texts/stage' + str(doc) + 'text.txt', 'r', encoding = 'utf8')
        global script
        script = scriptread.read().splitlines()
    
    
    def dpmultiline(self, responcestart, responceend):
        self.lines = (responceend - responcestart) + 1
        for i in range(self.lines):
            txtdis.renew(i + responcestart)
            system.waituntilmouserelease()
        txtdis.renew(1)

    def renew(self,line):
        self.txtarray = []
        self.line = script[line]
        self.current = 1
        self.goal = len(self.line)
    
    def update(self):
        if self.current == self.goal:
            screen.blit(textfont.render(self.line, False, (150, 0, 0)),(0,850))

        else:
            self.current = self.current + 1
            screen.blit(textfont.render(self.line[:self.current], False, (150, 0, 0)),(0,850))

    def simplerender(self, x, y, r, g, b, text):
        screen.blit(textfont.render(str(text), False, (r, g, b)),(x,y))



txtdis = textdisplay()


txtdis.load(0)
txtdis.renew(0)

class enterpassclass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enterpress = False
        self.entered = ''
        self.enterkey = ''
        self.numbers = [0,1,2,3,4,5,6,7,8,9]
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def unlock(self, anwser):
        self.enterpress = False
        self.entered = ''
        self.enterkey = ''
        while self.enterpress == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.check(event.key)
            system.whilerepeat()
        updatelist.remove(enterpass)
        if self.entered == str(anwser):
            return 'pass'
        else:
            return 'notpass'
        
        pass
    def update(self):
        txtdis.simplerender(1000,700,255,255,255, self.entered)
    def check(self,key):
        self.enterkey = ''
        if key == 13 or key == 271:
            print('enter')
            self.enterpress = True
        elif key >=48 and key <= 57:
            self.enterkey = self.numbers[key-48]
        elif key >=256 and key <= 265:
            self.enterkey = self.numbers[key-256]
        elif key >= 97 and key <= 122:
            self.enterkey = self.letters[key-97]
        elif key == 8:
            self.entered = self.entered[:len(self.enterkey)-1]
        self.entered = str(self.entered) + str(self.enterkey)

enterpass = enterpassclass()
class diarypagedisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.currentdiaryroom = []
    def loadroom(self,room):

        if room == 'madamroom':
            for i in range(6):
                pic = pygame.image.load('backgrounds/diarytext/' + str(i+1) + '.png')

              
                self.currentdiaryroom.append(pygame.transform.scale(pic,(1000,1000*pic.get_rect().size[1]//pic.get_rect().size[0])))
        elif room == 'dukeroom':
            pic = pygame.image.load('backgrounds/diarytext/' + str(1) + '.png')
            self.currentdiaryroom.append((pygame.transform.scale(pic,(1000,1000*pic.get_rect().size[1]//pic.get_rect().size[0]))))
        
    def updatepage(self, pagenum):
        print('length' + str(len(self.currentdiaryroom)))
        self.image = self.currentdiaryroom[pagenum-1]
    def update(self):
        screen.blit(self.image, (550,200))
diarypgdp = diarypagedisplay()



class Gamesys():
    def __init__(self):

        global textbar, objectbar, updatelist, fadelist, currentdisplayscenes, currentdisplaybuttons, currentsceneobjects, diaries, diaryleftarrow, diaryrightarrow, enterpasslist
        global madamroomicon, dukeroomicon, woodendooricon, madambox, madamlockbox1, madamlockbox2, madamroomobjects , woodendoorobjects, madamroomdiarycover, madamroomdiaryopen, dukeroomobjects, dukeroomdiarycover, dukeroomdiaryopen, dukeroomlockobjects #stage1
        global dukestudylockobjects, dukestudyobjects
        self.currentdisplayscene =[]
        textbar = background()
        textbar.updateimage(0, 0, 840,1920,250)

        objectbar = background()
        objectbar.updateimage(1, 0, 0,360,800)


        

        self.diarypage = 1
        self.dukeroomlock = True
        self.dukestudylock = True

        self.currentstage = '00'

        updatelist = []

        fadelist = []

        currentdisplayscenes = []
        currentdisplaybuttons = []
        currentsceneobjects = []
        woodendoorobjects = []
        dukeroomobjects = []
        dukeroomlockobjects = []
        dukestudylockobjects = []
        dukestudyobjects = []
        enterpasslist = []


        madamroomicon = objects(0,800,5,80,45)
        dukeroomicon = objects(80, 800, 17, 80, 45)
        woodendooricon = objects(160,800,6,80,45)
        madamroomicon.assign('swapmadamroom')
        dukeroomicon.assign('swapdukeroom')
        woodendooricon.assign('swapwoodendoor')
        currentdisplaybuttons.append(madamroomicon)
        currentdisplaybuttons.append(dukeroomicon)
        currentdisplaybuttons.append(woodendooricon)


        
        dukeroomdiarycover = objects(1200,450,13,100,170)
        dukeroomdiaryopen = objects(400, 50, 18, 1300, 800)
        dukeroomobjects.append(dukeroomdiarycover)

        madambox = objects(850,400,7,300,300)
        madambox.assignrespond(2,2)
        madamlockbox1 = objects(1550,430,8,90,45)
        madamlockbox1.assignrespond(3,3)
        madamlockbox2 = objects(1750,430,9,90,45)
        madamlockbox2.assignrespond(4,4)
        madamroomdiarycover = objects(900, 300, 12, 100, 170)
        madamroomdiaryopen = objects(400, 50, 14, 1300, 800)
        madamroomobjects = []
        madamroomobjects.append(madambox)
        madamroomobjects.append(madamlockbox1)
        madamroomobjects.append(madamlockbox2)
        madamroomobjects.append(madamroomdiarycover)
        


        diaryleftarrow = objects(400, 700, 15, 200, 150)
        diaryrightarrow = objects(1500, 700, 16, 200, 150)


        diaries = []
        diaries.append(madamroomdiarycover)
        diaries.append(dukeroomdiarycover)


        self.currentdisplayscene = madamroomobjects

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

    def update(self):
        screen.fill((0,0,0))
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
                if event.key == pygame.K_ESCAPE:
                    print('Escape')
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
                pygame.quit()
                exit()

        for currentdisplayscenesobject in currentdisplaybuttons:
            if currentdisplayscenesobject.click == True:
                currentdisplayscenesobject.click = False
                self.roomtemp = currentdisplayscenesobject.assignment
                self.execute('swapscene', currentdisplayscenesobject.assignment)
                    
               

        for currentdiaries in diaries:
            if currentdiaries.click == True:
                print('diaries')
                print(currentdiaries.click)
                currentdiaries.click = False
                print(currentdiaries.click)
                self.diary(currentdiaries)
                                

        self.update()
        pygame.display.update()


    def execute(self, type, mission):
        if type == 'swapscene':
            while self.mouseclick != False:
                self.whilerepeat()
            for i in self.currentdisplayscene:
                print(i)
                updatelist.remove(i)
            if mission == 'swapmadamroom':
                bg.updateimage(10,352,0,1568,840)
                bg.alpha = 255
                self.currentdisplayscene = madamroomobjects
                for i in madamroomobjects:
                    updatelist.append(i)
                self.madamroom()
            elif mission == 'swapdukeroom':
                if self.dukeroomlock == True: 
                    time.sleep(0.2)
                    bg.updateimage(12, 352, 0, 1568, 840)
                    bg.alpha = 255
                    self.currentdisplayscene = dukeroomlockobjects
                    for i in dukeroomlockobjects:
                        updatelist.append(i)
                    self.dukeroomlocked()
                else:
                    bg.updateimage(14, 352, 0, 1568, 840)
                    bg.alpha = 255
                    self.currentdisplayscene = dukeroomobjects
                    for i in dukeroomobjects:
                        updatelist.append(i)
                    self.dukeroom() 
            elif mission == 'swapdukestudy':
                if self.dukestudylock == True: 
                    time.sleep(0.2)
                    bg.updateimage(12, 352, 0, 1568, 840)
                    bg.alpha = 255
                    self.currentdisplayscene = dukestudylockobjects
                    for i in dukestudylockobjects:
                        updatelist.append(i)
                    self.dukestudylocked()
                else:
                    bg.updateimage(15, 352, 0, 1568, 840)
                    bg.alpha = 255
                    self.currentdisplayscene = dukestudyobjects
                    for i in dukestudyobjects:
                        updatelist.append(i)
                    self.dukestudy() 
            elif mission == 'swapwoodendoor':
                bg.updateimage(13,352,0,1568,840)
                bg.alpha = 255
                self.currentdisplayscene = woodendoorobjects
                self.update()
                pygame.display.update()
                self.woodendoor()

        elif type == 'enterpass':

            while self.mouseclick != False:
                self.whilerepeat()
            for i in self.currentdisplayscene:
                updatelist.remove(i)
            bg.updateimage(11, 352, 0, 1568, 840)
            bg.alpha = 255
            self.currentdisplayscene = enterpasslist
            updatelist.append(enterpass)
            if enterpass.unlock(mission) == 'pass':
                return(True)
            else:
                return(False)
            
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
        for i in range(0):
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
        #down to lines are from current stage 02
        txtdis.renew(15)
        updatelist.append(txtdis)
        #at the bottom
        self.currentstage = '10'
        self.currentstage10()
    
    def currentstage10(self):
        print('Entering Escape')
        txtdis.load(1)
        bg.updateimage(9,0,0,0,0)
        updatelist.remove(textbar)
        updatelist.remove(txtdis)
        for i in range(25):
            screen.fill((0,0,0))
            bg.alpha = bg.alpha + i * 25.5
            self.whilerepeat()
        for i in range(0):
            self.whilerepeat()
        for i in range(25):
            screen.fill((0,0,0))
            bg.alpha = bg.alpha - i * 25.5
            self.whilerepeat()
        bg.alpha = -45
        textbar.alpha = -45
        objectbar.alpha = -45
        madamroomicon.alpha = -45
        woodendooricon.alpha = -45
        bg.updateimage(10,352,0,1568,840)
        txtdis.load(1)
        txtdis.renew(1)
        
        print('currentstage10')
        self.currentstage11()
    
    def currentstage11(self):

        updatelist.append(textbar)
        updatelist.append(objectbar)
        self.updateicons()
        fadelist.append(textbar)
        fadelist.append(objectbar)
        fadelist.append(madamroomicon)
        fadelist.append(woodendooricon)
        for i in range(30):
            screen.fill((0,0,0))
            self.fadein()
            self.whilerepeat()

        for i in self.currentdisplayscene:
            updatelist.append(i)
        print(updatelist)
        updatelist.append(txtdis)
        print('currentstage11')
        #self.currentstage12() #for debugging only
        self.execute('swapscene', 'swapmadamroom')
    
    def currentstage12(self):
        #unlocked duke room
        self.currentstage = '12'
        self.dukeroomlock = False
        global dukestudyicon
        dukestudyicon = objects(240,800,19,80,45)
        dukestudyicon.assign('swapdukestudy')
        updatelist.append(dukestudyicon)
        currentdisplaybuttons.append(dukestudyicon)
        self.execute('swapscene', 'swapdukeroom')
    
    def currentstage13(self):
        #unlocked dukestudy
        self.currentstage = '13'
        self.dukestudylock = False
        self.execute('swapscene', 'swapdukestudy')
    def updateicons(self):
        for i in currentdisplaybuttons:
            updatelist.append(i)

    def waituntilmouserelease(self):
        time.sleep(0.2)
        while self.mouseclick == True:
            self.whilerepeat()
        while self.mouseclick == False:
            self.whilerepeat()
        
    def madamroom(self):
        print('madamroom')
        while True:
            self.whilerepeat()

            if self.currentdisplayscene != madamroomobjects:
                break
            for i in madamroomobjects:
                if i.click == True:
                    print('True')
                    i.respond()

                    #print('false respond')
    def dukeroomlocked(self):

        while True:
            self.whilerepeat()
            bg.detectmouse()
            if bg.hover == True and self.mouseclick == True:
                txtdis.dpmultiline(5,7)
                if self.execute('enterpass', 128) == True:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(8,8)
                    self.currentstage12()
                else:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(9,9)
                    self.execute('swapscene', 'swapdukeroom')

            if self.currentdisplayscene != dukeroomlockobjects:
                break

    def dukeroom(self):
        while True:
            self.whilerepeat()
            if self.currentdisplayscene != dukeroomobjects:
                break
            for i in dukeroomobjects:
                if i.click == True:
                    print('True')
                    i.respond()

    def dukestudylocked(self):
        while True:
            self.whilerepeat()
            bg.detectmouse()
            if bg.hover == True and self.mouseclick == True:
                txtdis.dpmultiline(12,12)
                if self.execute('enterpass', 69) == True:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(13,13)
                    self.currentstage13()
                else:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(9,9)
                    self.execute('swapscene', 'swapdukestudy')

            if self.currentdisplayscene != dukestudylockobjects:
                break        

    def dukestudy(self):
        while True:
            self.whilerepeat()
            if self.currentdisplayscene != dukestudyobjects:
                break
            for i in dukestudyobjects:
                if i.click == True:
                    print('True')
                    i.respond()
    

    def woodendoor(self):
        while True:
            self.whilerepeat()
            bg.detectmouse()
            if bg.hover == True and self.mouseclick == True:
                txtdis.dpmultiline(10,11)            
            if self.currentdisplayscene != woodendoorobjects:
                break
    def diary(self, room):
        if room == madamroomdiarycover:
  
            updatelist.append(madamroomdiaryopen)
            updatelist.append(diaryleftarrow)
            updatelist.append(diaryrightarrow)
            diarypgdp.currentdiaryroom = []
            diarypgdp.loadroom('madamroom')
            diarypgdp.updatepage(1)
            updatelist.append(diarypgdp)
            time.sleep(0.2)
            while True:
                self.whilerepeat()
                if diaryrightarrow.click == True:
                    if self.diarypage == 5:
                        self.diarypage = 0
                    else:
                        self.diarypage = self.diarypage + 1
                    print(self.diarypage)
                    while self.mouseclick != False:
                        self.whilerepeat()
                    diarypgdp.updatepage(self.diarypage)
                elif diaryleftarrow.click == True:
                    if self.diarypage == 0:
                        self.diarypage = 5
                    else:
                        self.diarypage = self.diarypage - 1
                    print(self.diarypage)
                    while self.mouseclick != False:
                        self.whilerepeat()
                    diarypgdp.updatepage(self.diarypage)
                if self.mouseclick == True and madamroomdiaryopen.hover == False: 
                    break
            
            updatelist.remove(madamroomdiaryopen)  
            updatelist.remove(diaryleftarrow)
            updatelist.remove(diaryrightarrow)
            updatelist.remove(diarypgdp)
        if room == dukeroomdiarycover:
  
            updatelist.append(dukeroomdiaryopen)
            time.sleep(0.2)
            updatelist.append(diarypgdp)
            diarypgdp.currentdiaryroom = []
            diarypgdp.loadroom('dukeroom')
            diarypgdp.updatepage(0)
            while True:
                self.whilerepeat()
                if self.mouseclick == True and dukeroomdiaryopen.hover == False: 
                    break

            updatelist.remove(dukeroomdiaryopen)
            updatelist.remove(diarypgdp)  






system = Gamesys()

system.currentstagedetect()
clock.tick(60)
while True:
    system.whilerepeat()

    #vscode is testing
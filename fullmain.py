import pygame
import time
import screenctrl
import classes
import commonvar


pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
clock.tick(60)


bgno = 0
screenmode = 1
screen = commonvar.bridge.getvar('screen')



pygame.mixer.init()
pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.play()


bg = classes.background()
bg.updateimage(2, 0, 0, 0, 0)
bg.alpha = 255


startgame = classes.objects(300, 650, 0, 510, 202)
startgame.alpha = 255

txtdis = commonvar.bridge.getvar('txtdis')


txtdis.load(0)
txtdis.renew(0)

class enterpassclass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enterpress = False
        self.close = classes.objects(1691,3,24,91,141)
        self.entered = ''
        self.enterkey = ''
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def unlock(self, anwser):
        self.enterpress = False
        self.entered = ''
        self.enterkey = ''
        updatelist.append(self.close)
        while self.enterpress == False and self.close.click == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.check(event.key)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    system.mouseclick = True
                else:
                    system.mouseclick = False
            system.whilerepeat()
            print(str(self.close.hover) + ' hover')
            print(self.close.click)
            if self.close.hover == True:
                print('yes')
            print(system.mouseclick)
        updatelist.remove(enterpass)
        updatelist.remove(self.close)
        if self.entered == str(anwser):
            return 'pass'
        else:
            return 'notpass'
        
        pass
    def update(self):
        txtdis.simplerender(1000, 700, 255, 255, 255, self.entered)
    def check(self, key):
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
    def loadroom(self, room):

        if room == 'madamroom':
            for i in range(6):
                pic = pygame.image.load('backgrounds/diarytext/' + str(i+1) + '.png')

              
                self.currentdiaryroom.append(pygame.transform.scale(pic, (1000, 1000*pic.get_rect().size[1]//pic.get_rect().size[0])))
        elif room == 'dukeroom':
            pic = pygame.image.load('backgrounds/diarytext/dukediary.png' )
            self.currentdiaryroom.append((pygame.transform.scale(pic, (1000, 1000*pic.get_rect().size[1]//pic.get_rect().size[0]))))
        elif room == 'leaderroom':
            pic = pygame.image.load('backgrounds/diarytext/leadderroom.png' )
            self.currentdiaryroom.append((pygame.transform.scale(pic, (1000, 1000*pic.get_rect().size[1]//pic.get_rect().size[0]))))
    def updatepage(self, pagenum):
        print('length' + str(len(self.currentdiaryroom)))
        self.image = self.currentdiaryroom[pagenum-1]
    def update(self):
        screen.blit(self.image, (550, 200))
diarypgdp = diarypagedisplay()



class Gamesys():
    def __init__(self):

        global textbar, objectbar, updatelist, fadelist, currentdisplayscenes, currentdisplaybuttons, currentsceneobjects, diaries, diaryleftarrow, diaryrightarrow, enterpasslist
        global madamroomicon, dukeroomicon, woodendooricon, madambox, madamlockbox1, madamlockbox2, madamroomobjects , woodendoorobjects, madamroomdiarycover, madamroomdiaryopen, dukeroomobjects, dukeroomdiarycover, dukeroomdiaryopen, dukeroomlockobjects #stage1
        global dukestudylockobjects, dukestudyobjects, dukestudyaxe, leaderroomobjects, leaderroomdiarycover, leaderroomdiaryopen
        self.currentdisplayscene =[]
        textbar = classes.background()
        textbar.updateimage(0, 0, 840, 1920, 250)

        objectbar = classes.background()
        objectbar.updateimage(1, 0, 0, 360, 800)


        self.mousefollowbg =  pygame.transform.scale(pygame.image.load('objects/cursor/background.png'),(175,50))

        self.diarypage = 1
        self.dukeroomlock = True
        self.dukestudylock = True
        self.getaxe = False

        self.currentstage = '00'

        updatelist = []
        commonvar.bridge.setvar('updatelist', updatelist)
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
        leaderroomobjects = []


        madamroomicon = classes.objects(0, 800, 5, 80, 45)
        dukeroomicon = classes.objects(80, 800, 17, 80, 45)
        woodendooricon = classes.objects(160, 800, 6, 80, 45)
        madamroomicon.assign('swapmadamroom')
        dukeroomicon.assign('swapdukeroom')
        woodendooricon.assign('swapwoodendoor')
        currentdisplaybuttons.append(madamroomicon)
        currentdisplaybuttons.append(dukeroomicon)
        currentdisplaybuttons.append(woodendooricon)


        #dukeroomstuff
        dukeroomdiarycover = classes.objects(1200, 450, 13, 100, 170)
        dukeroomdiaryopen = classes.objects(400, 50, 18, 1300, 800)
        dukeroomobjects.append(dukeroomdiarycover)
        #madamroom stuff
        madambox = classes.objects(850, 400, 7, 300, 300)
        madambox.assignrespond(2, 2)
        madamlockbox1 = classes.objects(1550, 430, 8, 90, 45)
        madamlockbox1.assignrespond(3, 3)
        madamlockbox2 = classes.objects(1750, 430, 9, 90, 45)
        madamlockbox2.assignrespond(4, 4)
        madamroomdiarycover = classes.objects(900, 300, 12, 100, 170)
        madamroomdiaryopen = classes.objects(400, 50, 14, 1300, 800)
        madamroomobjects = []
        madamroomobjects.append(madambox)
        madamroomobjects.append(madamlockbox1)
        madamroomobjects.append(madamlockbox2)
        madamroomobjects.append(madamroomdiarycover)
        #dukestudystuff
        dukestudyaxe = classes.objects(1006,518,20,82,150)        
        dukestudyobjects.append(dukestudyaxe)
        dukestudyaxe.assignrespond(29,29)

        leaderroomdiarycover = classes.objects(733, 475, 22, 100, 170)
        leaderroomdiaryopen = classes.objects(400, 50, 23, 1300, 800)
        leaderroomobjects.append(leaderroomdiarycover)

        diaryleftarrow = classes.objects(400, 700, 15, 200, 150)
        diaryrightarrow = classes.objects(1500, 700, 16, 200, 150)


        diaries = []
        diaries.append(madamroomdiarycover)
        diaries.append(dukeroomdiarycover)
        #diaries.append(leaderroomdiarycover)

        self.currentdisplayscene = madamroomobjects

        self.menushow = 0
        self.menuendexecute = False
        self.menufullscreen = False
        self.mouseclick = False


    def update(self):
        screen.fill((0, 0, 0))
        for updateobjects in updatelist:
            updateobjects.update()
        commonvar.bridge.updatevar('updatelist', updatelist)

        if self.menushow == 1:
            screenctrl.controls.menu(updatelist)
    def fadeout(self):
        for fadeoutobjects in fadelist:
            fadeoutobjects.fadeout()

    def fadein(self):
        for fadeinobjects in fadelist:
            fadeinobjects.fadein()




    def eventupdate(self):
        screenctrl.controls.eventupdate(updatelist)

    def whilerepeat(self):
        clock.tick(60)
        self.eventupdate()

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
        self.mousefollow()
        pygame.display.update()


    def execute(self, type, mission):
        if type == 'swapscene':
            while self.mouseclick != False:
                self.whilerepeat()
            for i in self.currentdisplayscene:
                print(i)
                updatelist.remove(i)
            if mission == 'swapmadamroom':
                bg.updateimage(10, 352, 0, 1568, 840)
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
                bg.updateimage(13, 352, 0, 1568, 840)
                bg.alpha = 255
                self.currentdisplayscene = woodendoorobjects
                self.update()
                pygame.display.update()
                self.woodendoor()
            elif mission == 'swapleaderroom':
                bg.updateimage(17, 352, 0, 1568, 840)
                bg.alpha=255
                self.currentdisplayscene = leaderroomobjects
                self.leaderroom()

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
            
    

    

    def updateicons(self):
        for i in currentdisplaybuttons:
            updatelist.append(i)

    def waituntilmouserelease(self):
        time.sleep(0.2)
        while commonvar.bridge.getvar('mouseclick') == True:
            self.whilerepeat()
        while commonvar.bridge.getvar('mouseclick') == False:
            self.whilerepeat()
        
    def mousefollow(self):
        screen.blit(self.mousefollowbg, (int(pygame.mouse.get_pos()[0]),int(pygame.mouse.get_pos()[1])))
        txtdis.simplerender(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],255,255,255,str(str(pygame.mouse.get_pos()[0]) + "," + str(pygame.mouse.get_pos()[1])))


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
                txtdis.dpmultiline(5, 7)
                if self.execute('enterpass', '0128') == True:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(8, 8)
                    stage1.currentstage12()
                else:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(9, 9)
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
                txtdis.dpmultiline(12, 12)
                if self.execute('enterpass', '0609') == True:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(13, 13)
                    stage1.currentstage13()
                else:
                    bg.updateimage(12, 352, 0, 1568, 840)
                    self.whilerepeat()
                    txtdis.dpmultiline(9, 9)
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
                    if i == dukestudyaxe and self.getaxe == False:
                        self.getaxe = True
                        self.objectbaraxe = classes.objects(30,30,20,82,150)  
                        updatelist.append(self.objectbaraxe)
                        updatelist.remove(dukestudyaxe)
                        
                        dukestudyobjects.remove(dukestudyaxe)
                    print('True')
                    i.respond()

    

    def woodendoor(self):
        
        self.waituntilmouserelease()
        if self.getaxe == True:
            self.getaxe = 'None'
            stage1.currentstage14()
        elif self.getaxe == False: 
            while True:
                self.whilerepeat()
                bg.detectmouse()
                if bg.hover == True and self.mouseclick == True:
                    txtdis.dpmultiline(10, 11)            
                if self.currentdisplayscene != woodendoorobjects:
                    break
    def leaderroom(self):
        for i in leaderroomobjects:
            updatelist.append(i)
        while leaderroomdiarycover.click != True:
            self.whilerepeat()
        self.diary(leaderroomdiarycover)
        self.ending()
            
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
        if room == leaderroomdiarycover:
            updatelist.append(leaderroomdiaryopen)
            time.sleep(0.2)
            updatelist.append(diarypgdp)
            diarypgdp.currentdiaryroom = []
            diarypgdp.loadroom('leaderroom')
            diarypgdp.updatepage(0)
            while True:
                self.whilerepeat()
                if self.mouseclick == True and dukeroomdiaryopen.hover == False: 
                    break
            updatelist.remove(leaderroomdiaryopen)
            updatelist.remove(diarypgdp)  
    def wait(self, secs):
        waitsecs = float(secs)
        for i in range(secs * 30):
            self.whilerepeat()
    def ending(self):
        endingupdate = classes.background()
        for i in range(10):
            for deleteing in updatelist:
                updatelist.remove(deleteing)
        print(updatelist)
        tobecontinued = classes.background()
        print(updatelist)
        tobecontinued.updateimage(25,1500,800,400,280)
        tobecontinued.alpha = 255
        updatelist.append(endingupdate)
        updatelist.append(tobecontinued)
        endingupdate.alpha = 0
        screen.fill((0,0,0))
        self.whilerepeat()
        pygame.display.update()
        for i in range(7):
            endingupdate.updateimage(i + 18, 0,0,1920,1080)
            endingupdate.alpha = 0
            for i in range(25):
                endingupdate.alpha += 25
                screen.fill((0,0,0))
                self.eventupdate()
                self.update()
                pygame.display.update()
            self.wait(3)
            for i in range(25):
                endingupdate.alpha -= 25
                screen.fill((0,0,0))
                self.eventupdate()
                self.update()
                pygame.display.update()
        endingupdate.updateimage(2,0,0,1920,1080)
        for i in range(25):
            endingupdate.alpha += 25
            screen.fill((0,0,0))
            self.eventupdate()
            self.update()
            pygame.display.update()
        while True:
            system.whilerepeat()



class Stage0():
    def __init__(self):
        updatelist.append(bg)
        updatelist.append(startgame)
        fadelist.append(bg)
        fadelist.append(startgame)
    def currentstage00(self):
        bg.updateimage(2,0,0,1920,1080)
        bg.alpha = 255
        print(updatelist)
        while startgame.click == False:
            system.whilerepeat()
        startgame.click = False
        self.currentstage01()
    def currentstage01(self):
        system.currentstage == '01'

        updatelist.remove(startgame)
        fadelist.remove(startgame)
        for i in range(30):
            screen.fill((0, 0, 0))
            system.fadeout()
            pygame.display.update()
        bg.updateimage(3, 0, 0 , 1920, 1080)
        for i in range(30):
            screen.fill((0, 0, 0))
            system.fadein()
            pygame.display.update()
        print(bg.alpha)
        system.waituntilmouserelease()
        for i in range(30):
            screen.fill((0, 0, 0))
            system.fadeout()
            pygame.display.update()
        
        self.currentstage02()

    def currentstage02(self):
        system.currentstage = '02'
        bg.updateimage(4, 0, 0, 0, 0)
        updatelist.append(textbar)
        fadelist.append(textbar)
        #down to lines are from current stage 02
        txtdis.renew(15)
        updatelist.append(txtdis)
        for i in range(30):
            screen.fill((0, 0, 0))
            system.fadein()
            pygame.display.update()
        #cutted into main
        system.waituntilmouserelease()
        txtdis.renew(0)
        system.waituntilmouserelease()
        txtdis.renew(1)
        time.sleep(0.2)
        system.waituntilmouserelease()
        print('continue')
        bg.updateimage(5,0,0,0,0)
        for i in range(30):
            screen.fill((0,0,0))
            system.fadein()
            system.whilerepeat()
        txtdis.renew(2)

        system.waituntilmouserelease()
        txtdis.renew(3)

        system.whilerepeat()
        time.sleep(0.2)
        system.whilerepeat()
        system.waituntilmouserelease()
        for i in range(30):
            screen.fill((0,0,0))
            system.fadeout()
            system.whilerepeat()
        bg.updateimage(6,0,0,0,0)
        for i in range(30):
            screen.fill((0,0,0))
            system.fadein()
            system.whilerepeat()
        txtdis.renew(4)


        system.waituntilmouserelease
        
        txtdis.renew(5)

        system.waituntilmouserelease()
        txtdis.renew(6)


        system.waituntilmouserelease()

        for i in range(30):
            screen.fill((0,0,0))
            system.fadeout()
            system.whilerepeat()
        bg.updateimage(7,0,0,0,0)
        for i in range(30):
            screen.fill((0,0,0))
            system.fadein()
            system.whilerepeat()
        txtdis.renew(4)


        txtdis.renew(7)

        system.waituntilmouserelease()
        txtdis.renew(8)


        system.waituntilmouserelease()
        txtdis.renew(9)


        system.waituntilmouserelease()
        txtdis.renew(10)


        system.waituntilmouserelease()
        txtdis.renew(11)

        system.waituntilmouserelease()
        txtdis.renew(12)
        system.waituntilmouserelease()
        txtdis.renew(13)
        system.waituntilmouserelease()
        txtdis.renew(14)
        system.waituntilmouserelease()
        for i in range(30):
            screen.fill((0,0,0))
            system.fadeout()
            system.whilerepeat()
        bg.updateimage(8,0,0,0,0)
        system.currentstage = '10'

class Stage1():
    def __init__(self):
        pass
    def currentstage10(self):
        print('Entering Escape')
        txtdis.load(1)
        bg.updateimage(9, 0, 0, 0, 0)
        #"""
        updatelist.remove(textbar)
        updatelist.remove(txtdis)#"""
        #updatelist.append(bg)
        for i in range(25):
            screen.fill((0, 0, 0))
            bg.alpha = bg.alpha + i * 25.5
            system.whilerepeat()
        system.waituntilmouserelease()
        for i in range(25):
            screen.fill((0, 0, 0))
            bg.alpha = bg.alpha - i * 25.5
            system.whilerepeat()
        bg.alpha = -45
        textbar.alpha = -45
        objectbar.alpha = -45
        madamroomicon.alpha = -45
        dukeroomicon.alpha = -45
        woodendooricon.alpha = -45
        bg.updateimage(10, 352, 0, 1568, 840)
        txtdis.load(1)
        txtdis.renew(1)
        
        print('currentstage10')
        self.currentstage11()
    
    def currentstage11(self):

        updatelist.append(textbar)
        updatelist.append(objectbar)
        system.updateicons()
        fadelist.append(textbar)
        fadelist.append(objectbar)
        fadelist.append(madamroomicon)
        fadelist.append(dukeroomicon)
        fadelist.append(woodendooricon)
        for i in range(30):
            screen.fill((0, 0, 0))
            system.fadein()
            system.eventupdate()
            system.update()
            pygame.display.update()
        
        for i in system.currentdisplayscene:
            updatelist.append(i)
        print(updatelist)
        print(textbar.alpha)
        updatelist.append(txtdis)
        print('currentstage11')
        system.execute('swapscene', 'swapmadamroom')
    
    def currentstage12(self):
        #unlocked duke room
        system.currentstage = '12'
        system.dukeroomlock = False
        global dukestudyicon
        dukestudyicon = classes.objects(240, 800, 19, 80, 45)
        dukestudyicon.assign('swapdukestudy')
        updatelist.append(dukestudyicon)
        currentdisplaybuttons.append(dukestudyicon)
        system.execute('swapscene', 'swapdukeroom')
    
    def currentstage13(self):
        #unlocked dukestudy
        system.currentstage = '13'
        system.dukestudylock = False
        system.execute('swapscene', 'swapdukestudy')
    
    def currentstage14(self):
        system.currentstage = '14'
        bg.updateimage(16, 352, 0, 1568, 840)
        updatelist.remove(system.objectbaraxe)
        system.update()
        pygame.display.update()
        updatelist.remove(madamroomicon)
        updatelist.remove(dukeroomicon)
        updatelist.remove(dukestudyicon)
        updatelist.remove(woodendooricon)
        txtdis.dpmultiline(14,28)
        global leadericon
        leadericon = classes.objects(0, 800, 21, 80, 45)
        dukestudyicon.assign('swapleaderroom')


        updatelist.append(leadericon)
        currentdisplaybuttons.append(leadericon)
        system.execute('swapscene', 'swapleaderroom')


system = Gamesys()
stage0 = Stage0()
stage0.currentstage00()
stage1 = Stage1()
stage1.currentstage10()
clock.tick(60)
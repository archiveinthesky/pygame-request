import pygame
import commonvar
import screenctrl
pygame.init()

global screen, txtdis
screen = commonvar.bridge.getvar('screen')
txtdis =commonvar.bridge.getvar('txtdis')

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

textfont = pygame.font.Font("texts/brushpen.ttc", 40)

class Simplefunctions():
    def __init__(self):
        self.mouseclick = False
        
        self.updatelist = commonvar.bridge.getvar('updatelist')
    def waituntilmouserelease(self):
        while commonvar.bridge.getvar('mouseclick') == True:
            self.whilerepeat()
        while commonvar.bridge.getvar('mouseclick') == False:
            self.whilerepeat()
    def whilerepeat(self):
        commonvar.bridge.updatevar('updatelist', self.updatelist)
        screenctrl.controls.eventupdate(commonvar.bridge.getvar('updatelist'))
        updatelist = commonvar.bridge.getvar('updatelist')
        for updateitem in updatelist:
            updateitem.update()
        
        pygame.display.update()


sf = Simplefunctions()
class background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = bgs[0].convert()
        self.image.set_alpha(255)
        self.image.set_colorkey(pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect()
        self.bgno = 2
        self.alpha = 255
        self.responses = [1, 1]

    def update(self):
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def updateimage(self, currentbgno, blitx, blity, resizex, resizey):
        self.bgno = currentbgno
        if resizex == 0 and resizey == 0:
            self.image = bgs[self.bgno].convert()
        else:
            self.image = pygame.transform.scale(bgs[self.bgno], (resizex, resizey)).convert()
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
        self.responses = [1, 1]
        self.hover = False
        self.password = 'none'
        
    def detectmouse(self):#''''''
        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            self.hover = True
        else:
            self.hover = False
        if self.rect.collidepoint(pygame.mouse.get_pos()) and commonvar.bridge.getvar('mouseclick')== True:
            self.click = True
        else:
            self.click = False
    def update(self):
        self.detectmouse()
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pygame.mouse.get_pos()) == True:
            self.hover = True
        else:
            self.hover = False
        if self.rect.collidepoint(pygame.mouse.get_pos()) and commonvar.bridge.getvar('mouseclick') == True:
            self.click = True
        else:
            self.click = False

    def setpass(self, password):
        
        self.unlock = commonvar.bridge.getvar('enterpass')
        self.password = str(password)

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
        if self.password != 'none':
            print(self.unlock.unlock(self.password))


class textdisplay(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.txtarray= []
        self.passwordmode = False
        self.lines = 1
        self.currentdisplayline = 1
    def load(self, doc):
        scriptread = open('texts/stage' + str(doc) + 'text.txt', 'r', encoding = 'utf8')
        global script
        script = scriptread.read().splitlines()
    
    
    def dpmultiline(self, responcestart, responceend):
        self.lines = (responceend - responcestart) + 1
        for i in range(self.lines):
            txtdis.renew(i + responcestart)
            sf.waituntilmouserelease()
        txtdis.renew(1)

    def renew(self, line):
        self.txtarray = []
        self.line = script[line]
        self.current = 1
        self.goal = len(self.line)
    
    def update(self):
        if self.current == self.goal:
            screen.blit(textfont.render(self.line, False, (150, 0, 0)), (0, 850))

        else:
            self.current = self.current + 1
            screen.blit(textfont.render(self.line[:self.current], False, (150, 0, 0)), (0, 850))

    def simplerender(self, x, y, r, g, b, text):
        screen.blit(textfont.render(str(text), False, (r, g, b)), (x, y))


txtdis = textdisplay()
commonvar.bridge.setvar('txtdis', txtdis)
class enterpassclass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.enterpress = False
        self.close = objects(1691,3,24,91,141)
        self.entered = ''
        self.enterkey = ''
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def unlock(self, anwser):
        updatelist = commonvar.bridge.getvar('updatelist')
        self.enterpress = False
        self.entered = ''
        self.enterkey = ''
        self.close.click = False
        updatelist.append(enterpass)
        updatelist.append(self.close)
        commonvar.bridge.updatevar('updatelist', updatelist)
        while self.enterpress == False and self.close.click == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.check(event.key)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    commonvar.bridge.updatevar('mouseclick', True)
                else:
                    commonvar.bridge.updatevar('mouseclick', False)
            sf.whilerepeat()
        updatelist.remove(enterpass)
        updatelist.remove(self.close)
        commonvar.bridge.updatevar('updatelist', updatelist)
        if self.entered == str(anwser):
            return 'pass'
        else:
            return 'notpass'
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
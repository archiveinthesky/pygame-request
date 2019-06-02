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
    def waituntilmouserelease(self):
        while commonvar.bridge.getvar('mouseclick') == True:
            self.whilerepeat()
        while commonvar.bridge.getvar('mouseclick') == False:
            self.whilerepeat()
    def whilerepeat(self):
        screenctrl.controls.eventupdate(commonvar.bridge.getvar('updatelist'))
        for updateitem in commonvar.bridge.getvar('updatelist'):
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


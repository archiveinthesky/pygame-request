import pygame
#import pyganim
from pygame.locals import *
# 初始化 pygame
# dictionary module: pandas

pygame.init()
pygame.font.init()
from random import randint
import datetime
import math

size = 8;
# 設定遊戲畫面大小
screen = pygame.display.set_mode((144 * size, 90 * size))
keys = pygame.key.get_pressed()

#loading pictures and assets

BGColor = (100, 80, 100)
youwin = pygame.transform.scale(pygame.image.load('assets/youwin.png'), (size * 40, size * 40))
compwin = pygame.transform.scale(pygame.image.load('assets/computerwins.jpeg'), (size * 40, size * 40))
start = pygame.transform.scale(pygame.image.load('assets/start.jpeg'), (size * 30, size * 30))
countdown = [pygame.image.load('assets/3.png'),
             pygame.image.load('assets/2.png'),
             pygame.image.load('assets/1.png')]
upbutton = pygame.transform.scale(pygame.image.load('assets/up.png'), (size * 10, size * 10))
downbutton = pygame.transform.scale(pygame.image.load('assets/down.png'), (size * 10, size * 10))
replay = pygame.transform.scale(pygame.image.load('assets/playagain.png'), (size * 20, size * 20))
playbg = pygame.image.load('assets/battle.jpg')
startbg = pygame.image.load('assets/startimg.jpg')
choosebg = pygame.image.load('assets/choosebg.jpg')
check = [pygame.transform.scale(pygame.image.load('assets/unchecked.png'), (60, 60)),
         pygame.transform.scale(pygame.image.load('assets/check.png'), (60, 60))]
pics = [pygame.transform.scale(pygame.image.load('assets/9.jpg'), (260, 350)),
        pygame.transform.scale(pygame.image.load('assets/10.jpg'), (260, 350)),
        pygame.transform.scale(pygame.image.load('assets/11.jpg'), (260, 350)),
        pygame.transform.scale(pygame.image.load('assets/12.jpg'), (260, 350)),
        pygame.transform.scale(pygame.image.load('assets/13.jpg'), (260, 350)),
        pygame.transform.scale(pygame.image.load('assets/14.jpg'), (260, 350)),
        pygame.transform.scale(pygame.image.load('assets/15.jpg'), (260, 350))]
instructions = pygame.transform.scale(pygame.image.load('assets/instructions.png'), (1155, 722))
insButton = pygame.transform.scale(pygame.image.load('assets/InstructionsButton.png'), (200, 70))
mainmenu = pygame.transform.scale(pygame.image.load('assets/Badge_Main_Menu.png'), (150, 150))

fr = open('10k.txt', 'r')
text = fr.read().splitlines()
text = fr.read().splitlines()
print(text)
fr.close()
font = pygame.font.Font('fonts/couture-bld.otf', 4*size)
sign = pygame.font.Font('fonts/Code New Roman.otf', 5*size)
nextword = pygame.font.Font("fonts/Code New Roman.otf", 3 * size)
bigword = pygame.font.Font('fonts/Hack-Regular.ttf', 10 * size)
yearold = pygame.font.Font('fonts/Hack-Regular.ttf', 6 * size)

words = 0

class wordgen(pygame.sprite.Sprite):
    def __init__(self):
        global dif
        self.word = ''
        self.ifupdate = False
        self.num = 20
        self.list = []
        self.current = 0
        self.win = False
        self.vocab = [3000, 4000, 5500, 7000, 8000, 9000, 9500, 9500]
    def choose(self):
        self.word = text[randint(0, self.vocab[dif - 9])]
        self.list.append(self.word)
    def check(self):
        if (enterstring.string == self.word):
            global words
            words += 1
            self.current += 1
            if (self.current >= self.num):
                self.win = True
                return
            self.word = self.list[self.current]
    def generate(self):
        self.current = 0
        self.num = 20 + (dif - 9) * 10
        for i in range(self.num):
            self.choose()
        self.word = self.list[self.current]

class compgen(pygame.sprite.Sprite):
    def __init__(self):
        global dif
        self.word = ''
        self.num = 20
        self.list = []
        self.current = 0
        self.win = False
    def copy(self):
        self.num = 20 + (dif - 9) * 10
        self.list = wordgen.list
        self.word = self.list[self.current]
        self.current = 0
        computer.lim = len(self.word)
        computer.wordlen = 0
    def next(self):
        self.current += 1
        if (self.current >= self.num):
            self.win = True
            return
        self.word = self.list[self.current]
        computer.lim = len(self.word)
        computer.wordlen = 0

class enterstring(pygame.sprite.Sprite):
    def __init__(self):
        self.string = ''
        self.keys = keys
        self.chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def work(self, keynum):
        if (compgen.win == False):
            if (keynum >= 97 and keynum <= 122):
                self.string += self.chars[keynum - 97]
            if (keynum == 32):
                if (wordgen.ifupdate == True):
                    print (self.string)
                    wordgen.check()
                self.string = ''
            if (keynum == 8):
                self.string = self.string[0:-1]
            if (keynum == 13):
                global chose
                if (wordgen.ifupdate == False and ifstart == True):
                    chose = True
            if (keynum == 27 and wordgen.ifupdate == True):
                global esc, timer, t
                esc += 1
                timer = t.second


class computer(pygame.sprite.Sprite):
    def __init__(self):
        global dif
        self.difficulty = 0
        self.speed = [2.5, 2.8, 3.2, 3.8, 4.3, 4.6, 4.85, 5.1]
        self.accuracy = [82, 83, 84, 87, 90, 92, 95, 95]
        self.time = 0
        self.str = ''
        self.wordlen = 0
        self.lim = 0
    def type(self, ti):
        if (self.wordlen <= self.lim) :
            if (ti > self.time):
                if (ti - self.time > 1000000 / self.speed[dif - 9]):
                    self.time = ti
                    if (randint(1, 101) > 100 - self.accuracy[dif - 9]):
                        self.enter()
            if (ti < self.time):
                if (ti + 1000000 - self.time > 1000000 / self.speed[dif - 9]):
                    self.time = ti
                    if (randint(1, 101) > 100 - self.accuracy[dif - 9]):
                        self.enter()
    def enter(self):
        self.wordlen += 1
        self.str = compgen.word[0:self.wordlen]
        if (self.wordlen == self.lim):
            compgen.next()


enterstring = enterstring()
wordgen = wordgen()
compgen = compgen()
computer = computer()
ifstart = False
chose = False
dif = 9
timed = False
esc = 0
memory = 0
instr = False

# 主遊戲循環
clock = pygame.time.Clock()
running = True
fps = 60
while running:
    screen.fill(BGColor)
    if (ifstart == False):
        screen.blit(startbg, (0, 0))
    elif (ifstart == True):
        if (wordgen.ifupdate == True):
            screen.blit(playbg, (0, 0))
        else:
            screen.blit(choosebg, (0, 0))
    # 控制遊戲最大幀率為 60
    clock.tick(fps)
    # 按右上角X可以關掉遊戲
    t = datetime.datetime.now()
    if (ifstart == False):
        screen.blit(start, (430, 170))
        screen.blit(insButton, (900, 550))
    if (instr == True):
        screen.blit(instructions, (0, 0))
        screen.blit(mainmenu, (1000, 20))
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            enterstring.work(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (start.get_rect(topleft=(430, 170)).collidepoint(x, y) and instr == False and wordgen.ifupdate == False):
                ifstart = True
            if (upbutton.get_rect(topleft=(200, 200)).collidepoint(x, y)):
                if (dif + 1 <= 16):
                    dif += 1
            if (downbutton.get_rect(topleft=(200, 500)).collidepoint(x, y)):
                if (dif - 1 >= 9):
                    dif -= 1
            if (replay.get_rect(topleft=(450, 250)).collidepoint(x, y) and (wordgen.win == True or compgen.win == True)):
                wordgen.win = False
                compgen.win = False
                ifstart = True
                wordgen.ifupdate = False
                chose = False
                wordgen.__init__()
                compgen.__init__()
                enterstring.__init__()
                computer.__init__()
                words = 0
            if (check[memory].get_rect(topleft=(205, 630)).collidepoint(x, y)):
                if memory == 0:
                    memory = 1
                else:
                    memory = 0
            if (insButton.get_rect(topleft=(900, 550)).collidepoint(x, y)):
                instr = True
            if (mainmenu.get_rect(topleft=(1000, 20)).collidepoint(x, y)):
                instr = False

    if (ifstart == True and wordgen.ifupdate == False and timed == False):
        screen.blit(upbutton, (200, 200))
        screen.blit(downbutton, (200, 500))
        if (dif <= 15):
            difstr = bigword.render(str(dif) + " yrs old", False, (55, 55, 55))
            screen.blit(pics[dif - 9], (800, 200))
        else:
            difstr = yearold.render("Peak Condition (HARD)", False, (55, 55, 55))
        screen.blit(difstr, (218, 350))
        checkbox_rect = check[memory].get_rect()
        checkbox_rect.topleft = (205, 630)
        screen.blit(check[memory], checkbox_rect)
        screen.blit(nextword.render("Memory mode: Can't see the current word! (Remember the next word)", False, (0, 0, 0)), (300, 650))

    if (chose):
        wordgen.generate()
        compgen.copy()
        chose = False
        timer = t.second
        timed = True

    if(wordgen.ifupdate == True):
        try:
            screen.blit(nextword.render("Next: " + wordgen.list[wordgen.current + 1], False, (100, 100, 100)), (200, 180))
        except IndexError:
            screen.blit(nextword.render("<End>", False, (100, 100, 100)), (400, 180))

        if (esc == 1):
            leave = font.render("Press ESC again to leave", False, (255, 255, 255))
            screen.blit(leave, (50, 500))
            if (math.fabs(timer - t.second) >=5):
                esc = 0
        if (esc == 2):
            wordgen.ifupdate = False
            ifstart = False
            esc = 0
            wordgen.__init__()
            compgen.__init__()
            enterstring.__init__()
            memory = 0
            words = 0

        aicount = bigword.render(str(compgen.current), False, (0, 0, 0))
        wordcount = bigword.render(str(words), False, (0, 0, 0))
        wordcount_rect = wordcount.get_rect()
        wordcount_rect.topright = (535, 570)
        firstto = sign.render("First to " + str(wordgen.num) + " words", False, (0, 0, 0))
        question = font.render(wordgen.word, False, (0, 0, 0))
        question_rect = question.get_rect()
        question_rect.center = (300, 120)
        textsurface = font.render(enterstring.string, False, (0, 0, 0))
        textsurface_rect = textsurface.get_rect()
        textsurface_rect.topleft = (question_rect.topleft[0], 300)
        aiword = font.render(compgen.word, False, (0, 0, 0))
        computerword = font.render(computer.str, False, (0, 0, 0))
        if (dif <=15):
            display = yearold.render (str(dif) + "-year-old", False, (230, 230, 230))
        else:
            display = yearold.render("Fastest", False, (230, 230, 230))
        display_rect = display.get_rect()
        display_rect.topright = (965, 650)

        screen.blit(display, display_rect)
        screen.blit(textsurface, textsurface_rect)
        if (memory != 1 or words == 0):
            screen.blit(question, question_rect)
            screen.blit(aiword, (740, 100))
        screen.blit(computerword, (740, 300))
        screen.blit(aicount, (610, 570))
        screen.blit(wordcount, wordcount_rect)
        screen.blit(firstto, (50, 20))
    if (wordgen.win == True):
        screen.blit(youwin, (20, 200))
        screen.blit(replay, (480, 250))
    if (compgen.win == True):
        screen.blit(compwin, (800, 200))
        screen.blit(replay, (480, 250))
    if (wordgen.win == False and compgen.win == False and wordgen.ifupdate == True):
        computer.type(int(t.microsecond))

    if (timed):
        try:
            screen.blit(countdown[int(math.fabs(timer - t.second))], (500, 300))
        except IndexError:
            if (math.fabs(timer - t.second) >=3):
                wordgen.ifupdate = True
                timed = False
    # 更新畫面
    pygame.display.update()
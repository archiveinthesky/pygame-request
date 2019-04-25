import pygame
from pygame.locals import *
from pygame_functions import*
import  pygame_textinput
from pygame_textinput import *
import pyganim
import random

pygame.init()
# 設定遊戲畫面大小
screenSize(700,400)
screen = pygame.display.set_mode((700, 400))
bg1 =  pygame.image.load('gameui/bg1.jpg')
bg2 =  pygame.image.load('gameui/bg2.png')
sloganimg = pygame.image.load('gameui/play-title.png')
warrior = pygame.transform.scale(pygame.image.load('gameui/warrior.png'),(120,140))
scene = 0


class slogan(pygame.sprite.Sprite):
    def __init__(self,btntype):
        pygame.sprite.Sprite.__init__(self)
        self.aaa = 255
        ############################################################################here alpha
        self.image = pygame.image.load('gameui/warrior.png')
        #####################################################################################
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.show = 1
        self.rect.y = -100
        self.type = btntype;
    def update(self):
        ############################################################################ here alpha change
        self.image.fill((255, 255, 255,255), None, pygame.BLEND_RGBA_MULT)

        ############################################################################
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def showslogan(self):
        self.rect.y = -100

def showtextoooo():
    wordbox = makeTextBox(10, 80, 300, 0, "Enter text here", 5, 24)
    showTextBox(wordbox)
    entry = textBoxInput(wordbox)
    hideTextBox(wordbox)
    end


clock = pygame.time.Clock()
running = True
count = -100
sw = 1

startposy = -100
slogan111 = slogan("start")
wordbox = makeTextBox(10,80,300,0,"Enter text here",5,24)
showTextBox(wordbox)
ask = 0
texinput = pygame_textinput.TextInput()

while running:
    # 控制遊戲最大幀率為 60
    clock.tick(60)
    # 按右上角X可以關掉遊戲
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            running = False
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_SPACE:
                ask=0
                texinput.clear_text()
                texinput.__init__()

    if scene == 0:
       screen.blit(bg1, (0, 0))
       #screen.blit(warrior,(500,150))
       #slogan111.update()
    elif scene == 1:
        screen.blit(bg2, (0, 0))

    if ask == 0:
        screen.blit(texinput.get_surface(), (50,50))
        if texinput.update(events):
            print(texinput.get_text())
            ask=1


    #showLabel(instructionlabel)
   # showLabel(instructionlabel)


    pygame.display.update()
import pygame

import commonvar
pygame.init()
class Controls():
    def __init__(self):
        self.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
        pygame.display.set_caption('Request')
        commonvar.bridge.setvar('screen',self.screen)
        commonvar.bridge.setvar('mouseclick', False)
        import classes
        self.menushow = 0
        self.menufullscreen = False
        global menu,menufullscreencheck,menufullscreencheckbox,menuleavegame
        menu = classes.objects(550, 150, 1, 766, 887)
        menufullscreencheck = classes.objects(1010, 455, 2, 100, 80)
        menufullscreencheckbox = classes.objects(1010, 455, 3, 80, 80)
        menuleavegame = classes.objects(730, 550, 4, 450, 180)
       
    def eventupdate(self, updatelist):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                commonvar.bridge.updatevar('mouseclick', True)
            else:
                commonvar.bridge.updatevar('mouseclick', False)

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
                        self.menu(updatelist)
                        self.menushow = 1
                    elif self.menushow == 1:
                        self.menushow = 0
                        updatelist.remove(menu)
                        updatelist.remove(menuleavegame)
                        if self.menufullscreen == False:
                            updatelist.remove(menufullscreencheckbox)
                        elif self.menufullscreen == True:
                            updatelist.remove(menufullscreencheck)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    def menu(self, updatelist):
        
        if self.menufullscreen == False and menufullscreencheckbox.click == True:
            menufullscreencheckbox.click = False
            self.menufullscreen = True
            menufullscreencheckbox.click = False
            self.fullscreen(updatelist)

        if self.menufullscreen == True and menufullscreencheck.click == True:
            menufullscreencheck.click = False
            self.menufullscreen = False
            self.resizeable(updatelist)
            menufullscreencheck.click = False
        if menuleavegame.click == True:
            pygame.quit()
            exit()
    
    def fullscreen(self, updatelist):
        menufullscreencheckbox.click = False
        updatelist.remove(menufullscreencheckbox)
        updatelist.append(menufullscreencheck)
        self.screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
        commonvar.bridge.updatevar('screen', self.screen)
    def resizeable(self, updatelist):
        menufullscreencheckbox.click = False
        updatelist.remove(menufullscreencheck)
        updatelist.append(menufullscreencheckbox)
        self.screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
        commonvar.bridge.updatevar('screen', self.screen)

controls = Controls()
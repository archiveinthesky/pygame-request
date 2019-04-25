import pygame
a = pygame.image.load('backgrounds/madamroomtext/2.png')
b = a.get_rect().size
x = b[0]
y = b[1]
c = 1000*y//x
newx = 1000
newy = c
a = pygame.transform.scale(a,(newx,newy))   
screen = pygame.display.set_mode((1000,500))
while True:
    screen.blit(a,(0,0))
    pygame.display.update()
print(b,x,y,c)
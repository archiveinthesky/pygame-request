import pygame
a = pygame.image.load('backgrounds/madamroomtext/1.png')
b = a.get_rect().size
x = b[0]
y = b[1]
c = 1000*y/x
print(b,x,y)
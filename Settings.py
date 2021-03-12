import pygame

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

#Properities
PLAYER_ACC = -1
PLAYER_FRICTION = -0.06
ICE_ACC = -0.4
ICE_FRICTION = -0.01
GRAVITY = 1
ROT_SPEED = 15

#screen size
spaceInFront = 700
WIDTH = 800
HEIGHT = 500
size = (WIDTH, HEIGHT) #800/500
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((size), pygame.RESIZABLE)

# -- Title of new window/screen
pygame.display.set_caption("Car Game")


#clipartkey

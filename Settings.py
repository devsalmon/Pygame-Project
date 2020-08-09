import pygame

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)

#Properities
PLAYER_ACC = -1
PLAYER_FRICTION = -0.06
GRAVITY = 1
ROT_SPEED = 15

#screen size
spaceInFront = 500
WIDTH = 800
HEIGHT = 500
size = (WIDTH, HEIGHT) #800/500
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((size), pygame.RESIZABLE)

# -- Title of new window/screen
pygame.display.set_caption("Car Game")


#NEXT STEP IS GETTING CAR TO ROLL DOWN HILL

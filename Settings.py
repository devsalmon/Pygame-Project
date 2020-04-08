import pygame

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)

#Properities
PLAYER_ACC = -0.5
PLAYER_FRICTION = -0.12

#screen size
WIDTH = 800
HEIGHT = 500
size = (WIDTH, HEIGHT) #800/500
screen = pygame.display.set_mode(size)
#screen = pygame.display.set_mode((size), pygame.RESIZABLE)

# -- Title of new window/screen
pygame.display.set_caption("Road Rush")


#NEXT STEP IS GETTING CAR TO ROLL DOWN HILL

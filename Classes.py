import pygame
from Settings import *

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for Player
    def __init__(self):
        
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.width = 20
        self.height = 20
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(WHITE)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 20
        self.v_gravity = 0
        self.h_speed = 0
        self.running = True

    def update(self):
        self.rect.x = self.rect.x + self.h_speed
        #print(self.v_gravity)
        self.rect.y = (self.rect.y + self.v_gravity)
        #Reset position of Player once off the screen
        if self.rect.y >= size[1]:
            self.running = False
            #self.rect.x = 300
            #self.rect.y = 20
            #pygame.quit()
    #End Method

    def player_set_speed(self, val):
        self.h_speed = val
    # End Method

    def player_set_v_gravity(self, val):
        self.v_gravity = val
        #self.v_gravity += (MAX_SPEED - self.v_gravity) * 2

# End Player class

class Path(pygame.sprite.Sprite):
    # Define the constructor for Path
    def __init__(self, xpos, ypos):

        # Call the sprite constructor
        super().__init__()
        self.width = 1
        self.height = 1
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(WHITE)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.x_speed = 0

    def update(self):    
        self.rect.x -= self.x_speed
        
    def scroll(self, val):
        self.x_speed = val

# End Path class

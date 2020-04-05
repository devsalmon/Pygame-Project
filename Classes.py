import pygame
from Settings import *
import cv2, time #!!!!!
import math

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
        self.running = True
        self.g_Acc = 0
        self.g_Vel = 0

    def update(self):
        self.g_Acc = 0.8
        self.g_Vel += self.g_Acc
        self.rect.y += self.g_Vel + 0.5 * self.g_Acc
        #Reset position of Player once off the screen
        if self.rect.y >= size[1]:
            video = cv2.VideoCapture(0) #!!!!!!
            # create a frame object #!!!!!!!!!!
            check, frame = video.read() #!!!!!!
            #print(check) #!!!!!!!!!!
            #print(frame) # representing image #!!!!!!!
            cv2.imshow("Capturing", frame) #!!!!!!!
            cv2.waitKey(0) #!!!!!!!!!!
            video.release() #!!!!!!!!!!!!
            cv2.destroyAllWindows #!!!!!!!!!!!!!!
            self.running = False
    #End Method

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
        self.vel = 0
        self.acc = 0
        
    def update(self):    
        self.acc = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.acc = -1
        self.acc += self.vel * -0.06 # apply friction
        self.vel = self.vel + self.acc
        ###ISSUE: Path moved Right appropriately and would stop like it should.
        #However it would never stop when moving left due to asymptotic equation.
        #In other words, once self.vel < 0.1 it would round down to 0, thus it worked
        #when moving to the right. However when self.vel > -0.1, it would always round
        #to -0.1 no matter how close to 0 it was. So now with math.ceil, -0.001 would
        #round up to 0.
        #WHY are blocks piling up? Could it be because negative acceleration in the
        #negative direction. Maybe I should just destroy blocks once negative.
        self.rect.x += (math.ceil(self.vel) + (0.5 * self.acc)) #S = Ut + 1/2at^"

# End Path class

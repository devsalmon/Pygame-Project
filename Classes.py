import pygame
from Settings import *
#import cv2, time #!!!!!
import math
import random

# Defines the class Player which is a sprite.
class Player(pygame.sprite.Sprite):
    
    # Define the constructor for Player.
    def __init__(self, my_Game):
        
        # Call the sprite constructor.
        super().__init__()
        # Allows attributes from the Game class to be accessed.
        self.my_Game = my_Game
        # Sets the width and height of the object to 20 by 20 pixels.
        self.width = 20
        self.height = 20
        # Creates the sprite image.
        self.image = pygame.Surface([self.width,self.height])
        ##self.image = pygame.image.load("mcqueensprite.png")
        self.image.set_colorkey(BLACK)
        self.new_image = self.image
        #self.new_image.set_colorkey(BLACK)
        self.image.fill(WHITE)
        # Set the position of the sprite
        #self.new_image = self.image.get_rect()
        #self.rect = self.new_image
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 20
        self.running = True
        # Sets the acceleration of the gravitational
        # force equal to the constant.
        self.g_Acc = GRAVITY
        # The initial velocity of gravity will be 0.
        self.g_Vel = 0
        #For rotation:
        self.rot = 0
        self.rot_speed = ROT_SPEED
        self.rect.center = (310, 50)
        #For finding y velocity:
        self.y_reading = False
        self.t = 0
        self.last_y = 0
        self.current_y = 0
        self.change_in_y = 0

    def update(self):

        # GRAVITY
        # Motion equations for constant acceleration (SUVAT).
        # V = U + AT.
        self.g_Vel += self.g_Acc
        #S = UT + 1/2AT^2.
        self.rect.y += self.g_Vel + 0.5 * self.g_Acc

        #Finds player's y component of velocity when collided(for lift off)
        if self.my_Game.player_path_collision_group:
            self.t += 1 #Later every 60 loops (1 second) the y component of velocity is given.
            if self.y_reading == True:
                self.last_y = self.rect.y
                self.y_reading = False
            self.current_y = self.rect.y #Every loop current y position is returned so that it can be subtracted from last position taken (last_y)
            self.change_in_y = self.current_y - self.last_y
            if self.t % 30 == 0: #Every 0.5 seconds set current y reading to last one.
                self.y_reading = True
            #print(self.change_in_y) #Fine but should be improved maybe with time.wait
        else:
            self.change_in_y = 0
            
        #Reset position of Player once off the screen (new game) + take photo
        if self.rect.y >= HEIGHT:
           ## video = cv2.VideoCapture(0) #!!!!!!
            # create a frame object #!!!!!!!!!!
            #check, frame = video.read() #!!!!!!
            #print(check) #!!!!!!!!!!
            #print(frame) # representing image #!!!!!!!
            #cv2.imshow("Capturing", frame) #!!!!!!!
            #cv2.waitKey(0) #!!!!!!!!!!
            #video.release() #!!!!!!!!!!!!
            #cv2.destroyAllWindows #!!!!!!!!!!!!!!
            self.running = False
        #Endif
            
        keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP]: #PLAYER projection. Also look at bottom right rect...
         #   self.g_Vel = -5   #A.rect.bottomright. must find y vel at all times for this.
        #ROTATE PLAYER
        if keys[pygame.K_SPACE] and not self.my_Game.player_path_collision_group:
            #making a copy of the old center of the rectangle
            old_center = self.rect.center
            #defines angle of rotation
            self.rot = (self.rot + self.rot_speed) % 360
            #rotating the orignal image  
            self.new_image = pygame.transform.rotate(self.image , self.rot)
            #self.image = self.new_image#
            self.rect = self.new_image.get_rect()
            #self.rect = self.image.get_rect()#
            #set the rotated rectangle to the old center
            self.rect.center = old_center
            #screen.blit(new_image, self.rect)
    #End method

# End Player class

# Defines the class Path which is a sprite.
class Path(pygame.sprite.Sprite):
    
    # Define the constructor for Path.
    def __init__(self, my_Game, xpos, ypos):

        # Call the sprite constructor.
        super().__init__()
        # Allows attributes from the Game class to be accessed.
        self.my_Game = my_Game
        # Each object will be a square 1 pixel wide and 1 pixel tall.
        self.width = 1
        self.height = 1
        # Creates the sprite image.
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # Set the position of the sprite.
        # Each object will have different coordinates. The are instantiated
        # in the game class and will make up different components.
        self.rect.x = xpos
        self.rect.y = ypos
        self.vel = 0
        self.acc = 0
        self.rawscore = 0
        self.score = 0
        self.origx = 0
        
    def update(self):
        if self.my_Game.score == 0:
            self.origx = self.rect.x
         # Acceleration must always be 0 except for when space key is pressed.
        self.acc = 0
        # Stores which keys get pressed.
        keys = pygame.key.get_pressed()

        # If the space key is pressed and the player and path are colliding...
        if keys[pygame.K_SPACE] and self.my_Game.player_path_collision_group:
            # Sets acceleration equal to the player acceleration constant.
            self.acc = PLAYER_ACC
            
        # Motion equations for constant acceleration (SUVAT).
        # This reduces the acceleration as the velocity increases, allowing
        # the player to decelerate when the space key is not pressed, and also
        # sets a limit to the maximum speed possible to reach.
        self.acc += self.vel * PLAYER_FRICTION
        # V = U + AT.
        self.vel = self.vel + self.acc
        # S = UT + 1/2AT^2.
        self.rect.x += math.ceil(self.vel) + (0.5 * self.acc)
        
        # removes path from path group.
        if self.rect.x < 30:
            self.my_Game.path_group.remove(self)

        #SCORE
        self.rawscore = int(self.origx - self.rect.x)
        #if self.rawscore % 20 == 0: #Keeps the score from going too high.
        self.score = math.ceil(self.rawscore / 20) # WHY DOESN'T // WORK?!
        #self.my_Game.collision = pygame.sprite.collide_rect(self.my_Game.my_Player.bottomright, self)
# End Path class

class Collectables(pygame.sprite.Sprite):

    def __init__(self, xpos, ypos):
    #def __init__(self, my_Game, xpos, ypos):

        super().__init__()
        self.width = 20
        self.height = 20
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(YELLOW)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

class SizeUp(Collectables):
    def __init__(self, xpos, ypos):  # you can pass some other properties
        super().__init__(xpos, ypos)  # you must pass required args to Alien's __init__
        # your custom stuff:
        #self.player = player
        #self.my_Game = my_Game

    #def update(self):

        #if self.my_Game.player_SizeUp_collision_group:

    #def spawn(self):
     #   self.rect.x = random.randrange(spaceInFront) + 310
      #  ypos = random.randrange(HEIGHT - 10)

   # def update(self):
        #for count in range(20):
         #   self.spawn()
        #Next count

import pygame
from Settings import *
#import cv2, time #!!!!!
import math

## -- Define the class Player which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for Player
    def __init__(self, my_Game):
        
        # Call the sprite constructor
        super().__init__()
        self.my_Game = my_Game
        # Create a sprite and fill it with colour
        self.width = 20
        self.height = 20
        self.image = pygame.Surface([self.width,self.height])
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
        self.g_Acc = 0
        self.g_Vel = 0
        #For rotation:
        self.rot = 0
        self.rot_speed = 15
        self.rect.center = (310, 50)
        #For finding y velocity:
        self.y_reading = False
        self.t = 0
        self.last_y = 0
        self.current_y = 0
        self.change_in_y = 0

    def update(self):
        #Gravity
        self.g_Acc = 0.8
        self.g_Vel += self.g_Acc
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

class Path(pygame.sprite.Sprite):
    # Define the constructor for Path
    def __init__(self, my_Game, xpos, ypos):

        # Call the sprite constructor
        super().__init__()
        #self.game = game
        self.my_Game = my_Game
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
        self.rawscore = 0
        self.score = 0
        
    def update(self):
        orig = self.rect.x
        self.acc = 0
        keys = pygame.key.get_pressed()
        #hits = pygame.sprite.spritecollide(self, self.my_Game.my_Player, False)
        if keys[pygame.K_SPACE] and self.my_Game.player_path_collision_group:
            self.acc = -1
            #print(self.collision)
            #self.rect.x += 1
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
        #SCORE
        if self.rect.x < orig: #If player has moved forwards
            self.rawscore += 1 #Add one
            if self.rawscore % 20 == 0: #Keeps the score from going too high.
                self.score += 1
        #self.my_Game.collision = pygame.sprite.collide_rect(self.my_Game.my_Player.bottomright, self)
# End Path class

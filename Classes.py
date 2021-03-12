import pygame
from Settings import *
#import cv2, time #!!!!!
import math
import random

# Defines the class Player which is a sprite.
class Player(pygame.sprite.Sprite):
    
    # Define the constructor for Player.
    def __init__(self, my_Game, posx, posy):
        
        # Call the sprite constructor.
        super().__init__()
        # Allows attributes from the Game class to be accessed.
        self.my_Game = my_Game
        # Sets the width and height of the object to 20 by 20 pixels.
        self.width = 20
        self.height = 20
        # Creates the sprite image.
        self.image = pygame.Surface([self.width,self.height])
        #######self.image = pygame.image.load("test.png")
        ##self.image.set_colorkey(YELLOW)
        self.new_image = self.image
        #self.new_image.set_colorkey(BLACK)
        self.image.fill(BLACK)
        # Set the position of the sprite
        #self.new_image = self.image.get_rect()
        #self.rect = self.new_image
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.running = True
        # Sets the acceleration of the gravitational
        # force equal to the constant.
        self.g_Acc = GRAVITY
        # The initial velocity of gravity will be 0.
        self.g_Vel = 0
        #For rotation:
        self.rot = 0
        self.rot_speed = ROT_SPEED
        self.rect.center = (posx, posy)
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

        # Finds player's y component of velocity when on path. (For lift off).
        # If both wheels are on the path...
        if self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group:
            # Add 1 to the counter.
            self.t += 1
            # If it is time to check the velocity...
            if self.y_reading == True:
                # Store the current y position.
                self.last_y = self.rect.y
                # Set self.y_reading to false in order to allow time to
                # pass before storing the y position again.
                self.y_reading = False
            # Every loop the current y position is returned and stored
            # so that it can be subtracted from self.last_y to find the
            # change in the y coordinates. This can be used to work out
            # the vertical component of velocity.
            self.current_y = self.rect.y
            self.change_in_y = self.current_y - self.last_y
            # Everytime self.t reaches a multiple of 20 which is about 0.3 seconds,
            # set the self.y_reading equal to True to update self.last_y.
            if self.t % 20 == 0:
                self.y_reading = True
        # If the wheels are not touching the path, we do not need to worry about
        # vertical velocity as gravity is acting on the car appropriately already.
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
            self.my_Game.playing = False
        #Endif
            
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP]: #PLAYER projection. Also look at bottom right rect...
         #   self.g_Vel = -5   #A.rect.bottomright. must find y vel at all times for this.
        #ROTATE PLAYER
##        if keys[pygame.K_SPACE] and not self.my_Game.player1_path_collision_group and not self.my_Game.player2_path_collision_group:
##            #making a copy of the old center of the rectangle
##            old_center = self.rect.center
##            #defines angle of rotation
##            self.rot = (self.rot + self.rot_speed) % 360
##           #rotating the orignal image  
##            self.new_image = pygame.transform.rotate(self.image , self.rot)
##            #self.image = self.new_image#
##            self.rect = self.new_image.get_rect()
##            #self.rect = self.image.get_rect()#
##            #set the rotated rectangle to the old center
##            self.rect.center = old_center
##            #screen.blit(new_image, self.rect)
    #End method

# End Player class

# Defines the class Player which is a sprite.
class Playerbody(pygame.sprite.Sprite):
    
    # Define the constructor for Player.
    def __init__(self, my_Game):
        
        # Call the sprite constructor.
        super().__init__()
        # Allows attributes from the Game class to be accessed.
        self.my_Game = my_Game
        # Creates image of car.
        self.image = pygame.image.load("car.png")
        # Gives the rotating image a transparent background.
        self.image.set_colorkey(BLACK)
        # The new image at the start will be equal to the current image.
        self.new_image = self.image        
        # Creates variables that will define the angle and speed of rotation.
        self.rot = 0
        self.rot_speed = ROT_SPEED
        ####self.image.fill(YELLOW)
        # Set the position of the sprite
        #self.new_image = self.image.get_rect()
        #self.rect = self.new_image
        self.rect = self.image.get_rect()
        # Sets the acceleration of the gravitational
        # force equal to the constant.
        self.g_Acc = GRAVITY
        # The initial velocity of gravity will be 0.
        self.g_Vel = 0
        #For finding y velocity:
        self.y_reading = False
        self.t = 0
        self.last_y = 0
        self.current_y = 0
        self.change_in_y = 0
        self.running = True

    def update(self):

        # Stores which keys get pressed.    
        keys = pygame.key.get_pressed()
        #if keys[pygame.K_UP]: #PLAYER projection. Also look at bottom right rect...
         #   self.g_Vel = -5   #A.rect.bottomright. must find y vel at all times for this.
        #ROTATE PLAYER
        # If the space key is pressed and the player and path are colliding...
        if keys[pygame.K_SPACE] and not self.my_Game.player1_path_collision_group and not self.my_Game.player2_path_collision_group:
            # Makes a copy of the center of the square to ensure the newly rotated
            # square does not change position.
            old_center = self.rect.center
            # Creates the angle of rotation.
            self.rot = (self.rot + self.rot_speed) % 360
            # Orignal image is rotated, creating a new image.  
            self.new_image = pygame.transform.rotate(self.image , self.rot)
            # The new image is defined as a new object.
            self.rect = self.new_image.get_rect()
            # The rotated square's center is set to the old center.
            self.rect.center = old_center
            
    #End method
            #print(self.rot)
         #if collision + landing on back then die   
        # If both wheels on ground...
        #elif self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group:
            #IF DGREES ARE WITHIN CERTAIN RANGE..
            # Gives body the same gradient as wheels.
         #   self.new_image = pygame.transform.rotate(self.image, (self.my_Game.degs - 180))
        #ELSE RUNNING = FALSE
        #If collided and on its back, new game...
        #elif self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group and self.rot > 90 and self.rot < 270:
         #   self.my_Game.playing = False

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
        self.rollDown = False
        
    def update(self):
        if self.my_Game.score == 0:
            self.origx = self.rect.x

        # Acceleration must always be 0 except for when space key is pressed.
        self.acc = 0
        # Stores which keys get pressed.
        keys = pygame.key.get_pressed()

        # If the space key is pressed and the player and path are colliding...
        if keys[pygame.K_SPACE] and self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group:
            # Sets acceleration equal to the player acceleration constant.
            self.acc = PLAYER_ACC
        # Handles rolling down the hill going downwards.
        elif not keys[pygame.K_SPACE] and self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group and self.my_Game.degs > 100 and self.my_Game.degs < 150:
            # Car rolls forwards down hill.
            self.acc = PLAYER_ACC
        # Handles rolling down the hill going upwards.
        elif not keys[pygame.K_SPACE] and self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group and self.my_Game.degs < -100 and self.my_Game.degs > -150:
            # Car rolls backwards down hill.
            self.acc = -PLAYER_ACC

        # If player has collided with the turbo boost, they should get boosted.
        if keys[pygame.K_SPACE] and self.my_Game.turbo == True:
            self.vel = -12
            
        # Motion equations for constant acceleration (SUVAT).
        # This reduces the acceleration as the velocity increases, allowing
        # the player to decelerate when the space key is not pressed, and also
        # sets a limit to the maximum speed possible to reach.
        self.acc += self.vel * PLAYER_FRICTION

        # If the space key is pressed and the player and path are colliding and ice boost is active...
        if keys[pygame.K_SPACE] and self.my_Game.player1_path_collision_group and self.my_Game.player2_path_collision_group and self.my_Game.ice == True:
            # Sets acceleration equal to the player acceleration constant.
            self.acc = ICE_ACC
            self.acc += self.vel * ICE_FRICTION

        # If ice boost is active
        #if self.my_Game.ice == True:
         #   self.acc += self.vel * -0.01
        
        # V = U + AT.
        self.vel = self.vel + self.acc
        # S = UT + 1/2AT^2.
        self.rect.x += math.ceil(self.vel) + (0.5 * self.acc)
        
        # Removes path from path group when the path is behind the player.
        if self.rect.x < 30:
            self.my_Game.path_group.remove(self)

        #SCORE
        self.rawscore = int(self.origx - self.rect.x)
        #if self.rawscore % 20 == 0: #Keeps the score from going too high.
        self.score = math.ceil(self.rawscore / 20) # WHY DOESN'T // WORK?!
        #self.my_Game.collision = pygame.sprite.collide_rect(self.my_Game.my_Player.bottomright, self)
# End Path class

#class Collectables(pygame.sprite.Sprite):
#
 #   def __init__(self, xpos, ypos):
  #  #def __init__(self, my_Game, xpos, ypos):
#
 #       super().__init__()
  ##      self.width = 20
    #    self.height = 20
     ##   self.image = pygame.Surface([self.width,self.height])
       # self.image.fill(YELLOW)
        # Set the position of the sprite
        #self.rect = self.image.get_rect()
        #self.rect.x = xpos
        #self.rect.y = ypos
        
# Defines the sprite class Spin which is a subclass of 'Path'.
class Spin(Path):
    
    # Defines the constructor.
    def __init__(self, my_Game, xpos, ypos):
        
        # Calls the sprite constructor.
        super().__init__(my_Game, xpos, ypos)
        # Creates the collectable image.
        self.image = pygame.image.load("spin_collectable.png")
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.spin_collectable_group.remove(self)


  ##  def remove_from_group(self):
        # removes path from path group.
    ##    if self.rect.x < 30:
      ##      self.my_Game.collectable_group.remove(self)

#class Spin(Path):
 #   
  #  def __init__(self, xpos, ypos):  # you can pass some other properties
   #     
    #    super().__init__(width, height, xpos, ypos)  # you must pass required args to Alien's __init__
     #   self.image = pygame.image.load("test.png")
      #  #self.image.set_colorkey(YELLOW)
       # self.new_image = self.image
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

# Defines the sprite class TurboBoost which is a subclass of 'Path'.
class TurboBoost(Path):

    # Defines the constructor.
    def __init__(self, myGame, xpos, ypos):

        # Calls the sprite constructor.
        super().__init__(myGame, xpos, ypos)
        # Creates the collectable image.
        self.image = pygame.image.load("turbo_collectable.png")
        # Set the position of the sprite.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method.
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.turbo_collectable_group.remove(self)


# Defines the sprite class IcePath which is a subclass of 'Path'.
class IcePath(Path):

    # Defines the sprite constructor.
    def __init__(self, myGame, xpos, ypos):

        # Calls the sprite constructor.
        super().__init__(myGame, xpos, ypos)
        # Creates the collectable image.
        self.image = pygame.image.load("ice_collectable.png")
        # Set the position of the sprite.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method.
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.ice_collectable_group.remove(self)
            

# Defines the sprite class Giant which is a subclass of 'Path'.
class Giant(Path):

    # Defines the constructor.
    def __init__(self, myGame, xpos, ypos):
        
        # Calls the sprite constructor.
        super().__init__(myGame, xpos, ypos)
        # Creates the collectable image.
        self.image = pygame.image.load("giant_collectable.png")
        # Set the position of the sprite.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method.
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.giant_collectable_group.remove(self)
            

# Defines the sprite class Small which is a subclass of 'Path'.
class Small(Path):
    
    # Defines the constructor.
    def __init__(self, myGame, xpos, ypos):

        # Calls the sprite constructor.
        super().__init__(myGame, xpos, ypos)
        # Creates the collectable image.
        self.image = pygame.image.load("small_collectable.png")
        # Set the position of the sprite.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method.
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.small_collectable_group.remove(self)


# Defines the sprite class Sports which is a subclass of 'Path'.
class Sports(Path):

    # Defines the constructor.
    def __init__(self, myGame, xpos, ypos):

        # Calls the sprite constructor.
        super().__init__(myGame, xpos, ypos)
        # Creates the collectable image.
        self.image = pygame.image.load("sports_car_collectable.png")
        # Set the position of the sprite.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method.
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.sports_collectable_group.remove(self)

            
# Defines the sprite class Random which is a subclass of 'Path'.
class Random(Path):

    # Defines the constructor.    
    def __init__(self, myGame, xpos, ypos):

        # Calls the sprite constructor.
        super().__init__(myGame, xpos, ypos)
        # Create the collectable image.
        self.image = pygame.image.load("random_collectable.png")
        # Set the position of the sprite.
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    def update(self):

        # Calls the path update method.
        super().update()
        # Removes collectables from group once behind player.
        if self.rect.x < 30:
            self.my_Game.random_collectable_group.remove(self)

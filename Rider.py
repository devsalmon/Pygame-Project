#PROJECT
import pygame
import random

# -- Global Constants
turnDown = False
collision = False

#colours
BLACK = (0,0,0)
WHITE = (255,255,255)

# -- Initialise PyGame
pygame.init()

#screen size
size = (800, 500)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Road Rush")

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
        self.v_gravity = 1
        self.h_speed = 0

    def update(self):
        self.rect.x = self.rect.x + self.h_speed
        self.rect.y = self.rect.y + self.v_gravity
        #Reset position of Player once off the screen
        if self.rect.y >= size[1]:
            self.rect.x = 300
            self.rect.y = 20
            #pygame.quit()
    #End Method

    def player_set_speed(self, val):
        self.h_speed = val
    # End Method

    def player_set_v_gravity(self, val):
        self.v_gravity = val

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

# Create a sprite group of all sprites
all_sprites_group = pygame.sprite.Group()
# Create a sprite group of the paths
path_group = pygame.sprite.Group()

# Create the Objects
my_Player = Player()
all_sprites_group.add(my_Player)

my_Path = Path(100, 400)
path_group.add(my_Path)
all_sprites_group.add(my_Player)

#Functions

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# -- Exit game flag set to false
done = False

# SPAWN RAMP
for count in range(1000):
    if my_Path.rect.y <= 100:
        turnDown = True
    if my_Path.rect.y >= 500:
        turnDown = False
    if turnDown == False:
        #Makes ramp go up
        my_Path = Path(my_Path.rect.x + my_Path.rect.width, my_Path.rect.y - 1)
        path_group.add(my_Path)
        all_sprites_group.add(my_Path)
    if turnDown == True:
        #Makes ramp go down
        my_Path = Path(my_Path.rect.x + my_Path.rect.width, my_Path.rect.y + 1)
        path_group.add(my_Path)
        all_sprites_group.add(my_Path)
#Nextcount

### -- Game Loop
while not done:

    # Path and player collisions
    player_path_collision_group = pygame.sprite.spritecollide(my_Player, path_group, False)
    #count = 1
    #for e in player_path_collision_group:
        #print(count + ":" + e.rect.x)
        #print(count + ":" + e.rect.y)
        #print("P:" + my_Player.rect.x + 20)
        #print(":" + my_Player.rect.y + 20)
        #count = count + 1
    if player_path_collision_group:
        collision = True
        my_Player.player_set_v_gravity(0)
    else:
        collision = False
      ##  my_Player.player_set_v_gravity(0)
        ##for foo in player_path_collision_group:
          ##  my_Player.rect.y = foo.rect.y
        #my_Player.rect.y = my_Player.rect.y
        #my_Player.rect.y = player_path_collision_group[0].rect.
            #my_Player.rect.y - 1

    ##else:
      ##  my_Player.player_set_v_gravity(3)
    #Endif
    if collision == True:
        for foo in player_path_collision_group:
            my_Player.rect.y = foo.rect.y - 20 #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
        #if my_Player.rect.y == foo.rect.y and my_Player.rect.x == foo.rect.x:
    else:
        my_Player.player_set_v_gravity(1)
      #  elif my_Player.rect.y != foo.rect.y and my_Player.rect.x != foo.rect.x:
       #     my_Player.player_set_v_gravity(1)          
    
    # -- User inputs here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - A key is down
            if event.key == pygame.K_SPACE: # - If the left key pressed
                for foo in path_group:
                    #if foo.rect ==
                    foo.scroll(1)
                    #foo.rect.y += 10
                #Next
                #my_Path.scroll(1)
                #my_Player.player_set_speed(2) # - Speed set to 4   
        elif event.type == pygame.KEYUP: # - A key released            
            if event.key == pygame.K_SPACE:
                for foo in path_group:
                    foo.scroll(0)
                #my_Player.player_set_speed(0) # Speed set to 0
                #Next
            #Endif
        #Endif
    #Next

# -- Game logic goes after this comment

        
# -- Screen background is BLACK
    screen.fill(BLACK)

# Update each sprite each loop
    all_sprites_group.update()

# -- Draw here
    all_sprites_group.draw(screen)
    #pygame.draw.line(screen, WHITE, (0,0), (200,200), 5)
    
# -- flip display to reveal new position of objects
    pygame.display.flip()
# - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
#HOW DO CREATE A LINE CLASS AND HOW DO YOU GET SCREEN TO MOVE WITH PLAYER

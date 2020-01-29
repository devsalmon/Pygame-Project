#PROJECT
import pygame
import random

# -- Global Constants

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
        self.rect.x = 200
        self.rect.y = 200
        self.v_gravity = 1
        self.h_speed = 0

    def update(self):
        self.rect.x = self.rect.x + self.h_speed
        self.rect.y = self.rect.y + self.v_gravity
        #Reset position of Player once off the screen
        if self.rect.y >= size[1]:
            self.rect.x = 200
            self.rect.y = 200
    #End Method

    def player_set_speed(self, val):
        self.h_speed = val
    # End Method

    def player_set_v_gravity(self, val):
        self.v_gravity = val

# End Player class

class Path(pygame.sprite.Sprite):
    # Define the constructor for Path
    def __init__(self):

        # Call the sprite constructor
        super().__init__()
        self.width = 300
        self.height = 5
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(WHITE)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300

# Create a sprite group of all sprites
all_sprites_group = pygame.sprite.Group()
# Create a sprite group of the paths
path_group = pygame.sprite.Group()

# Create the Objects
my_Player = Player()
all_sprites_group.add(my_Player)

my_Path = Path()
path_group.add(my_Path)
all_sprites_group.add(my_Path)

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

# -- Exit game flag set to false
done = False

### -- Game Loop
while not done:
    
    # -- User inputs here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - A key is down
            if event.key == pygame.K_SPACE: # - If the left key pressed
                my_Player.player_set_speed(4) # - Speed set to 4
        elif event.type == pygame.KEYUP: # - A key released            
            if event.key == pygame.K_SPACE:
                my_Player.player_set_speed(0) # Speed set to 0
                #Endif
            #Endif
        #Endif

# -- Game logic goes after this comment

    player_path_collision_group = pygame.sprite.spritecollide(my_Player, path_group, False)
    for count in player_path_collision_group:
        my_Player.player_set_v_gravity(0)
    #Nextcount

    # When not touching path, Player should fall
    if my_Player.rect.x >= 400:
        my_Player.player_set_v_gravity(2)
    #Endif


# -- Screen background is BLACK
    screen.fill(BLACK)

# Update each sprite each loop
    all_sprites_group.update()

# -- Draw here
    all_sprites_group.draw(screen)
    pygame.draw.line(screen, WHITE, (0,0), (200,200), 5)
    
# -- flip display to reveal new position of objects
    pygame.display.flip()
# - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
#HOW DO CREATE A LINE CLASS AND HOW DO YOU GET SCREEN TO MOVE WITH PLAYER

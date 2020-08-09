#PROJECT
import pygame
import random
from pygame.math import Vector2
from Classes import *
from Settings import *
from os import path

class Game(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        self.turnDown = False
        self.turnUp = False
        self.clock = pygame.time.Clock()
        self.running = True
        self.load_data()

    def load_data(self):
        #Load high score
        self.dir = path.dirname(__file__)#Locate game directory
        with open(path.join(self.dir, 'highscore.txt'), 'rb') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

    def play_Smusic(self):
        song_queue = ["TheFatRat - Unity.mp3", "The Cranberries - Zombie (Lost Sky Remix).mp3",
                           "Monody.mp3", "Xenogenesis.mp3"]
        pygame.mixer.music.load(random.choice(song_queue))
        pygame.mixer.music.play()
        #pygame.mixer.music.set_volume(0.0)
        
    def straightPath(self):
        # Creates first path block which others build from.
        self.my_Path = Path(self, 175, 200)
        # After each object is created, it is added to the path group and the
        # all sprites group in order to facilitate detecting collisions,
        # and so that they can be drawn easily, all together onto the screen.
        self.path_group.add(self.my_Path)
        self.all_sprites_group.add(self.my_Path)
        # The for loop will iterate 250 times creating 250 path objects.
        for count in range(250):
            # The width of each path is added to the previous x coordinate
            # so that the next object appears exactly on the right of the
            # previous object, forming a level line.
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def manualCurveDown(self):
        # Creates 5 path objects going down at a -1/2 gradient.
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 2, self.my_Path.rect.y + 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        # Creates 4 path objects going down at a -1/3 gradient.
        for count in range(4):
            self.my_Path = Path(self, self.my_Path.rect.x + 3, self.my_Path.rect.y + 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        # Creates 3 path objects going down at a -1/4 gradient.    
        for count in range(3):
            self.my_Path = Path(self, self.my_Path.rect.x + 4, self.my_Path.rect.y + 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        # Creates 5 level path objects at the bottom of the curve.
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 1, self.my_Path.rect.y)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def manualCurveUp(self):
        # Creates 5 level path objects at the bottom of the curve.
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 1, self.my_Path.rect.y)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        # Creates 3 path objects going up at a 1/4 gradient.
        for count in range(3):
            self.my_Path = Path(self, self.my_Path.rect.x + 4, self.my_Path.rect.y - 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        # Creates 4 path objects going up at a 1/3 gradient.
        for count in range(4):
            self.my_Path = Path(self, self.my_Path.rect.x + 3, self.my_Path.rect.y - 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        # Creates 5 path objects going up at a 1/2 gradient.
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 2, self.my_Path.rect.y - 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def pathGap(self):
        # Adds 60 pixels to the previous path object, creating a gap.
        self.my_Path = Path(self, self.my_Path.rect.x + 60, self.my_Path.rect.y)
        # The for loop iterates 30 times creating a short straight path,
        # giving the player something to land on.
        for count in range(30):
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def downRamp(self):
        # The for loop will iterate 125 times creating 125 path objects.
        for count in range(125):
            # Creates a new path object directly on the right of the previous
            # object by adding the width to the x coordinate. It also subtracts
            # the height of the object to the y coordinate to make each object
            # appear slightly lower than the previous object, forming a ramp.
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y + 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def upRamp(self):
        # The for loop will iterate 125 times creating 125 path objects.
        for count in range(125):
            # Creates a new path object directly on the right of the previous
            # object by adding the width to the x coordinate. It also adds
            # the height of the object to the y coordinate to make each object
            # appear slightly above the previous object, forming a ramp.
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y - 1)
            # Adds each object to the sprite groups.
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    # Creates downwards compatible path components in a random order.
    def createPath_d(self):

        # Stores the compatible path components in a list.
        paths = [self.manualCurveDown, self.manualCurveUp, self.downRamp] #self.pathGap]
        # Chooses a random item from the list and executes the selected method.
        random.choice(paths)()

    # Creates upwards compatible path components in a random order.
    def createPath_u(self):

        # Stores the compatible path components in a list.
        paths = [self.manualCurveDown, self.manualCurveUp, self.upRamp] #self.pathGap]
        # Chooses a random item from the list and executes the selected method.
        random.choice(paths)()

    #After certain x value. Harder path functions should start.

    def createCollectables(self):
        #xpos = random.randrange(spaceInFront) + 310
        xpos = 300
        ypos = random.randrange(HEIGHT - 10)
        self.my_Collectable = Collectables(xpos, ypos)
        #print(self.my_Collectable.rect.y)
        self.collectable_group.add(self.my_Collectable)
        self.all_sprites_group.add(self.my_Collectable)
        
    def new_game(self):

        #self.play_Smusic() #Plays the shuffled song

        self.score = 0
        self.insx = 180 #Instructions appear each round

        # Create a sprite group of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        # Create a sprite group of the paths
        self.path_group = pygame.sprite.Group()
        # Create a sprite group of the collectables
        self.collectable_group = pygame.sprite.Group()

        # Create the Objects
        self.my_Player = Player(self)
        self.all_sprites_group.add(self.my_Player)
        self.player_path_collision_group = pygame.sprite.spritecollide(self.my_Player, self.path_group, False)

        self.player_SizeUp_collision_group = pygame.sprite.spritecollide(self.my_Player, self.collectable_group, True)


        for count in range(2): 
            self.createCollectables()

        # SPAWN PATH
        # Initial straight path segment is called so player starts
        # level and comfortably always.            
        self.straightPath()

        # Will create 100 path random path components.
        for count in range(100):
            
            # If path is too low, path will know to start building downwards.
            if self.my_Path.rect.y <= 200:
                # turnDown will be true until path becomes too low.
                self.turnDown = True
            # If path is too high, path will know to start building upwards.
            elif self.my_Path.rect.y >= 350:
                # turnDown will be false until path becomes too high.
                self.turnDown = False              
                    
            # When turnDown is true, path should go downwards.
            if self.turnDown == True:
                # Spawns random downwards components.
                self.createPath_d()
            else:
                # Spawns random upwards components.
                self.createPath_u()

        #Runs game?
        self.run()
        

    def run(self):

        self.playing = True

        while self.playing == True:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            
    def update(self):

        # Update each sprite each loop
        self.all_sprites_group.update()
        #if player,rect.x + 20 != mypath 
        #IF BOTTOM RIGHT DOESNT HAVE COLLISION PLAYER CAN JUMP
        # Path and player collisions
        #for foo in self.path_group:
         #   self.collision = self.my_Player.rect.collidepoint(foo.rect.topright)
        #if self.collision != 0:
        #    print(self.collision)
        #self.collision = pygame.sprite.collide_rect(self.my_Player, self.my_Path)
        #print(self.collision)
        
        # PLAYER-PATH COLLISIONS
        # Creates a group of the path objects the player collides with.
        # False as the last argument indicates that the path objects should
        # not destroy on collision.
        self.player_path_collision_group = pygame.sprite.spritecollide(self.my_Player, self.path_group, False)

        # If the player and path objects collide...
        if self.player_path_collision_group:
            # The player's gravity velocity becomes 0. 
            self.my_Player.g_Vel = 0
            
            # For every object in the collision group...
            for foo in self.player_path_collision_group:
                # The bootom edge of the player should remain on the top
                # edge of the path objects.
                self.my_Player.rect.bottom = foo.rect.top

        else: #If no collision...
            #self.my_Path.acc = 0 #Player shouldn't accelerate when not colliding:
            if self.my_Player.change_in_y < 0: #if no collision + going up... 
                #self.my_Player.current_y = 0
                #self.my_Player.last_y = 0 #makes change_in_y positive.
                self.my_Player.g_Vel = self.my_Path.vel #-8 #player should go up.
                #Player should move down quicker
                #if change in y > 0 allow movement if just collided?


        # PLAYER-COLLECTABLE COLLISIONS
        self.player_SizeUp_collision_group = pygame.sprite.spritecollide(self.my_Player, self.collectable_group, False)
        ##if self.player_SizeUp_collision_group:
            #self.my_Player.width = 2
            #print("test")

        #SCORE
        self.score = self.my_Path.score
        if self.score > self.highscore: #New high score
            #self.draw_stats(50, 50, "NEW HIGH SCORE")
            self.highscore = self.score
            with open(path.join(self.dir, "highscore.txt"), 'w') as f:
                f.write(str(self.highscore))

        #Instructions
        self.insx += self.my_Path.vel   #x pos of info will move appropriately
                                        #vel is negative as path moves left so you add it

        #ENDS GAME
        if self.my_Player.running == False:
            #self.running = False
            self.playing = False
            
    def events(self):

        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False

    def draw(self):
                
        # -- Screen background is BLACK
        screen.fill(BLACK)

        # -- Draw here
        #self.all_sprites_group.draw(screen)
        self.path_group.draw(screen) #Is first block appearing fine?

        #Draws collectables group
        self.collectable_group.draw(screen)
        
        #pygame.draw.line(screen, WHITE, (0,0), (200,200), 5)
        #pygame.draw.arc(screen, WHITE,[80,80,80,80], 0.5, 0.5, 10)
        #Draw player which can rotate
        screen.blit(self.my_Player.new_image, self.my_Player.rect)
        ##screen.blit(self.my_Player.image, self.my_Player.rect)
        
        #Draw stats
        self.draw_stats((WIDTH // 2 - 80), 50, "SCORE: %d" % self.score, 30)
        self.draw_stats((WIDTH - 150), 0, "HIGH SCORE: %d" % self.highscore, 20)
        self.draw_stats(self.insx, 220, "PRESS SPACE TO MOVE", 25)
        self.draw_stats(self.insx, 250, "PRESS SPACE TO FLIP", 25)
        self.draw_stats(self.insx, 280, "DON'T LAND UPSIDE DOWN!", 25)
            
        # -- flip display to reveal new position of objects
        pygame.display.flip()

    def draw_stats(self, x, y, stats, size):
        # Select the font to use, size, bold, italics
        font = pygame.font.SysFont('Calibri', size, True, False)
        # Render the text. "True" means anti-aliased text.
        # Note: This line creates an image of the letters,
        # but does not put it on the screen yet.
        text = font.render(str(stats), True, WHITE)
        # Puts the image of the text on the screen at x,y
        screen.blit(text, (x, y))
#Endproc


#End Game Class

my_Game = Game()
while my_Game.running == True:
    my_Game.new_game()
    
pygame.quit()

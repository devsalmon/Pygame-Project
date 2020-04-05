#PROJECT
import pygame
import random
from pygame.math import Vector2
from Classes import *
from Settings import *

class Game(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.init()
        self.turnDown = False
        self.turnUp = False
        self.collision = False
        self.clock = pygame.time.Clock()
        self.running = True

    def play_Smusic(self):
        song_queue = ["TheFatRat - Unity.mp3", "The Cranberries - Zombie (Lost Sky Remix).mp3",
                           "Monody.mp3", "Xenogenesis.mp3"]
        pygame.mixer.music.load(random.choice(song_queue))
        pygame.mixer.music.play()
        #pygame.mixer.music.set_volume(0.0)

    def straightPath(self):
        for count in range(250):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def manualCurve1(self):
        for count in range(5):
            self.my_Path = Path(self.my_Path.rect.x + 2, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(4):
            self.my_Path = Path(self.my_Path.rect.x + 3, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(3):
            self.my_Path = Path(self.my_Path.rect.x + 4, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(5):
            self.my_Path = Path(self.my_Path.rect.x + 1, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def manualCurve2(self):
        for count in range(3):
            self.my_Path = Path(self.my_Path.rect.x + 4, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(4):
            self.my_Path = Path(self.my_Path.rect.x + 3, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(5):
            self.my_Path = Path(self.my_Path.rect.x + 2, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def pathGap1(self):
        self.my_Path = Path(self.my_Path.rect.x + 60, self.my_Path.rect.y)
        for count in range(30):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def downRamp(self):
        for count in range(125):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def upRamp(self):
        for count in range(125):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def createPath_d(self): #Creates downwards compatible path segments randomly.
        paths = [self.pathGap1, self.manualCurve1, self.manualCurve2, self.downRamp]
        random.choice(paths)()

    def createPath_u(self): #Creates upwards compatible path segments randomly.
        paths = [self.pathGap1, self.manualCurve1, self.manualCurve2, self.upRamp]
        random.choice(paths)()

    #After certain x value. Harder path functions should start.
                  
#Nextcount
        

    def new_game(self):

        #self.play_Smusic() #Plays the shuffled song

        # Create a sprite group of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        # Create a sprite group of the paths
        self.path_group = pygame.sprite.Group()

        # Create the Objects
        self.my_Player = Player()
        self.all_sprites_group.add(self.my_Player)

        self.my_Path = Path(175, 200) #Creates first path block which others build from
        self.path_group.add(self.my_Path)
        self.all_sprites_group.add(self.my_Player)

        # SPAWN RAMP
        self.straightPath() #Initial straight path segment so player starts level and comfortably always. Maybe menu appears above.                  
        for count in range(200):
            
            if self.my_Path.rect.y <= 200: #If path is too low, start building upwards.
                self.turnDown = True
                self.turnUp = False
            elif self.my_Path.rect.y >= 350: #If path is too high, start building downwards.
                self.turnDown = False
                self.turnUp = True                
                
            if self.turnUp == True:
                #Makes ramp go up
                self.createPath_u()
            elif self.turnDown == True:
                #Makes ramp go down
                self.createPath_d()

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

        # Path and player collisions
        player_path_collision_group = pygame.sprite.spritecollide(self.my_Player, self.path_group, False)
        if player_path_collision_group: #If player and block collide...
            for foo in player_path_collision_group:
                self.my_Player.rect.bottom = foo.rect.top #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
                self.my_Player.g_Vel = 0
       
        if self.collision == True:          
            for foo in player_path_collision_group:
                self.my_Player.rect.bottom = foo.rect.top #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
                self.my_Player.g_Vel = 0 #Player's gravity velocity is 0 at collision.

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
        self.all_sprites_group.draw(screen)
        
        #pygame.draw.line(screen, WHITE, (0,0), (200,200), 5)
        #pygame.draw.arc(screen, WHITE,[80,80,80,80], 0.5, 0.5, 10)
            
        # -- flip display to reveal new position of objects
        pygame.display.flip()

#End Game Class

my_game = Game()
while my_game.running == True:
    my_game.new_game()
    
pygame.quit()

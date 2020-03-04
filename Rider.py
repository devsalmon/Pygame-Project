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
        self.t = 0
        self.t2 = 0
        self.y_reading = False
        self.current_y = 0
        self.last_y = 0
        self.change_in_y = 0

    def play_Smusic(self):
        song_queue = ["TheFatRat - Unity.mp3", "The Cranberries - Zombie (Lost Sky Remix).mp3",
                           "Monody.mp3", "LAY LAY.mp3", "Xenogenesis.mp3"]
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

        self.play_Smusic()

        self.t = 0
        self.t2 = 0
        self.change_in_y = 0

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

        #Gravity Power
        #Finds player's y component of velocity
        self.t2 += 1 #Later every 60 loops (1 second) the y component of velocity is given.
        if self.y_reading == True:
            self.last_y = self.my_Player.rect.y
            self.y_reading = False
        self.current_y = self.my_Player.rect.y #Every loop current y position is returned so that it can be subtracted from last position taken (last_y)
        self.change_in_y = self.current_y - self.last_y
        if self.t2 % 30 == 0: #Every 0.5 seconds set current y reading to last one.
            self.y_reading = True

        # Path and player collisions
        player_path_collision_group = pygame.sprite.spritecollide(self.my_Player, self.path_group, False)
        if player_path_collision_group:
            collision = True
        else:
            collision = False
            
        if collision == True:          
            self.my_Player.player_set_v_gravity(0)
            self.t = 0 #Gravity strength resets so time goes to 0.
            for foo in player_path_collision_group:
                self.my_Player.rect.bottom = foo.rect.bottom #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
        else:
            self.my_Player.player_set_v_gravity(1) #WTF stops from floating beyond screen

            self.t += (1/60) #Time elapses where gravity should be getting stronger.
            if self.change_in_y > 0: #Player moves down because of gravity at increasingly faster rates.
                if self.t >= 0 and self.t < 0.5: #if in the air for 0.5 seconds move down at this speed etc.
                    self.my_Player.v_gravity = 2
                elif self.t >= 0.5 and self.t < 1:
                    self.my_Player.v_gravity = 3
                elif self.t >= 1 and self.t < 1.5:
                    self.my_Player.v_gravity = 4
                elif self.t >= 1.5 and self.t < 2:
                    self.my_Player.v_gravity = 5
                elif self.t >= 2 and self.t < 2.5:
                    self.my_Player.v_gravity = 6
                elif self.t >= 2.5 and self.t < 3:
                    self.my_Player.v_gravity = 7
                elif self.t >= 3 and self.t < 3.5:
                    self.my_Player.v_gravity = 8
                elif self.t >= 3.5 and self.t < 4:
                    self.my_Player.v_gravity = 9
                    
            elif self.change_in_y <= -5: #Player should move up if y velocity is fast enough.
                self.my_Player.player_set_v_gravity(-3)
            elif self.change_in_y <= -1 and self.change_in_y > -5:
                self.my_Player.player_set_v_gravity(-1)
        #£ndif

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
            elif event.type == pygame.KEYDOWN: # - A key is down
                if event.key == pygame.K_SPACE: # - If the space key pressed
                    #if self.flying == False: Player should only move if touching surface
                    for foo in self.path_group:
                        foo.scroll(5) #Path scrolls from right to left
            elif event.type == pygame.KEYUP: # - A key released            
                if event.key == pygame.K_SPACE:
                    for foo in self.path_group:
                        foo.scroll(0) #If space key is released, path stops moving
                    #Next
                #Endif
            #Endif
        #Next
                        

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

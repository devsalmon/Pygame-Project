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
        self.bottomRamp1 = False
        self.collision = False
        self.clock = pygame.time.Clock()
        self.running = True
        self.t = 0
        self.flying = True
        self.t2 = 0

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
        #if my_Path.rect.y == 400:
         #   my_Path = Path(my_Path.rect.x + my_Path.rect.width, my_Path.rect.y - 1)

    def pathGap1(self):
        self.my_Path = Path(self.my_Path.rect.x + 60, self.my_Path.rect.y)
        for count in range(30):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def downRamp(self):
        #after certain x value. harder path functions start.
        #Try getting the curves in the down or up functions
        #Game.pathGap1(self)
        #Game.manualCurve1(self)
        #Game.manualCurve2(self)
        for count in range(125):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def upRamp(self):
        for count in range(125):
            self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def createPath_d(self):
        paths = [self.pathGap1, self.manualCurve1, self.manualCurve2, self.downRamp]
        random.choice(paths)()

    def createPath_u(self):
        paths = [self.pathGap1, self.manualCurve1, self.manualCurve2, self.upRamp]
        random.choice(paths)()
                  
#Nextcount
        

    def new_game(self):

        #pygame.draw.arc(screen, WHITE,[80,80,80,80], 0.5, 0.5, 10)
        self.play_Smusic()

        self.t = 0
        self.t2 = 0

        # Create a sprite group of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        # Create a sprite group of the paths
        self.path_group = pygame.sprite.Group()

        # Create the Objects
        self.my_Player = Player()
        self.all_sprites_group.add(self.my_Player)

        self.my_Path = Path(175, 200)
        self.path_group.add(self.my_Path)
        self.all_sprites_group.add(self.my_Player)

        # SPAWN RAMP
        self.straightPath()                   
        for count in range(200):
            
            if self.my_Path.rect.y <= 200:
                self.turnDown = True
                self.turnUp = False
                #self.bottomRamp1 = False
            #elif self.my_Path.rect.y >= 390 and self.my_Path.rect.y <= 392:
             #   self.bottomRamp1 = True
              #  self.turnDown = False
               # self.turnUp = False
            elif self.my_Path.rect.y >= 350:
                #self.bottomRamp1 = False
                #pygame.draw.arc(screen, WHITE ,[88,145,61,25], 0.5,0.5, 10)
                self.turnDown = False
                self.turnUp = True
                #self.bottomRamp = False

        
        #Different type of bottoms and tops of ramps. rounded / gap.
            #if self.bottomRamp == True:
               # for count in range(20):
                #    self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y + 1)                
                
            if self.turnUp == True:
                #Makes ramp go up
                #for i in range(100):
                self.createPath_u()
            elif self.turnDown == True:
                #Makes ramp go down
                #for i in range(100):
                #Game.downRamp(self)
                self.createPath_d()
            #elif self.bottomRamp1 == True:
                #Game.manualCurve(self)
             
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
        if player_path_collision_group:
            self.flying = False
            collision = True
            self.my_Player.player_set_v_gravity(0)
        else:
            collision = False
            self.flying = True
            
        if collision == True:
            for foo in player_path_collision_group:
                self.my_Player.rect.bottom = foo.rect.bottom #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
        else:
            self.my_Player.player_set_v_gravity(1)

        #Gravity Power

        if self.flying == True:
            self.t += (1/60)
            if self.t >= 0 and self.t < 0.5:
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
        elif self.flying == False:
            self.t = 0

        self.t2 += (1/60)
        if self.t2 == 0:
            prev_y_speed = self.my_Player.rect.y
        elif self.t2 == 1:
            current_y_speed = self.my_Player.rect.y
            print(prev_y_speed, current_y_speed)

        #print(self.t)
        #print(self.t) v = u + at

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
                    for foo in self.path_group:
                        foo.scroll(5)
            elif event.type == pygame.KEYUP: # - A key released            
                if event.key == pygame.K_SPACE:
                    for foo in self.path_group:
                        foo.scroll(0)
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

        #pygame.draw.arc(screen, WHITE,[400,300,100,100], 3.2, 0, 2)
            
        # -- flip display to reveal new position of objects
        pygame.display.flip()

#End Class

my_game = Game()
while my_game.running == True:
    my_game.new_game()
    
pygame.quit()

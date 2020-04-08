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
        self.my_Path = Path(self, 175, 200) #Creates first path block which others build from
        self.path_group.add(self.my_Path)
        self.all_sprites_group.add(self.my_Player)
        for count in range(250):
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def manualCurve1(self):
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 2, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(4):
            self.my_Path = Path(self, self.my_Path.rect.x + 3, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(3):
            self.my_Path = Path(self, self.my_Path.rect.x + 4, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 1, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def manualCurve2(self):
        for count in range(3):
            self.my_Path = Path(self, self.my_Path.rect.x + 4, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(4):
            self.my_Path = Path(self, self.my_Path.rect.x + 3, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)
        for count in range(5):
            self.my_Path = Path(self, self.my_Path.rect.x + 2, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def pathGap1(self):
        self.my_Path = Path(self, self.my_Path.rect.x + 60, self.my_Path.rect.y)
        for count in range(30):
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.width, self.my_Path.rect.y)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def downRamp(self):
        for count in range(125):
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y + 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def upRamp(self):
        for count in range(125):
            self.my_Path = Path(self, self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y - 1)
            self.path_group.add(self.my_Path)
            self.all_sprites_group.add(self.my_Path)

    def createPath_d(self): #Creates downwards compatible path segments randomly.
        paths = [self.manualCurve1, self.manualCurve2, self.downRamp]#self.PathGap1
        random.choice(paths)()

    def createPath_u(self): #Creates upwards compatible path segments randomly.
        paths = [self.manualCurve1, self.manualCurve2, self.upRamp]#self.PathGap1
        random.choice(paths)()

    #After certain x value. Harder path functions should start.
        
    def new_game(self):

        #self.play_Smusic() #Plays the shuffled song

        self.score = 0
        self.insx = 180 #Instructions appear each round

        # Create a sprite group of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        # Create a sprite group of the paths
        self.path_group = pygame.sprite.Group()

        # Create the Objects
        self.my_Player = Player(self)
        self.all_sprites_group.add(self.my_Player)
        self.player_path_collision_group = pygame.sprite.spritecollide(self.my_Player, self.path_group, False)

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
        #if player,rect.x + 20 != mypath 
        #IF BOTTOM RIGHT DOESNT HAVE COLLISION PLAYER CAN JUMP
        # Path and player collisions
        #for foo in self.path_group:
         #   self.collision = self.my_Player.rect.collidepoint(foo.rect.topright)
        #if self.collision != 0:
        #    print(self.collision)
        #self.collision = pygame.sprite.collide_rect(self.my_Player, self.my_Path)
        #print(self.collision)
        self.player_path_collision_group = pygame.sprite.spritecollide(self.my_Player, self.path_group, False)
        if self.player_path_collision_group: #If player and block collide...
            for foo in self.player_path_collision_group:
                self.my_Player.rect.bottom = foo.rect.top #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
                self.my_Player.g_Vel = 0 #Player's gravity velocity is 0 at collision      
        else: #If no collision...
                #self.my_Path.acc = 0 #Player shouldn't accelerate when not colliding:
            if self.my_Player.change_in_y < 0: #if no collision + going up... 
                #self.my_Player.current_y = 0
                #self.my_Player.last_y = 0 #makes change_in_y positive.
                self.my_Player.g_Vel = self.my_Path.vel #-8 #player should go up.
                #Player should move down quicker
                #if change in y > 0 allow movement if just collided?

        #SCORE
        self.score = self.my_Path.score
        if self.score > self.highscore: #New high score
            #self.draw_stats(50, 50, "NEW HIGH SCORE")
            self.highscore = self.score
            with open(path.join(self.dir, "highscore.txt"), 'w') as f:
                f.write(str(self.score))

        #Instructions
        self.insx += self.my_Path.vel #x pos of info will move appropriately

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
        
        #pygame.draw.line(screen, WHITE, (0,0), (200,200), 5)
        #pygame.draw.arc(screen, WHITE,[80,80,80,80], 0.5, 0.5, 10)
        #Draw player which can rotate
        screen.blit(self.my_Player.new_image, self.my_Player.rect)
        
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

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
        self.collision = False
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.mixer.music.load("TheFatRat - Unity.mp3")
        

    def new_game(self):

        pygame.mixer.music.play()

        # Create a sprite group of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        # Create a sprite group of the paths
        self.path_group = pygame.sprite.Group()

        # Create the Objects
        self.my_Player = Player()
        self.all_sprites_group.add(self.my_Player)

        self.my_Path = Path(100, 400)
        self.path_group.add(self.my_Path)
        self.all_sprites_group.add(self.my_Player)

        # SPAWN RAMP
                           
        for count in range(100):
            
            if self.my_Path.rect.y <= 100:
                self.turnDown = True
            elif self.my_Path.rect.y >= 500:
                self.turnDown = False
            if self.turnDown == False:
                #Makes ramp go up
                self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y - 1)
                self.path_group.add(self.my_Path)
                self.all_sprites_group.add(self.my_Path)
            elif self.turnDown == True:
                #Makes ramp go down
                self.my_Path = Path(self.my_Path.rect.x + self.my_Path.rect.width, self.my_Path.rect.y + 1)
                self.path_group.add(self.my_Path)
                self.all_sprites_group.add(self.my_Path)
            #if my_Path.rect.y == 400:
             #   my_Path = Path(my_Path.rect.x + my_Path.rect.width, my_Path.rect.y - 1)
                
        #Nextcount
             
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
            collision = True
            self.my_Player.player_set_v_gravity(0)
        else:
            collision = False
            
        if collision == True:
            for foo in player_path_collision_group:
                self.my_Player.rect.bottom = foo.rect.bottom #This method works. PLayers bottom right tho must be touching so it can move up if it is moved forwards.
        else:
            self.my_Player.player_set_v_gravity(2)

        
    def events(self):

        # -- User inputs here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN: # - A key is down
                if event.key == pygame.K_SPACE: # - If the space key pressed
                    for foo in self.path_group:
                        foo.scroll(3)
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
            
        # -- flip display to reveal new position of objects
            pygame.display.flip()

#End Class

my_game = Game()
while my_game.running == True:
    my_game.new_game()
    
pygame.quit()

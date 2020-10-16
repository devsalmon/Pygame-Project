import pygame as py  

# define constants  
WIDTH = 500  
HEIGHT = 500  
FPS = 30  

# define colors  
BLACK = (0 , 0 , 0)  
GREEN = (0 , 255 , 0)  

# initialize pygame and create screen  
py.init()  
screen = py.display.set_mode((WIDTH , HEIGHT))  
# for setting FPS  
clock = py.time.Clock()  

rot = 0  
rot_speed = 5

#TEST IMAGE
test_image = py.image.load("test.png")
#test_image.convert_alpha()
#image = pygame.Surface([width, height], pygame.SRCALPHA)

# define a surface (RECTANGLE)  
##image_orig = py.Surface((100 , 100))
image_orig = py.image.load("test.png")
# for making transparent background while rotating an image  
##test_image.set_colorkey(BLACK)
image_orig.set_colorkey(BLACK)  
# fill the rectangle / surface with green color  
##image_orig.fill(GREEN)  
# creating a copy of orignal image for smooth rotation  
#image = image_orig.copy()  
#image_orig.set_colorkey(BLACK)  
# define rect for placing the rectangle at the desired position  
rect = image_orig.get_rect()
#rect.center = (WIDTH // 2 , HEIGHT // 2)
#rect.center = (WIDTH // 2 , HEIGHT // 2)  
# keep rotating the rectangle until running is set to False  
running = True
while running:  
    # set FPS  
    clock.tick(FPS)  
    # clear the screen every time before drawing new objects  
    screen.fill(BLACK)  
    # check for the exit  
    for event in py.event.get():  
        if event.type == py.QUIT:  
            running = False  

    # making a copy of the old center of the rectangle  
    ###old_center = rect.center
    old_center = (300,200)
    # defining angle of the rotation  
    rot = (rot + rot_speed) % 360 
    # rotating the orignal image  
    new_image = py.transform.rotate(image_orig , rot)  
    rect = new_image.get_rect()
    # set the rotated rectangle to the old center  
    rect.center = old_center  
    # drawing the rotated rectangle to the screen  
    screen.blit(new_image , rect)
    ##screen.blit(test_image , (100, 200))
    # flipping the display after drawing everything  
    py.display.flip()  

py.quit()  

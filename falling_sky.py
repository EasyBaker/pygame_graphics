#Anders Blom
#Super Gnarly Code


# Imports
import pygame
import pygame, math
import random
from random import randrange


# Initialize game engine
pygame.init()

#Image
knuckles = pygame.image.load('knuckles.png')
meteor = pygame.image.load('meteor.png')

# Window
SIZE = (800, 600)
TITLE = "Moving Block"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)
BLACK = (0, 0, 0)

# Block
block_loc = [380, 500]
vel = [0, 0]
speed = 10

def draw_snowflake(flake):
    x = flake[0]
    y = flake[1]

    screen.blit(meteor, (x, y))

def draw_block(loc):
    x = block_loc[0]
    y = block_loc[1]
    
    screen.blit(knuckles, (x,y))

''' make ground '''
ground = pygame.Surface([800, 200])
ground.fill(GREEN)

''' Make snow '''
snow = []
num_flakes = 5
def draw_meteors():
    num_meteors = random.randrange(1, 6)
    for i in range(num_meteors):
            x = random.randrange(0, 800)
            y = random.randrange(-100, 100)
            stop = 610
            flake = [x, y, stop]
            snow.append(flake)
draw_meteors()
count = 0
is_snowing = True
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                vel[0] = speed
            if event.key == pygame.K_a:
                vel[0] =-1 *  speed
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                vel[0] = 0
            if event.key == pygame.K_a:
                vel[0] = 0
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    shot_fired = True
                
    # Game logic
    block_loc[0] += vel[0]

    if is_snowing:
        ''' move rain '''
        for s in snow:
            s[1] += 1

            if s[1] >= s[2]:
                s[0] = random.randrange(0, 800)
                s[1] = random.randrange(-100, 100)
                count += 1
    if count == 6:
        draw_meteors()
        count = 0

    # Drawing code
    screen.fill(BLACK)
    draw_block(block_loc)
    
    ''' grass '''
    #pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    #screen.blit(ground, [0, 400])

    ''' rain ''' 
    for s in snow:
        draw_snowflake(s)
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

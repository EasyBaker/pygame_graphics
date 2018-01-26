# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Snowy Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREEN = (100, 125, 75)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (75, 200, 255)
DARK_BLUE = (0, 0, 100)
GRAY = (150, 150, 150)
DARK_GRAY = (75, 75, 75)
NOT_QUITE_DARK_GRAY = (100, 100, 100)
YELLOW = (200, 200, 100)

#settings
sticky = True
stormy = True

def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])

def draw_snowflake(flake):
    rect = flake[:4]
    pygame.draw.ellipse(screen, WHITE, rect)

''' make ground '''
ground = pygame.Surface([800, 200])
ground.fill(GREEN)

''' Make clouds '''
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)

''' Make snow '''
num_flakes = 700
snow = []

for i in range(num_flakes):
    x = random.randrange(-100, 900)
    y = random.randrange(-100, 600)
    r = random.randrange(4, 7)
    stop = random.randrange(400, 625)
    flake = [x, y, r, r, stop]
    snow.append(flake)

lightning_timer = 0
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    ''' move clouds '''
    for c in far_clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    for c in near_clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)

    ''' move rain '''
    for s in snow:
        s[0] += random.randrange(-1, 2)
        s[1] += random.randrange(1, 2)

        if s[1] >= s[4]:
            if sticky:
                pygame.draw.ellipse(ground, WHITE, [s[0], s[1] - 402, s[3], s[3]])

            s[0] = random.randrange(-100, 900)
            s[1] = random.randrange(-100, 0)

    ''' flash lighting '''
    if stormy:
        if random.randrange(0, 150) == 0:
            lightning_timer = 5
        else:
            lightning_timer -= 1
             
    # Drawing code
    ''' sky '''
    if lightning_timer > 0:
        screen.fill(YELLOW)
    else:
        screen.fill(GRAY)

    ''' sun '''
    #pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    #pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])
    screen.blit(ground, [0, 400])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    
    ''' clouds '''
    for c in far_clouds:
        draw_cloud(c, NOT_QUITE_DARK_GRAY)

    ''' rain ''' 
    for s in snow:
        draw_snowflake(s)

    ''' clouds '''
    for c in near_clouds:
        draw_cloud(c, WHITE)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

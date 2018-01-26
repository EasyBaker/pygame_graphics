# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
BROWN = (99, 45, 3)
YELLOW = (235, 255, 200)

def draw_christmas_tree(x,y):
    pygame.draw.rect(screen, BROWN, [50, 480, 50, 80])
    pygame.draw.polygon(screen, GREEN, [[x+80, y], [x+160, y+80], [x, y+80]])
    pygame.draw.polygon(screen, GREEN, [[x+80, y-40], [x+140, y+40], [x+20, y+40]])
    pygame.draw.polygon(screen, GREEN, [[x+80, y-80], [x+120, y], [x+40, y+0]])
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40, 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

def draw_flower(x, y):
    pygame.draw.rect(screen, GREEN, [x + 8, y + 40, 4, 30])
    pygame.draw.ellipse(screen, RED, [x + 3, y + 35, 15, 15])

def draw_moon(x, y):
    pygame.draw.ellipse(screen, YELLOW, [x, y, 100, 100])
    
        
''' make stars '''
'''stars = []
for i in range(200):
    x = random.randrange(0, 800)
    y = random.randrange(0, 400)
    r = random.randrange(1, 5)
    stars.append([x, y, r, r])'''

'''rain'''
rain = []
for i in range(200):
    x = random.randrange(0,800)
    y = random.randrange(0,500)
    r = random.randrange(1,5)
    rain.append([x, y, r, r])

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Drawing Code
    ''' Sky '''
    screen.fill(BLACK)

    ''' stars '''
    stars = []
    for i in range(200):
        x = random.randrange(8, 100)
        y = random.randrange(180, 400)
        r = random.randrange(1, 5)
        stars.append([x, y, r, r])
    for s in stars:
        pygame.draw.ellipse(screen, BLUE, s)

    for i in range(200):
        x = random.randrange(255,342)
        y = random.randrange(100, 500)
        r = random.randrange(1,5)
        stars.append([x, y, r, r])
    for s in stars:
        pygame.draw.ellipse(screen, BLUE, s)

    for i in range(200):
        x = random.randrange(355,445)
        y = random.randrange(155, 485)
        r = random.randrange(1,5)
        stars.append([x, y, r, r])
    for s in stars:
        pygame.draw.ellipse(screen, BLUE, s)

    for i in range(200):
        x = random.randrange(455,545)
        y = random.randrange(205, 535)
        r = random.randrange(1,5)
        stars.append([x, y, r, r])
    for s in stars:
        pygame.draw.ellipse(screen, BLUE, s)

    for i in range(200):
        x = random.randrange(655,745)
        y = random.randrange(130, 460)
        r = random.randrange(1,5)
        stars.append([x, y, r, r])
    for s in stars:
        pygame.draw.ellipse(screen, BLUE, s)

    ''' snowy ground '''
    pygame.draw.rect(screen, WHITE, [0, 400, 800, 200])

    '''Flowers'''
    draw_flower(5, 393)
    draw_flower(697, 450)
    draw_flower(452, 421)
    draw_flower(522, 390)
    draw_flower(300, 470)
    draw_flower(225, 390)
    draw_flower(158, 436)
    draw_flower(265, 450)
    draw_flower(497, 372)
    draw_flower(680, 420)
    draw_flower(634, 530)

    '''rain'''
    for r in rain:
        pygame.draw.ellipse(screen, YELLOW, r)

    ''' moon '''
    draw_moon(575, 75)

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        post = [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]]
        pygame.draw.polygon(screen, GREEN, post)

    pygame.draw.rect(screen, GREEN, [0, y+10, 800, 5])
    pygame.draw.rect(screen, GREEN, [0, y+30, 800, 5])

    ''' cloud '''
    draw_cloud(5, 150)
    draw_cloud(250, 75)
    draw_cloud(350, 125)
    draw_cloud(450, 175)
    draw_cloud(650, 100)
    
    ''' christmas tree '''
    draw_christmas_tree(0,460)
    
    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    pygame.draw.rect(screen, RED, [300, 300, 200, 200])
    pygame.draw.rect(screen, BLACK, [300, 300, 200, 200], 5)
    pygame.draw.rect(screen, BROWN, [350, 350, 100, 150])
    pygame.draw.rect(screen, BLACK, [350, 350, 100, 150], 5)
    pygame.draw.ellipse(screen, YELLOW, [365, 400, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [365, 400, 21, 21], 2)
    pygame.draw.polygon(screen, BLUE, [[250, 300], [400,150], [550, 300]])
    pygame.draw.polygon(screen, BLACK, [[250, 300], [400,150], [550, 300]], 5)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()


# Imports
import pygame
import math

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
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
BROWN = (99, 45, 3)
YELLOW = (234, 237, 49)
    

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [300, 300, 200, 200])
    pygame.draw.rect(screen, GREEN, [0, 500, 1000,1000])
    pygame.draw.rect(screen, BROWN, [350, 350, 100, 150])
    pygame.draw.ellipse(screen, YELLOW, [365, 400, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [365, 400, 21, 21], 2)
    pygame.draw.line(screen, YELLOW, [350, 0], [250,0], 10)
    pygame.draw.line(screen, YELLOW, [325, 75], [230,50], 10)
    pygame.draw.line(screen, YELLOW, [300, 145], [210,100], 10)
    pygame.draw.line(screen, YELLOW, [275, 220], [190,150], 10)
    pygame.draw.ellipse(screen, YELLOW, [-200, -200, 400, 400])
    
    pygame.draw.polygon(screen, BLUE, [[250, 300], [400,150], [550, 300]])

    ''' angles for arcs are measured in radians (a pre-cal topic) '''


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()

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
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 100

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
PINK = (226, 31, 168)
PURPLE = (154, 0, 153)
BLACK = (0, 0, 0)

# Make clouds
num_clouds = 20
clouds = []
for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 200)
    s = random.randrange(1,4)
    
    loc = [x, y]
    clouds.append(loc)

def draw_cloud(loc):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, PINK, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, PINK, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, PINK, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, PINK, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, PINK, [x + 20, y + 20, 60, 40])

stars = []
for i in range(400):
    x = random.randrange(-800, 800)
    y = random.randrange(-100, 400)
    r = random.randrange(1, 5)
    s = [x, y, r, r]
    stars.append(s)
    

   
# Game loop
done = False

while not done:
    ''' sky '''
    screen.fill(BLACK)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic
    for c in clouds:
        c[0] += 2

        if c[0] > 900:
           c[0] = random.randrange(-900, -100)
           c[1] = random.randrange(-50, 200)

    for s in stars:
        s[1] +=2
        s[0] +=1

        s[0] += random.randrange(0,2)
        s[1] += random.randrange(0,2)

        v = random.randrange(410, 1010)
        if s[1] >= v:
            s[0] = random.randrange(-800, 800)
            s[1] = random.randrange(-100, 0)
            pygame.draw.ellipse(screen, WHITE, s)
    
        
             
    # Drawing code
    ''' rain '''
    for s in stars:
        pygame.draw.ellipse(screen, WHITE, s)

    ''' clouds '''
    for c in clouds:
        draw_cloud(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()

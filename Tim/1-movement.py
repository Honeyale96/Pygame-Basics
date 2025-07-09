import pygame

pygame.init()

# This line creates a window of 500 width, 500 height
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game")

x = 50
y = 50
width = 40
height = 60
vel = 5


run = True
while run:

    # This will delay the game the given amount of milliseconds. In our case 0.1 seconds will be the delay
    pygame.time.delay(50)

    for event in pygame.event.get(): # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False # Ends the game loop

    # Movement

    # This will give us a dictionary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    screen.fill((0,0,0))    # # Fills the screen with black,necessary rectangle does not leave a trail
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height)) # This takes: window/surface, color, rect
    pygame.display.update() # This updates the screen so we can see our rectangle

pygame.quit() # If we exit the loop this will execute and close our game


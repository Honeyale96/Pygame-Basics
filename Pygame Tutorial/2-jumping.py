import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

# These go near the top of your program, outside the while loop
jumping = False
jumpCount = 10

run = True
while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Movement
    keys = pygame.key.get_pressed()

    # Making sure the top left position of our character is greater than our vel so we never move off the screen.
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    # Making sure the top right corner of our character is less than the screen width - its width
    if keys[pygame.K_RIGHT] and x < 800 - width - vel:
        x += vel
    # Checks if user is not jumping
    if not jumping:
        # Same principles apply for the y coordinate
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 800 - height  - vel:
            y += vel
        # Goes inside the while loop, under event for moving down
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        # This is what will happen if we are jumping
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            # Resetting our Variables
            jumping = False
            jumpCount = 10


    screen.fill((0,0,0))    # necessary to draw over the rectangle so it's not leaving a trail
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
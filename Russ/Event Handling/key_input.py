# There are two different ways of getting keyboard input in pygame:
    # Use Event Handler - more for single presses like Shooting or jumping
    # Use key.get_pressed() -  to move the player while a key is held down.

import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


running = False
sprinting = False

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #   Using the event handler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                running = True
            if event.key == pygame.K_LSHIFT:
                sprinting = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                running = False
            if event.key == pygame.K_LSHIFT:
                sprinting = False

    if sprinting and running:
        print('Sprinting')
    elif running:
        print('Running')

    # #   Using the key_pressed() function
    # key = pygame.key.get_pressed()
    # if key[pygame.K_a] == True and key[pygame.K_LSHIFT] == True:
    #     print("Sprinting")
    # elif key[pygame.K_a]:
    #     print("Running")

pygame.quit()
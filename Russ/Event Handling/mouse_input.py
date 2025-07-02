# There are two different ways of getting mouse input in pygame:
#   Using the event handler - more for detecting clicks, scrolls, and one-time actions.
#   Calling state mouse functions - more for dragging, aiming, or holding buttons.

import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:

    if pygame.mouse.get_pressed()[0]:
        print("Left mouse click")
    if pygame.mouse.get_pressed()[2]:
        print("Right mouse click")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Click")
        if event.type == pygame.MOUSEBUTTONUP:
            print("Release")

pygame.quit()
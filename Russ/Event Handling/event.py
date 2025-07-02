import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:

    # # Shows how all "event" are read when the program runs
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False
    #     print(event)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print("Key has been pressed")
        if event.type == pygame.KEYUP:
            print("Key has been released")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse has been clicked")
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse has been released")
        if event.type == pygame.MOUSEMOTION:
            print("Mouse is moving")


pygame.quit()
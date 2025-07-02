# Typically a pygame project will contain images and spritesheets,
# but for simpler shapes we can use the built-in draw module.
#   One of the key concepts in pygame is working with rectangles.
#   They allow you to position and move things around the screen, and they are also used for collision detection.

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Shapes")

run = True
while run:

  screen.fill((255, 255, 255))

  pygame.draw.rect(screen, (255, 0, 0), (200, 100, 150, 150))
  pygame.draw.circle(screen, (0, 0, 0), (500, 500), 75)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.flip()

pygame.quit()
# This is a key concept of how rectangles are used in pygame.
# In a finished game what you are seeing is just the sprites,
# but their positions and collisions are actually being done by the rectangles behind the scenes.
# We move the rectangle first, then we draw the image in its place.

import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Working With Rectangles")
soldier = pygame.image.load("soldier.png").convert_alpha()

rect_2 = soldier.get_rect()

rect_2.topleft = (200, 200)

clock = pygame.time.Clock()

run = True
while run:

  #refresh the screen at 60 FPS
  clock.tick(60)

  #fill the background white
  screen.fill((255, 255, 255))

  #player controls
  key = pygame.key.get_pressed()
  if key[pygame.K_a] == True:
      rect_2.move_ip(-5, 0)
  if key[pygame.K_d] == True:
      rect_2.move_ip(5, 0)
  if key[pygame.K_w] == True:
      rect_2.move_ip(0, -5)
  if key[pygame.K_s] == True:
      rect_2.move_ip(0, 5)

  #draw the rectangle and soldier image
  pygame.draw.rect(screen, (0, 255, 255), rect_2)
  screen.blit(soldier, rect_2)

  for event in pygame.event.get():
   if event.type == pygame.QUIT:
      run = False

  #refresh display
  pygame.display.flip()

pygame.quit()
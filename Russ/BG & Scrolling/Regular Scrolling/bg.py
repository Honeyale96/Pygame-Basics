import pygame
import math

# -----------------------
# Game Configurations
# -----------------------
pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

# -----------------------
# Initializations
# -----------------------
# Load image
bg = pygame.image.load("bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

# Game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1


# -----------------------
# Game Loop
# -----------------------
run = True
while run:

  clock.tick(FPS)

  # Draw scrolling background
  for i in range(0, tiles):
    screen.blit(bg, (i * bg_width + scroll, 0))
    bg_rect.x = i * bg_width + scroll
    pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

  # Scroll background
  scroll -= 5

  # Reset scroll
  if abs(scroll) > bg_width:
    scroll = 0

  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  pygame.display.update()
pygame.quit()
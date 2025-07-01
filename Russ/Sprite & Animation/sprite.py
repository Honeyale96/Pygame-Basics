import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()

BG = (50, 50, 50)
BLACK = (0, 0, 0)

def get_image(sheet, frame, width, height, scale, color):
    # create a black box surface
    image = pygame.Surface((width, height)).convert_alpha()
    # take the image from spritesheet and add it to the "black box"
    image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
    # scale image to be bigger
    image = pygame.transform.scale(image, (width *scale, height * scale))
    # remove the black box
    image.set_colorkey(color)

    return image


frame_0 = get_image(sprite_sheet_image, 0, 24, 24, 3, BLACK)
frame_1 = get_image(sprite_sheet_image, 1, 24, 24, 3, BLACK)
frame_2 = get_image(sprite_sheet_image, 2, 24, 24, 3, BLACK)
frame_3 = get_image(sprite_sheet_image, 3, 24, 24, 3, BLACK)

run = True
while run:

    # Update Background
    screen.fill(BG)

    # Display Image
    screen.blit(sprite_sheet_image, (0, 0))

    # Show Frame Image
    screen.blit(frame_0, (0, 25))
    screen.blit(frame_1, (75, 25))
    screen.blit(frame_2, (150, 25))
    screen.blit(frame_3, (225, 25))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()

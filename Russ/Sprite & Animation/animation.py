import pygame
import spritesheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet_image = pygame.image.load('doux.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)


BG = (50, 50, 50)
BLACK = (0, 0, 0)

# Create animation list
animation_list = []
animation_steps = [4, 6, 3, 4, 7]  # how many frames in sequence - 4 idle, 6 run, 3 jump, 4 hurt, 7 crouch
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 250
frame = 0
step_counter = 0

# Main loop to add animation steps into a temp list -> animation list
for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_img_list)

# Can see after the for loop animation list has 5 sub lists for - idle, run, jump, hurt, crouch.
print(animation_list)

run = True
while run:

    # Update Background
    screen.fill(BG)

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # Display Image
    screen.blit(sprite_sheet_image, (0, 0))

    # Show Frame Image
    screen.blit(animation_list[action][frame], (0, 25))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # press up and down keys to scroll through animations
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    pygame.display.update()
pygame.quit()
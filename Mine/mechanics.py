# 1. 🎮 Game Setup

import pygame

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 490
FPS = 60
scroll = 0
SCROLL_SPEED = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Run")

#----------------------------------------------------------------------


# # 2. 🌍 Asset Loading & World Creation

# Load the image for the ground and convert it for faster blitting
ground_image = pygame.image.load("Assets/images/ground.png").convert_alpha()

# Get the width and height of the ground image
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()


# Create an empty list to store background layers
bg_images = []

# Load each parallax background image and store it in the list
for i in range(1, 6):
    bg_image = pygame.image.load(f"Assets/images/plx-{i}.png").convert_alpha()
    bg_images.append(bg_image)

# Get the width of one background layer (assumes all layers are same width)
bg_width = bg_images[0].get_width()

# Y-position where the ground should be drawn (flush with bottom of screen)
ground_y = SCREEN_HEIGHT - (ground_height - 10)


#----------------------------------------------------------------------


# # 3. 🎨 Drawing the World

def draw_bg():
    for index, img in enumerate(bg_images):
        # Speed increases slightly for layers further back (parallax effect)
        speed = 1 + index * 0.2

        # Calculate horizontal offset for this layer using scroll value
        offset = (-scroll * speed) % bg_width

        # Start drawing on the left side of the screen
        x = offset - bg_width

        # Repeat background image until screen is filled
        while x < SCREEN_WIDTH:
            screen.blit(img, (x, 0))
            x += bg_width


def draw_ground():
    speed = 2.5  # Slightly faster than the background layers
    offset = (-scroll * speed) % ground_width
    x = offset - ground_width

    # Tile the ground image across the screen
    while x < SCREEN_WIDTH:
        screen.blit(ground_image, (x, SCREEN_HEIGHT - ground_height))
        x += ground_width


#----------------------------------------------------------------------


# # 4. 🕹️ Sprite Setup & Animation


# ## `SpriteSheet` Helper

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image  # Store the full loaded sprite sheet

    def get_image(self, frame, width, height, scale, color):
        # Create a new surface to extract a single frame
        image = pygame.Surface((width, height)).convert_alpha()
        # Copy the frame from the sheet into the surface
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        # Resize the frame for better visibility (optional)
        image = pygame.transform.scale(image, (width * scale, height * scale))
        # Remove the background color (e.g., black)
        image.set_colorkey(color)
        return image


# ## In Dino `__init__`:

# Animation state constants (easier to manage than magic numbers)
IDLE, RUN, JUMP, HURT, CROUCH = range(5)

# Number of frames per animation
animation_steps = [4, 6, 3, 4, 7]  # idle, run, jump, hurt, crouch

# Load sprite sheet image
sprite_sheet_image = pygame.image.load("Assets/images/doux.png").convert_alpha()
self.sheet = SpriteSheet(sprite_sheet_image)


self.animation_list = []
frame_index = 0

# Loop through each action's frame count
for animation in animation_steps:
    temp = []  # Store frames for one action (e.g., RUN or JUMP)
    for _ in range(animation):
        frame = self.sheet.get_image(frame_index, 24, 24, 3, (0, 0, 0))  # BLACK background
        temp.append(frame)
        frame_index += 1
    self.animation_list.append(temp)  # Add this action’s frames to the master list


self.action = self.RUN         # Start on the RUN animation
self.frame = 0                 # Index of the current animation frame
self.last_update = pygame.time.get_ticks()  # When the last frame changed
self.animation_cooldown = 100  # How long to wait before switching frames (in ms)


def _update_animation(self):
    current_time = pygame.time.get_ticks()  # Current time in milliseconds

    # If it's been long enough, switch to the next animation frame
    if current_time - self.last_update >= self.animation_cooldown:
        self.frame = (self.frame + 1) % len(self.animation_list[self.action])
        self.last_update = current_time  # Reset the timer

    # Update the current image to show on screen
    self.image = self.animation_list[self.action][self.frame]




#----------------------------------------------------------------------


# # 5. 🧪 Character Physics


# ## 5a. Jumping

self.vel_y = 0           # Vertical velocity
self.gravity = 0.6       # Downward acceleration
self.jump_vel = -12      # Upward force when jumping
self.on_ground = True    # True if character is on the ground
self.jump_count = 0      # Number of jumps made (used for double jump)


def jump(self):
    if self.jump_count < 2:               # Allow double jump (2 max)
        self.vel_y = self.jump_vel        # Apply upward velocity
        self.on_ground = False            # Mark as airborne
        self.jump_count += 1              # Track how many jumps used



# ## 5b. Gravity

def _apply_gravity(self):
    self.vel_y += self.gravity        # Accelerate downward
    self.rect.y += self.vel_y         # Apply velocity to vertical position

    # Check if Dino hits the ground
    if self.rect.bottom >= self.ground_y:
        self.rect.bottom = self.ground_y  # Stick to ground
        self.vel_y = 0                    # Stop falling
        self.on_ground = True            # Mark as grounded
        self.jump_count = 0              # Reset jump count


#----------------------------------------------------------------------


# # 6. 🧠 Character Control & State

def update(self, keys):
    prev_action = self.action  # Track previous state to reset frame if it changes

    # --- Animation State Logic ---
    if not self.on_ground:
        self.action = self.JUMP
        self.world_x += self.scroll_speed  # Keep Dino moving in mid-air
    elif keys[pygame.K_DOWN]:
        self.action = self.CROUCH
        self.world_x += self.scroll_speed  # Move forward while crouching
    else:
        self.action = self.RUN
        self.world_x += self.scroll_speed  # Default running state

    # If action changed (e.g., from RUN → JUMP), reset the frame counter
    if self.action != prev_action:
        self.frame = 0

    self._apply_gravity()     # Apply falling physics
    self._update_animation()  # Advance the sprite frame


#----------------------------------------------------------------------


# # 7. 🖼️ Drawing the Character

def draw(self, surface, scroll):
    # Convert world position to screen position
    screen_x = self.world_x - scroll

    # Draw the current sprite frame at that screen position
    surface.blit(self.image, (screen_x, self.rect.y))


#----------------------------------------------------------------------


# # 8. 🔁 Game Loop

run = True
while run:
    clock.tick(FPS)
    scroll += SCROLL_SPEED  # Move the background world to the left


    keys = pygame.key.get_pressed()  # Get current state of all keys
    dino.update(keys)  # Tell the Dino to update itself

    # Drawing the Frame
    draw_bg()  # Parallax background
    draw_ground()  # Infinite scrolling ground
    dino.draw(screen, scroll)  # Draw the character based on scroll

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # Exit the game

        # Handle jump key press
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_UP):
            dino.jump()

    pygame.display.update()  # Push everything drawn to the screen
pygame.quit()  # Safely shuts down Pygame

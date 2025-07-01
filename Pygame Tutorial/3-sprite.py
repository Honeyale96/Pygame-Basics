import pygame

pygame.init()

screen = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Game")

walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'),
             pygame.image.load('Game/R4.png'), pygame.image.load('Game/R5.png'), pygame.image.load('Game/R6.png'),
             pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]
walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'),
            pygame.image.load('Game/L4.png'), pygame.image.load('Game/L5.png'), pygame.image.load('Game/L6.png'),
            pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5

jumping = False
jumpCount = 10

left = False
right = False
walkCount = 0


def draw():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames,
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount
    screen.blit(bg, (0, 0)) # This will draw our background image at (0,0)

    if walkCount + 1 >= 27:
        walkCount = 0

    if left: # If we are facing left
        screen.blit(walkLeft[walkCount // 3], (x, y)) # divide walkCounter by 3
        walkCount += 1                                  # to ensure each image is shown 3 times every animation
    elif right:
        screen.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        screen.blit(char, (x, y)) # If the character is standing still

    pygame.display.update()


# mainloop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
    else:
        right = False
        left = False
        walkCount = 0

    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumping = False
            jumpCount = 10

    draw()

pygame.quit()
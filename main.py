import pygame

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((600, 400))

# Title and logo
pygame.display.set_caption("Shooty McShoot face")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("icon.png")
playerImg = pygame.transform.scale(playerImg, (30, 30))
playerX = 300.0
playerY = 200.0
playerX_c = 0
playerY_c = 0

def player(x, y):
    screen.blit(playerImg, (x, y))
    # rect = playerImg.get_rect()
    # rect = rect.move((x, y))
    # screen.blit(picture, rect)


# Game loop
running = True
while running:
    # fills background
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_c = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_c = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerX_c = 0
    playerX += playerX_c
    player(playerX, playerY)
    pygame.display.update()

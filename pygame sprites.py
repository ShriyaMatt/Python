import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (R, G, B)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Rectangles Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Player rectangle (controlled by arrow keys)
player_size = (50, 50)
player_pos = [100, 100]
player_speed = 5

# Static rectangle (does not move)
static_size = (50, 50)
static_pos = [400, 300]

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key states for continuous movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Keep player inside the screen boundaries
    player_pos[0] = max(0, min(player_pos[0], SCREEN_WIDTH - player_size[0]))
    player_pos[1] = max(0, min(player_pos[1], SCREEN_HEIGHT - player_size[1]))

    # Drawing
    screen.fill(WHITE)  # Clear screen
    pygame.draw.rect(screen, RED, (*player_pos, *player_size))   # Player
    pygame.draw.rect(screen, BLUE, (*static_pos, *static_size))  # Static rectangle

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Sprites with Color Change Event")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Define a custom event for changing colors
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Trigger every 2 seconds

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        # Random RGB color
        self.color = (random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite(200, HEIGHT // 2, 80, 80, (255, 0, 0))  # Red
sprite2 = ColorSprite(400, HEIGHT // 2, 80, 80, (0, 0, 255))  # Blue

# Group for easy drawing and updating
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle custom event
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Fill background
    screen.fill((30, 30, 30))

    # Draw sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit FPS
    clock.tick(60)
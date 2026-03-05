import pygame
import sys

# Initialize Pygame
pygame.init()

# Window parameters
WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
BACKGROUND_COLOR = (58, 58, 58)  # Grey background
IMAGE_SIZE = (300, 300)

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("my first pygame")

# Load and resize the image
try:
    image = pygame.image.load("your_image.png")  
except pygame.error as e:
    print(f"Error loading image: {e}")
    pygame.quit()
    sys.exit()

image = pygame.transform.scale(image, IMAGE_SIZE)

# Get image rect and center it
image_rect = image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Draw image
    screen.blit(image, image_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
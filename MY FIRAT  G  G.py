import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("my first game screen")

# Colors (R, G, B)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)  # Light blue color
BLACK = (0, 0, 0)

# Rectangle size and position (centered)
rect_width, rect_height = 200, 100
rect_x = (WIDTH - rect_width) // 2
rect_y = (HEIGHT - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Font setup
font = pygame.font.SysFont(None, 36)  # Default font, size 36
text_surface = font.render("Hello, Pygame!", True, BLACK)
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, LIGHT_BLUE, rectangle)

    # Draw text
    screen.blit(text_surface, text_rect)

    # Update display
    pygame.display.flip()
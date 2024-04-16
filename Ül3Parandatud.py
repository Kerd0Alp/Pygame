import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Ülesanne3-Kerdo-Alp")

# Colors
BLACK = (255, 0, 0)

# Number of rows and columns in the mesh
ROWS = 25
COLUMNS = 27

# Initial size of the square holes
SQUARE_SIZE = 20

# Function to draw the mesh with square holes
def drawMesh(screen, square_size):
    screen.fill([153, 255, 153])  # Fill the screen with white color

    # Calculate the size of each grid cell
    cell_width = 640 // COLUMNS
    cell_height = 480 // ROWS

    # Draw the grid
    for row in range(ROWS + 1):  # Add 1 to draw the last row up to the edge
        for col in range(COLUMNS + 1):  # Add 1 to draw the last column up to the edge
            rect = pygame.Rect(col * cell_width, row * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Draw the grid lines

# Initial drawing
drawMesh(screen, SQUARE_SIZE)
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                SQUARE_SIZE += 5  # Increase the size of the square holes
            elif event.key == pygame.K_DOWN:
                SQUARE_SIZE = max(5, SQUARE_SIZE - 5)  # Decrease the size, but keep it at least 5
            drawMesh(screen, SQUARE_SIZE)
            pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()


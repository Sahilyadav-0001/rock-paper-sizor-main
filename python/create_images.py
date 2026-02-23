import pygame
import os

# Initialize pygame
pygame.init()

# Create directory for images if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Function to create and save an image
def create_and_save_image(name, color, shape_function):
    # Create a surface with transparency
    surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    
    # Draw the shape
    shape_function(surface, color)
    
    # Save the image
    pygame.image.save(surface, f"{name}.png")
    print(f"Created {name}.png")

# Rock image (circle)
def draw_rock(surface, color):
    pygame.draw.circle(surface, color, (100, 100), 80)
    pygame.draw.circle(surface, (0, 0, 0), (100, 100), 80, 3)  # Border

# Paper image (square)
def draw_paper(surface, color):
    pygame.draw.rect(surface, color, (20, 20, 160, 160), border_radius=15)
    pygame.draw.rect(surface, (0, 0, 0), (20, 20, 160, 160), 3, border_radius=15)  # Border
    
    # Add some lines to make it look like paper
    for i in range(40, 160, 30):
        pygame.draw.line(surface, (0, 0, 0), (40, i), (160, i), 2)

# Scissors image (two intersecting ovals)
def draw_scissors(surface, color):
    # Draw two ovals for scissors
    pygame.draw.ellipse(surface, color, (30, 50, 140, 60))
    pygame.draw.ellipse(surface, (0, 0, 0), (30, 50, 140, 60), 3)  # Border
    
    pygame.draw.ellipse(surface, color, (30, 90, 140, 60))
    pygame.draw.ellipse(surface, (0, 0, 0), (30, 90, 140, 60), 3)  # Border
    
    # Add a small circle for the pivot
    pygame.draw.circle(surface, (50, 50, 50), (100, 100), 10)
    pygame.draw.circle(surface, (0, 0, 0), (100, 100), 10, 2)  # Border

# Create the images
create_and_save_image("rock", (173, 216, 230), draw_rock)       # Light blue
create_and_save_image("paper", (255, 255, 200), draw_paper)     # Light yellow
create_and_save_image("scissors", (200, 255, 200), draw_scissors)  # Light green

print("All images created successfully!")

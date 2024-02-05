import pygame
import sys
from NovaCentre import NovaCentre  # Assuming NovaCentre.py is in the same directory and properly structured

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nova Centre Game")
clock = pygame.time.Clock()

# Initialize NovaCentre
nova_centre = NovaCentre()
nova_centre.load_world("game_world.xml")  # This should be the path to your XML file defining the game world

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle other events like keyboard and mouse here

    # Update game state and draw the current scene
    screen.fill((0, 0, 0))  # Clear screen with black
    
    # Here you would update and draw your game world based on nova_centre.game_state
    
    pygame.display.flip()  # Update the full display Surface to the screen
    clock.tick(60)  # Cap the frame rate to 60 frames per second

pygame.quit()
sys.exit()

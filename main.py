import pygame
import sys
from random import randint

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Coin Collector Game")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(50, 50, 30, 30)  # Initial position
        self.speed = 3

    def move_towards_coin(self, coin_rect):
        # Simple AI logic: Move towards the coin
        dx = coin_rect.centerx - self.rect.centerx
        dy = coin_rect.centery - self.rect.centery
        dist = max(1, pygame.math.Vector2(dx, dy).length())
        self.rect.move_ip(dx / dist * self.speed, dy / dist * self.speed)

# Coin class
class Coin:
    def __init__(self):
        self.rect = pygame.Rect(700, 500, 20, 20)  # Initial position

# Initialize player and coin
player = Player()
coin = Coin()

# Counter
counter = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player position
    player.move_towards_coin(coin.rect)

    # Check collision
    if player.rect.colliderect(coin.rect):
        counter += 1
        coin.rect.x = randint(100, 500)  # Move the coin to a new position

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, blue, player.rect)
    pygame.draw.rect(screen, (255, 0, 0), coin.rect)
    pygame.display.flip()

# Clean up
pygame.quit()

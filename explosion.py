import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    def __init__(self, ai_game, x, y):
        super().__init__()
        self.screen = ai_game.screen

        # Create a font-rendered red "*"
        font = pygame.font.SysFont(None, 72)  # 72px tall
        self.image = font.render("*", True, (255, 0, 0))  # red star
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Explosion lifetime
        self.duration = 25  # milliseconds
        self.start_time = pygame.time.get_ticks()

    def update(self):
        """Remove the explosion after its duration expires."""
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time > self.duration:
            self.kill()

    def draw(self):
        """Draw the explosion on the screen."""
        self.screen.blit(self.image, self.rect)
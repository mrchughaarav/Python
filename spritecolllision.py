import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("bg.jpg"),
                    (SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.Sysfont("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init()
        self.image = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.image.fill(
            pygame.color("dodgerblue"))
        pygame.draw.rect(self.image, color, pygame.rect(0, 0, height, width))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change)
        )
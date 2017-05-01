import pygame

from entities.bullet import Bullet
import globals


class Character(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.image = pygame.Surface([40, 40])

        self.image.fill(color)
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

    def shoot(self, target, color):
        shot = Bullet(self.rect, target, color)

        globals.all_sprites.add(shot)
        globals.bullets.add(shot)

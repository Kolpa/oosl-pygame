import pygame
from threading import Timer
from entities.bullet import Bullet
import globals


class Character(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()

        self.color = color

        self.image = pygame.Surface([40, 40])

        self.image.fill(self.color)
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

    def shoot(self, target, color):
        shot = Bullet(self.rect, target, color)

        globals.all_sprites.add(shot)
        globals.bullets.add(shot)

    def hurt(self):
        self.image.fill((255, 0, 0))
        Timer(0.25, self.old_color, ()).start()

    def old_color(self):
        self.image.fill(self.color)

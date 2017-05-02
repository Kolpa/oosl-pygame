import pygame
import math
import globals


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, target, color):
        super().__init__()

        self.color = color

        self.image = pygame.Surface([5, 10])

        self.image.fill(color)
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()
        self.rect.centerx = pos.centerx
        self.rect.centery = pos.centery

        angle = math.atan2(target[0] - self.rect.centerx, target[1] - self.rect.centery) * 180 / math.pi
        self.image = pygame.transform.rotate(self.image, angle)

        self.target = pygame.math.Vector2(target[0], target[1])
        self.me = pygame.math.Vector2(self.rect.centerx, self.rect.centery)

        self.tick = self.target - self.me
        self.tick = self.tick.normalize()

    def update(self):
        self.rect.centerx += self.tick[0] * 10
        self.rect.centery += self.tick[1] * 10

        if self.rect.centerx > globals.res[0] or self.rect.centerx < 0:
            self.kill()
        if self.rect.centery > globals.res[1] or self.rect.centery < 0:
            self.kill()

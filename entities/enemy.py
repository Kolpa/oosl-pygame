import pygame
import globals


class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, pos, player):
        super().__init__()

        self.color = color

        self.image = pygame.Surface([20, 20])

        self.image.fill(color)
        self.image.set_colorkey((255, 255, 255))

        self.rect = self.image.get_rect()

        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]

        self.target = pygame.math.Vector2(player.rect.centerx, player.rect.centery)

    def update(self):

        me = pygame.math.Vector2(self.rect.centerx, self.rect.centery)

        tick = self.target - me
        tick = tick.normalize()

        self.rect.centerx += tick[0] * 8
        self.rect.centery += tick[1] * 8

        if self.rect.centerx > globals.res[0] or self.rect.centerx < 0:
            self.kill()
        if self.rect.centery > globals.res[1] or self.rect.centery < 0:
            self.kill()

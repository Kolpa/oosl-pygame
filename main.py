import pygame
import globals
from entities.character import Character
from entities.enemy import Enemy
from random import randint


def display_hp(hp, max, screen):
    pygame.draw.rect(screen, (60, 179, 113), pygame.Rect(0, 20, max * 25, 25))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 20, hp * 25, 25))


def safe_spawn():
    xy = (randint(0, globals.res[0]), randint(0, globals.res[1]))

    while abs(xy[0] - player.rect.centerx) < 200 and abs(xy[1] - player.rect.centery) < 200:
        xy = (randint(0, globals.res[0]), randint(0, globals.res[1]))

    return xy

pygame.init()

screen = pygame.display.set_mode(globals.res)
clock = pygame.time.Clock()
players = pygame.sprite.Group()
points_font = pygame.font.SysFont("monospace", 20)
closed = False

while not closed:
    players.empty()
    globals.enemies.empty()
    globals.all_sprites.empty()
    globals.bullets.empty()

    done = False

    player = Character((255, 255, 0), 400, 300)
    globals.all_sprites.add(player)
    players.add(player)

    spawnct = 0

    points = 0
    hp = 5

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    player.shoot(pygame.mouse.get_pos(), globals.colors[0])

                if event.key == pygame.K_w:
                    player.shoot(pygame.mouse.get_pos(), globals.colors[1])

                if event.key == pygame.K_e:
                    player.shoot(pygame.mouse.get_pos(), globals.colors[2])

        if spawnct > 100:
            enemy = Enemy(globals.colors[randint(0, 2)], safe_spawn(), player)
            globals.all_sprites.add(enemy)
            globals.enemies.add(enemy)

            spawnct = 0

        spawnct += 1

        hits = pygame.sprite.groupcollide(globals.enemies, globals.bullets, False, True)

        for hit in hits:
            if hit.color == hits[hit][0].color:
                points += 1
                hit.kill()

        hurt = pygame.sprite.groupcollide(globals.enemies, players, True, False)

        for h in hurt:
            hp -= 1
            if hp <= 0:
                done = True

        screen.fill((255, 255, 255))

        globals.all_sprites.update()
        globals.all_sprites.draw(screen)

        points_text = points_font.render("Points: {}".format(points), 1, (0, 0, 0))
        screen.blit(points_text, (0, 0))

        display_hp(hp, 5, screen)

        clock.tick(60)

        pygame.display.flip()

    done = False

    screen.fill((255, 255, 255))

    lost_text = points_font.render("WE FUCKING LOST", 1, (0, 0, 0))
    screen.blit(lost_text, (300, 275))

    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    done = True

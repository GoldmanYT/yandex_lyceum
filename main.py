import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        for sprite in all_sprites:
            if isinstance(sprite, Player):
                all_sprites.remove(sprite)
        for player in player_group:
            player_group.remove(player)
        super().__init__(all_sprites, player_group)
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        pg.draw.rect(self.image, 'blue', (0, 0, 20, 20))
        self.rect = pg.Rect((x, y, 20, 20))

    def update(self):
        collide_with = pg.sprite.spritecollide(self, ladder_group, False)
        if not any(sprite for sprite in collide_with):
            self.rect.move_ip(0, vertical_speed)
        else:
            return
        collide_with = pg.sprite.spritecollide(self, platform_group, False)
        if collide_with:
            self.rect.move_ip(0, -self.rect.bottom + min(sprite.rect.y for sprite in collide_with))

    def move(self, dx, dy):
        collide_with = pg.sprite.spritecollide(self, ladder_group, False)
        if not any(sprite for sprite in collide_with):
            dy = 0
        self.rect.move_ip(dx, dy)


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, platform_group)
        self.image = pg.Surface((50, 10), pg.SRCALPHA)
        pg.draw.rect(self.image, 'gray', (0, 0, 50, 10))
        self.rect = pg.Rect(x, y, 50, 10)


class Ladder(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, ladder_group)
        self.image = pg.Surface((10, 50), pg.SRCALPHA)
        pg.draw.rect(self.image, 'red', (0, 0, 10, 50))
        self.rect = pg.Rect(x, y, 10, 50)


pg.init()

all_sprites = pg.sprite.Group()
player_group = pg.sprite.Group()
platform_group = pg.sprite.Group()
ladder_group = pg.sprite.Group()

pg.display.set_caption('Лесенки')
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
run = True
FPS = 50
vertical_speed = 50 / FPS
horizontal_speed = 10

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                keys = pg.key.get_pressed()
                if keys[pg.K_LCTRL]:
                    Ladder(*event.pos)
                else:
                    Platform(*event.pos)
            elif event.button == 3:
                player = Player(*event.pos)
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                for player in player_group:
                    player.move(-10, 0)
            elif event.key == pg.K_RIGHT:
                for player in player_group:
                    player.move(10, 0)
            elif event.key == pg.K_UP:
                for player in player_group:
                    player.move(0, -10)
            elif event.key == pg.K_DOWN:
                for player in player_group:
                    player.move(0, 10)

    screen.fill('black')

    all_sprites.draw(screen)
    all_sprites.update()

    pg.display.flip()
    clock.tick(FPS)

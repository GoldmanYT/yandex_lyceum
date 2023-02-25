import pygame as pg
from sys import exit
from random import randint


class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pg.image.load('data/bomb.png')
        w, h = self.image.get_size()
        while True:
            x, y = randint(0, W - w), randint(0, H - h)
            self.rect = pg.Rect(x, y, w, h)
            collide_with = pg.sprite.spritecollide(self, all_sprites, False)
            collide_with.remove(self)
            if not collide_with:
                break
        self.triggered = False

    def update(self, x, y):
        if self.rect.x <= x <= self.rect.right and self.rect.y <= y <= self.rect.bottom:
            self.triggered = True
            if self.triggered:
                w, h = self.image.get_size()
                self.image = pg.image.load('data/boom.png')
                self.image = pg.transform.smoothscale(self.image, (w, h))


W, H = 600, 600

pg.init()
screen = pg.display.set_mode((W, H))

all_sprites = pg.sprite.Group()

for i in range(10):
    Ball()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            for bomb in all_sprites:
                bomb.update(x, y)

    screen.fill('black')
    all_sprites.draw(screen)
    pg.display.flip()

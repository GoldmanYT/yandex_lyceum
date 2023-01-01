import pygame as pg
from math import sin, cos, pi, atan2
from random import random, randint


pg.init()
W, H = 800, 600
FPS = 60

all_sprites = pg.sprite.Group()


class Ball(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        r = randint(50, 100)
        self.radius = r
        self.x, self.y = x - r, y - r
        self.a = random() * 2 * pi
        self.v = randint(7, 10) / 33
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.image = pg.Surface((2 * r, 2 * r), pg.SRCALPHA, 32)
        pg.draw.circle(self.image, color, (r, r), r)
        self.rect = pg.Rect(self.x, self.y, 2 * r, 2 * r)

    def update(self):
        self.x += self.v * cos(self.a)
        self.y += self.v * sin(self.a)
        self.rect = pg.Rect(self.x, self.y, 2 * self.radius, 2 * self.radius)
        others = pg.sprite.spritecollide(self, all_sprites, False, pg.sprite.collide_circle)
        if others is not None:
            for other in others:
                if other is not self:
                    b = atan2(self.y - other.rect.y, self.x - other.rect.x)
                    a1 = self.a - b
                    a2 = other.a - b
                    self.a = atan2(sin(a1), cos(a2)) + b
                    other.a = atan2(sin(a2), cos(a1)) + b
                    self.a %= 2 * pi
                    other.a %= 2 * pi
        if self.x + self.radius * 2 >= W and (self.a < pi / 2 or self.a > 3 * pi / 2) or \
                self.x <= 0 and pi / 2 < self.a < 3 * pi / 2:
            self.a = pi - self.a
        if self.y + self.radius * 2 >= H and 0 < self.a < pi or \
                self.y <= 0 and pi < self.a < 2 * pi:
            self.a = -self.a
        self.a %= 2 * pi

    # def collide(self, other):
    #     if (self.x - other.x) ** 2 + (self.y - other.y) ** 2 > (self.r + other.r) ** 2:
    #         return



screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            Ball(mouse_x, mouse_y)

    screen.fill('black')
    all_sprites.draw(screen)
    all_sprites.update()
    pg.display.flip()

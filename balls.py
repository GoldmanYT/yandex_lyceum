import pygame as pg
from math import sin, cos, pi, atan2
from random import random, randint


pg.init()
W, H = 800, 600
FPS = 60


class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.a = random() * 2 * pi
        self.v = randint(7, 20) / 33
        self.r = randint(50, 100)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def update(self):
        self.x += self.v * cos(self.a)
        self.y += self.v * sin(self.a)
        if self.x + self.r >= W and (self.a < pi / 2 or self.a > 3 * pi / 2) or \
                self.x - self.r <= 0 and pi / 2 < self.a < 3 * pi / 2:
            self.a = pi - self.a
        if self.y + self.r >= H and 0 < self.a < pi or \
                self.y - self.r <= 0 and pi < self.a < 2 * pi:
            self.a = -self.a
        self.a %= 2 * pi

    def collide(self, other):
        if (self.x - other.x) ** 2 + (self.y - other.y) ** 2 > (self.r + other.r) ** 2:
            return
        b = atan2(self.y - other.y, self.x - other.x)
        a1 = self.a - b
        a2 = other.a - b
        self.a = atan2(sin(a1), cos(a2)) + b
        other.a = atan2(sin(a2), cos(a1)) + b
        self.a %= 2 * pi
        other.a %= 2 * pi
        self.v, other.v = other.v, self.v

    def draw(self):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.r)


balls = []

screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            balls.append(Ball(mouse_x, mouse_y))

    for ball in balls:
        ball.update()
    for i, ball1 in enumerate(balls[:-1]):
        for ball2 in balls[i + 1:]:
            ball1.collide(ball2)

    screen.fill('black')
    for ball in balls:
        ball.draw()
    pg.display.flip()

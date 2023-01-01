import pygame as pg
from math import pi, sin, cos, atan2

pg.init()
W, H = 800, 600
FPS = 60
balls = []
rects = []


class Ball:
    def __init__(self, x, y, r):
        self.x, self.y, self.r = x, y, r
        self.a = pi / 6
        self.v = 10

    def update(self):
        self.x += self.v * cos(self.a)
        self.y += self.v * sin(self.a)
        for rect in rects:
            hor = []
            if self.r ** 2 - (self.y - rect.top) ** 2 > 0:
                hor += [(self.x - (self.r ** 2 - (self.y - rect.top) ** 2) ** 0.5, rect.top),
                        (self.x + (self.r ** 2 - (self.y - rect.top) ** 2) ** 0.5, rect.top)]
            if self.r ** 2 - (self.y - rect.bottom) ** 2 > 0:
                hor += [(self.x - (self.r ** 2 - (self.y - rect.bottom) ** 2) ** 0.5, rect.bottom),
                        (self.x + (self.r ** 2 - (self.y - rect.bottom) ** 2) ** 0.5, rect.bottom)]
            hor = [(x, y) for x, y in hor if rect.left <= x <= rect.right]
            ver = []
            if self.r ** 2 - (self.x - rect.left) ** 2 > 0:
                ver += [(rect.left, self.y - (self.r ** 2 - (self.x - rect.left) ** 2) ** 0.5),
                        (rect.left, self.y + (self.r ** 2 + (self.x - rect.left) ** 2) ** 0.5)]
            if self.r ** 2 - (self.x - rect.right) ** 2 > 0:
                ver += [(rect.right, self.y - (self.r ** 2 - (self.x - rect.right) ** 2) ** 0.5),
                        (rect.right, self.y + (self.r ** 2 - (self.x - rect.right) ** 2) ** 0.5)]
            ver = [(x, y) for x, y in ver if rect.top <= y <= rect.bottom]
            points = hor + ver
            if points:
                if len(points) == 1:
                    phi = 2 * pi
                else:
                    (x1, y1), (x2, y2) = points[:2]
                    phi = atan2(y2 - y1, x2 - x1)
                self.a = 2 * phi - self.a
        self.a %= 2 * pi

    def draw(self):
        pg.draw.circle(screen, 'white', (self.x, self.y), self.r)


def update():
    for ball in balls:
        ball.update()


def draw():
    screen.fill('black')
    for rect in rects:
        pg.draw.rect(screen, 'white', rect)
    for ball in balls:
        ball.draw()


rects.append(pg.Rect(0, 0, W, 0))
rects.append(pg.Rect(0, H, W, 0))
rects.append(pg.Rect(0, 0, 0, H))
rects.append(pg.Rect(W, 0, 0, H))
rects.append(pg.Rect(100, 100, 300, 100))
run = True
screen = pg.display.set_mode((W, H))
clock = pg.time.Clock()

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            balls.append(Ball(mouse_x, mouse_y, 10))
    update()
    draw()
    pg.display.flip()
    clock.tick(FPS)
pg.quit()

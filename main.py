import pygame as pg


class Player(pg.Rect):
    def __init__(self, x, y):
        super().__init__(self.x, self.y, 20, 20)
        self.x, self.y = x, y
        self.rect = pg.Rect((self.x, self.y, 20, 20))

    def move_to(self, x, y):
        self.x, self.y = x, y

    def move(self, dx, dy):
        self.x += dx * 10
        self.y += dy * 50

    def draw(self):
        pg.draw.rect(screen, 'blue', (self.x, self.y, 20, 20))


class Platform(pg.Rect):
    def __init__(self, x, y):
        super().__init__(self.x, self.y, 50, 10)
        self.x, self.y = x, y

    def draw(self):
        pg.draw.rect(screen, 'gray', (self.x, self.y, 50, 10))


pg.init()

player = None
platforms = []

pg.display.set_caption('Платформы')
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                platforms.append(Platform(*event.pos))
            elif event.button == 3:
                player = Player(*event.pos)

    screen.fill('black')

    if player is not None:
        player.draw()
    for platform in platforms:
        platform.draw()

    pg.display.flip()
    clock.tick(60)

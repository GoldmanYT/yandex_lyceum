import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.x, self.y = x, y
        self.image = pg.Surface((20, 20), pg.SRCALPHA)
        pg.draw.rect(self.image, 'blue', (0, 0, 20, 20))
        self.rect = pg.Rect((self.x, self.y, 20, 20))

    def update(self):
        self.rect = pg.Rect((self.x, self.y, 20, 20))

    def move_to(self, x, y):
        self.x, self.y = x, y

    def move(self, dx, dy):
        self.x += dx * 10
        self.y += dy * 10


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.x, self.y = x, y
        self.image = pg.Surface((50, 10), pg.SRCALPHA)
        pg.draw.rect(self.image, 'gray', (0, 0, 50, 10))
        self.rect = pg.Rect(self.x, self.y, 50, 10)


pg.init()

all_sprites = pg.sprite.Group()

pg.display.set_caption('Платформы')
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
run = True
FPS = 50
v = 1 * FPS / 1000

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                Platform(*event.pos, all_sprites)
            elif event.button == 3:
                Player(*event.pos, all_sprites)

    screen.fill('black')

    all_sprites.draw(screen)
    all_sprites.update()

    pg.display.flip()
    clock.tick(FPS)

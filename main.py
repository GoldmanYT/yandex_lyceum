import pygame as pg
from random import randint


class Board:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.board = [[-1] * w for _ in range(h)]

    def on_board(self, x, y):
        return self.w - 1 >= x >= 0 <= y <= self.h - 1

    def draw(self):
        screen.fill('black')
        font = pg.font.Font(None, 20)
        for y in range(self.h):
            for x in range(self.w):
                pos = self.board[y][x]
                if pos == 10:
                    pg.draw.rect(screen, 'red',
                                 (self.left + x * self.cell_size, self.top + y * self.cell_size,
                                  self.cell_size, self.cell_size))
                elif pos > -1:
                    text = font.render(f'{pos}', True, (0, 255, 0))
                    screen.blit(text, (self.left + 2 + x * self.cell_size, self.top + 2 + y * self.cell_size))
                pg.draw.rect(screen, 'white',
                             (self.left + x * self.cell_size, self.top + y * self.cell_size,
                              self.cell_size, self.cell_size), 1)


class Minesweeper(Board):
    def __init__(self, w, h):
        super().__init__(w, h)
        for _ in range(10):
            x, y = randint(0, self.w - 1), randint(0, self.h - 1)
            self.board[y][x] = 10

    def place(self, x, y):
        if not self.on_board(x, y) or self.board[y][x] == 10:
            return
        self.board[y][x] = self.mines_count(x, y)

    def mines_count(self, x, y):
        directions = (-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)
        return len([(x + dx, y + dy) for dx, dy in directions
                    if self.on_board(x + dx, y + dy) and self.board[y + dy][x + dx] == 10])


pg.init()

pg.display.set_caption('Дедушка сапёра')
screen = pg.display.set_mode((320, 470))
clock = pg.time.Clock()
run = True
FPS = 60

minesweeper = Minesweeper(10, 15)

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                x, y = ((mouse_x - minesweeper.left) // minesweeper.cell_size,
                        (mouse_y - minesweeper.top) // minesweeper.cell_size)
                minesweeper.place(x, y)

    minesweeper.draw()
    pg.display.flip()
    clock.tick(FPS)

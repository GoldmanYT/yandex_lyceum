import requests
import pygame as pg
from sys import exit

coords = [
    '64.796296,54.468172',
    '-0.554497,51.848595',
    '-63.984938,-33.867512'
]
d = {
    0: 16,
    1: 17,
    2: 16,
}

for i, coord in enumerate(coords):
    url = f'https://static-maps.yandex.ru/1.x/?l=sat&z={d[i]}&ll={coord}'
    response = requests.get(url)
    if response:
        with open(f'res{i}.png', 'wb') as f:
            f.write(response.content)
    else:
        print(response)

pg.init()
screen = pg.display.set_mode((600, 450))
pg.display.flip()
run = True
i = 0

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            pg.quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                i = (i - 1) % len(coords)
            elif event.key == pg.K_RIGHT:
                i = (i + 1) % len(coords)
            else:
                i = (i + 1) % len(coords)

    screen.blit(pg.image.load(f'res{i}.png'), (0, 0))
    pg.display.flip()

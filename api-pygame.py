import requests
import pygame as pg
from sys import exit
import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    distance = math.sqrt(dx * dx + dy * dy)

    return distance


coords = [
    (29.913396, 59.891665), (30.221951, 59.918606), (30.259094, 59.917800), (30.282579, 59.933602),
    (30.314566, 59.939864)
]
ans = sum(lonlat_distance(x, y) for x, y in zip(coords, coords[1:]))
print(ans)

s = []
for x, y in coords:
    s.append(f'{x},{y}')
s = ','.join(s)
x, y = coords[len(coords) // 2]
mark = f'{x},{y}'
url = f'https://static-maps.yandex.ru/1.x/?l=map&pl={s}&pt={mark}'
response = requests.get(url)
if response:
    with open(f'res.png', 'wb') as f:
        f.write(response.content)
else:
    print(response)

pg.init()
screen = pg.display.set_mode((600, 450))
pg.display.flip()
run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
            pg.quit()

    screen.blit(pg.image.load(f'res.png'), (0, 0))
    pg.display.flip()

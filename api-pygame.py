import requests
import pygame

url = 'https://static-maps.yandex.ru/1.x/?l=map&z=10&pl=29.913396,59.891665,30.221951,59.918606,30.259094,59.917800,30.282579,59.933602,30.314566,59.939864'

response = requests.get(url)
if response:
    with open('res.png', 'wb') as f:
        f.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load('res.png'), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

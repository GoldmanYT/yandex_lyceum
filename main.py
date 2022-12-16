import pygame


pygame.init()
width, height = 729, 300


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load('mountains.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


class Landing(pygame.sprite.Sprite):
    image = pygame.image.load("pt.png")

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


all_sprites = pygame.sprite.Group()
mountain = Mountain()

pygame.display.set_caption('Высадка десанта')
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
run = True
FPS = 60

while run:
    screen.fill('black')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)

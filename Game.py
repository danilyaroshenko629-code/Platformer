
import pygame as pg
import settings
import asset_manager
import platform

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((settings.WINDOW_SIZE))
clock = pg.time.Clock()




run = True
while run:

    dt = clock.tick(settings.FPS) / 1000.0
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False







    pg.display.update()



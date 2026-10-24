
import pygame as pg
import settings
from asset_manager import AssetManager
from game_plattform import GamePlatform
from player import Player

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((settings.WINDOW_SIZE))
clock = pg.time.Clock()
platform = GamePlatform((200,50),"Platform.png",(250 ,0),AssetManager())
player = Player(pg.Vector2(500,0),"img.png",(125,125),AssetManager())
platforms = pg.sprite.Group()
platforms.add(platform)


run = True
while run:

    dt = clock.tick(settings.FPS) / 1000.0
    screen.fill((0, 0, 0))
    player.draw(screen)
    player.update(dt,platforms)
    platform.draw(screen)




    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False







    pg.display.update()



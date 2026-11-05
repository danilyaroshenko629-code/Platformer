import pygame as pg
import Asset
import settings
from asset_manager import AssetManager
from game_plattform import GamePlatform
from player import Player
from game_ground import GameGround
from level_loader import load_level

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((settings.WINDOW_SIZE))
clock = pg.time.Clock()

asset_manager_bg = AssetManager()
bg_image = asset_manager_bg.get_image(settings.BACKGROUND , settings.WINDOW_SIZE)

platforms, walls, ground,player = load_level("level_1.txt", AssetManager())

run = True
while run:

    dt = clock.tick(settings.FPS) / 1000.0
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, 0))

    player.update(dt,platforms,walls,ground)

    player.draw(screen)
    platforms.draw(screen)
    walls.draw(screen)
    ground.draw(screen)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False

    pg.display.update()




import pygame as pg
import settings
from asset_manager import AssetManager
from game_plattform import GamePlatform
from player import Player

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((settings.WINDOW_SIZE))
clock = pg.time.Clock()
platform = GamePlatform((700,50),"Platform.png",(250 ,620),AssetManager())
platform_2 = GamePlatform((700,50),"Platform.png",(250 ,440),AssetManager())
platform_3 = GamePlatform((50,700),"Platform.png",(250 ,440),AssetManager())
player = Player(pg.Vector2(500,0),"img.png",(50,90),AssetManager())
platforms = pg.sprite.Group()
platforms.add(platform)
platforms.add(platform_2)
walls = pg.sprite.Group()
walls.add(platform_3)



asset_manager_bg = AssetManager()
bg_image = asset_manager_bg.get_image("Background_1.png",settings.WINDOW_SIZE)

run = True
while run:

    dt = clock.tick(settings.FPS) / 1000.0
    screen.fill((0,0,0))
    screen.blit(bg_image,(0,0))
    player.draw(screen)
    player.update(dt,platforms,walls)
    platforms.draw(screen)
    walls.draw(screen)




    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False



    pg.display.update()



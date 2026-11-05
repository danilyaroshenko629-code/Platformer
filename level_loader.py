import pygame as pg

from game_ground import GameGround
from game_plattform import GamePlatform
from player import Player
from settings import *

file_path = "level_1.txt"


def load_level(file_path, asset_manager):
    platforms = pg.sprite.Group()
    walls = pg.sprite.Group()
    ground = pg.sprite.Group()

    with open(file_path, "r", encoding="utf-8") as file:
        level_data = file.readlines()
    y = 0
    for line in level_data:
        x = 0

        for symbol in line.strip():

            if symbol == MAP_SYMBOLS["platform"]:
                platform = GamePlatform(
                    (TILE_SIZE, TILE_SIZE // 2), "Asset/Platform.png", pg.Vector2(x, y), asset_manager
                )
                platforms.add(platform)
            elif symbol == MAP_SYMBOLS["wall"]:
                wall = GamePlatform(
                    (TILE_SIZE, TILE_SIZE), "Asset/wall.top.png", pg.Vector2(x, y), asset_manager
                )
                walls.add(wall)

            elif symbol == MAP_SYMBOLS["ground"]:
                gr = GameGround(
                    (TILE_SIZE, TILE_SIZE // 2), "Asset/ground.png", pg.Vector2(x, y), asset_manager
                )
                ground.add(gr)

            elif symbol == MAP_SYMBOLS["player"]:
                player = Player(
                    pg.Vector2(x, y), "Asset/img.png", (TILE_SIZE, TILE_SIZE), asset_manager
                )


            x += TILE_SIZE
        y += TILE_SIZE



    return platforms, walls, ground, player
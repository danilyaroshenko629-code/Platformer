import pygame as pg
from game_plattform import GamePlatform
from settings import *

file_path = "level_1.txt"

def load_level(file_path, asset_manager):
    platforms = pg.sprite.Group()
    with open (file_path, "r", encoding="utf-8") as file:
        level_data = file.readlines()


    return platforms
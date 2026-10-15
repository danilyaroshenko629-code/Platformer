import pygame as pg
import game_object
import settings
import asset_manager

class Player(game_object):
    def  __init__(self,position: pg.Vector2, image_path : str,size: tuple[int,int],asset_manager):
        super().__init__()
        self.move_direction
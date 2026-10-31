import  pygame as pg
import game_object
from settings import *
from asset_manager import AssetManager

class GameGround(game_object.GameObject):
    def __init__(self,size: tuple[int,int],image_path: str, position: pg.Vector2,asset_manager: AssetManager):
        super().__init__( position , image_path ,size , asset_manager)

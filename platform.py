import  pygame as pg
import game_object
from settings import *
from asset_manager import AssetManager

class Platform(game_object.GameObject):
    def __init__(self,size: tuple[int,int],texture: str, position: pg.Vector2, image_path : str,asset_manager: AssetManager):
        super().__init__( position , image_path ,size , asset_manager )
        self.texture = pg.transform.scale(pg.image.load(texture), size)


    def update(self):
        pass



    def draw(self, screen : pg.Surface):
        screen.blit(self.texture, self.rect )
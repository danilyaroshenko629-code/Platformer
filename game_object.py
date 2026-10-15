import pygame as pg
from Platformer.asset_manager import AssetManager


class GameObject(pg.sprite.Sprite):
    def __init__(self, position: pg.Vector2, image_path : str,size: tuple[int,int],asset_manager: AssetManager):
        super().__init__()
        self.rect = pg.Rect(size)
        self.position = pg.Vector2(position)
        self.asset_manager = asset_manager
        self.image = self.asset_manager.get_image(image_path,size)




    def update(self):
        pg.display.update()

    def draw(self, screen : pg.Surface):
        screen.blit(self.image,self.rect)



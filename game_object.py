from  pygame import  Rect,Surface
from pygame.math import Vector2
from pygame import sprite
from asset_manager import AssetManager

class GameObject(sprite.Sprite):
    def __init__(self, position: Vector2, image_path : str,size: tuple[int,int],asset_manager: AssetManager):
        super().__init__()
        self.rect = Rect(size, position)
        self.position = Vector2(position)
        self.asset_manager = asset_manager
        self.image = self.asset_manager.get_image(image_path,size)



    def draw(self, screen : Surface):
        screen.blit(self.image,self.rect)
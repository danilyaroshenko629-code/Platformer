import pygame as pg
from game_object import GameObject
import settings
from asset_manager import AssetManager
import math


class Player(GameObject):
    def __init__(self, position: pg.Vector2, image_path: str, size: tuple[int, int], asset_manager: AssetManager):
        super().__init__(position, image_path, size, asset_manager)
        #
        self.move_direction = 0.0
        #
        self.velocity = pg.Vector2(0, 0)
        #
        self.is_grounded = True

    def handle_input(self):
        keys = pg.key.get_pressed()
        self.move_direction = 0.0

        if keys[pg.K_d]:
            self.move_direction += 1.0

        if keys[pg.K_a]:
            self.move_direction -= 1.0

    def jump(self):
        pass

    def apply_horizontal_movement(self,dt):
        if self.move_direction != 0:
            self.velocity.x += self.move_direction * settings.ACCELERATION * dt
            self.velocity.x =     pg.math.clamp(self.velocity.x,-settings.MAX_SPEED,settings.MAX_SPEED)


        else:
            if self.velocity.x > 0:
                self.velocity.x = max(0.0, self.velocity.x - settings.FRICTION * dt)
            elif self.velocity.x < 0:
                self.velocity.x = min(0, self.velocity.x + settings.FRICTION * dt)

        # перевіряємо чи є направлення

        # якщо направлення != 0, то ми розганяємо гравця в обраному напрямку

        # обмежуємо швидкість гравця
        # pg.math.clamp(ШВИДКІСТЬ ГРАВЦЯ, -МАКСИМАЛЬНА ШВИДКІСТЬ, МАКСИМАЛЬНА ШВИДКІСТЬ)



    def update(self, dt : float,platforms):
        self.handle_input()
        self.position += self.velocity * dt

        self.apply_horizontal_movement(dt)
        for pl in platforms:
            if self.rect.colliderect(pl.rect):
                print("collide")

                if self.velocity.x > 0:
                    self.rect.right = pl.rect.left
                    self.position.x = self.rect.x
                    self.velocity.x = 0

                elif self.velocity.x <0 :
                    self.rect.left = pl.rect.right
                    self.position.x = self.rect.x
                    self.velocity.x = 0

        self.rect.topleft = (self.position.x, self.position.y)
        return super().update()


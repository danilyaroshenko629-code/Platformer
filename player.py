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

        if keys[pg.K_SPACE]:
            self.jump()

        # якщо гравець натиснув пробіл то JUMP

    def jump(self):

        if self.is_grounded:
            self.velocity.y = -settings.JUMP_FORCE
            self.is_grounded = False


        # якщо гравець він не на землі
        # змінуюємо швидкість гравця velocity.y на JUMP_FORCE
        # кажемо що гравець тепер не на землі

        # def apply_vertical_movement(self, dt):
        """ГРАВІТАЦІЯ ЩО ДІЄ ПОСТІЙНО НА ГРАВЦЯ"""
        #  self.velocity.y += ГРАВІТАЦІЯ * dt

    def apply_vertical_movement(self, dt):
        self.velocity.y += settings.GRAVITY * dt

    def apply_horizontal_movement(self, dt):
        if self.move_direction != 0:
            self.velocity.x += self.move_direction * settings.ACCELERATION * dt
            self.velocity.x = pg.math.clamp(self.velocity.x, -settings.MAX_SPEED, settings.MAX_SPEED)


        else:
            if self.velocity.x > 0:
                self.velocity.x = max(0.0, self.velocity.x - settings.FRICTION * dt)
            elif self.velocity.x < 0:
                self.velocity.x = min(0, self.velocity.x + settings.FRICTION * dt)

    def check_window(self):
        if self.rect.left < 0:
            self.rect.left = 0
            self.position.x = float(self.rect.x)
            self.velocity.x = 0

        if self.rect.right > settings.WINDOW_SIZE[0]:
            self.rect.right = settings.WINDOW_SIZE[0]
            self.position.x = float(self.rect.x)
            self.velocity.x = 0

    def update(self, dt: float, platforms,walls,ground):
        self.handle_input()

        self.apply_horizontal_movement(dt)
        self.position.x += self.velocity.x * dt  # перероблюємо на ГОРИЗОНТАЛЬНИЙ рух
        for w in walls:
            if self.rect.colliderect(w.rect):

                if self.velocity.x > 0:
                    self.rect.right = w.rect.left
                    self.position.x = float(self.rect.x)
                    self.velocity.x = 0
        for w in walls:
            if self.rect.colliderect(w.rect):
                if self.velocity.x < 0:
                    self.rect.left = w.rect.right
                    self.position.x = float(self.rect.x)
                    self.velocity.x = 0

        self.apply_vertical_movement(dt)

        self.position.y += self.velocity.y * dt


        # ПЕРЕВІРЯЄМО чи гравець стоїть ЗВЕРХУ платформи та ЗНИЗУ

        self.rect.y = int(self.position.y)
        self.is_grounded = False
        for pl in platforms:
            if self.rect.colliderect(pl.rect) and (self.rect.bottom - pl.rect.top) <= (self.velocity.y * dt + 15):

                if self.velocity.y > 0:
                    self.rect.bottom = pl.rect.top
                    self.position.y = float(self.rect.y)
                    self.velocity.y = 0
                    self.is_grounded = True


        self.check_window()
        self.rect.topleft = (self.position.x, self.position.y)

        return super().update()


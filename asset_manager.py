import pygame as pg


class AssetManager:
    def __init__(self):
        self._images: dict[str: pg.Surface] = {}
        # self._sound =

    # ЗАВАНТАЖИТИ ФОТО та ПОВЕРНУТИ ЦЕ ФОТО
    def get_image(self, path: str, scale: tuple[int, int]):
        key = f"{path}_{scale}"

        if not key in self._images:
            try:
                loaded_image = pg.image.load(path).convert_alpha()  # ЗАВАНТАЖЕННЯ ЗОБРАЖЕННЯ В ГРУ та ОПТИМІЗАЦІЯ
                if scale:
                    loaded_image = pg.transform.scale(loaded_image, scale)
                self._images[key] = loaded_image
            except (pg.error, FileNotFoundError):
                size = (32, 32)
                if scale:
                    size = scale

                surface = pg.Surface(size)
                surface.fill((255, 0, 0))

                self._images[key] = surface

        return self._images[key]

# do not touch
# hello hello
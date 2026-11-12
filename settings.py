import Asset
from pathlib import Path
MAX_SPEED = 500
ACCELERATION = 2500
FRICTION = 4500
FPS = 144
WINDOW_SIZE = (1280,780)
JUMP_FORCE = 800
GRAVITY =  1600

TILE_SIZE = 75

MAP_SYMBOLS = {
    "platform" :  "-",
    "player" : "p",
    "wall"  : "w",
    "ground" : "g"

}

BACKGROUND = "Asset/picture/Background_1.png"
GROUND = "Asset/picture/ground.png"
PLAYER = "Asset/img.png"
PLATTFORM ="Asset/Platform.png"
WALL_RIGHT = "Asset/wall.right.png"
WALL_LEFT = "Asset/wall.top.png"
WALL_TOP = "Asset/wall_left.png"


JUMP_SFX = r"Asset/sounds/jumpsoundeffect.mp3"
LEVEL_1_MUSIC = "Asset/sounds/bit-shift-kevin-macleod-main-version-24901-03-12.mp3"
DEATH_SOUND =  "Asset/sounds/chisper-8-bit-game-over-634762.mp3"
# клас HUD -- клас для відображеня інформації гравця
from symtable import Class
import pygame as pg
import  settings

class HUD:
    def __init__(self,size ,font_name,color):
        self.size = size
        self.font_name = font_name
        self.color = color
        self.font = pg.font.Font(self.font_name,self.size)

    def draw_text(self,screen: pg.window,text,position):
        self.text = self.font.render(text, True, self.color)
        screen.blit(self.text, position)



    def draw(self,screen,player,level_info):
        player_hp = f"HP:{player.hp}"
        HP_text_pos = self.font.size(player_hp)
        self.draw_text(screen,player_hp,(settings.WINDOW_SIZE[0]-HP_text_pos[0],0))
        self.draw_text(screen, f"Time:", (0, 0))



"""
клас нічого не РАХУЄ він лише показує інформацію

худ малюєтсья поверх всього

налаштування (розмір шрифта, назва шрифта, колір)  знаходиться в settings

він має:
    шрифт

вміє:
    __init__(font_name):
        створює шрифт

    draw_text(screen,text, position):
        намалювати конкретний текст на екрані

    draw(screen, player, level_info)
        малює всі тексти на екрані

        draws(screen, f"HP: {player.hp}", 0,0)
"""


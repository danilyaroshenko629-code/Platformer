# клас HUD -- клас для відображеня інформації гравця
from symtable import Class
import pygame as pg

class HUD:
    def __init__(self,size ,font_name,color):
        self.size = size
        self.font_name = font_name
        self.color = color
        self.font = pg.font.Font(self.font_name,self.size)

    def draw_text(self,screen: pg.window,text,position):
        self.text =  self.font.render(text,True,self.color)
        screen.blit(self.text,position)


    def draw(self,screen,player,level_info):
        self.hp = self.font.render(f"HP:",True,self.color)
        screen.blit(self.hp)


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


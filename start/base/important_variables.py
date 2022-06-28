import pygame

from base.keyboard import Keyboard
from gui_components.window import Window

pygame.init()

screen_length = 1100
screen_height = 550
background_color = (200, 200, 200)

keyboard = Keyboard()
game_window = Window(screen_length, screen_height, background_color, "Game Basics")
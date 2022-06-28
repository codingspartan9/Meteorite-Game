import pygame

from base.dimensions import Dimensions
from base.important_variables import game_window
from gui_components.component import Component


class TextBox(Component):
    text = ""
    font = None
    font_size = 0
    background_color = None
    text_color = None
    is_centered = False

    def __init__(self, text, font_size, background_color, text_color, is_centered):
        self.text, self.font_size = text, font_size
        self.text_color, self.is_centered = text_color, is_centered
        self.background_color, self.color = background_color, background_color
        self.font = pygame.font.Font("freesansbold.ttf", font_size)
        super().__init__("")
        Dimensions.__init__(self, 0, 0, 0, 0)

    def render(self):
        super().render()

        text = self.font.render(self.text, True, self.text_color, self.background_color)
        text_rectangle = text.get_rect()

        if self.is_centered:
            text_rectangle.center = (self.horizontal_midpoint, self.vertical_midpoint)

        else:
            text_rectangle.top = self.top_edge
            text_rectangle.left = self.left_edge

        game_window.get_window().blit(text, text_rectangle)
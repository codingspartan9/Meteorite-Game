import pygame

from base.dimensions import Dimensions
from base.important_variables import game_window
from base.utility_functions import render_image, mouse_is_clicked


class Component(Dimensions):
    color = None
    path_to_image = None

    def __init__(self, path_to_image=""):
        self.path_to_image = path_to_image

    def run(self):
        pass

    def render(self):
        if self.path_to_image != "":
            render_image(self.path_to_image, self.left_edge, self.top_edge, self.length, self.height)

        else:
            pygame.draw.rect(game_window.get_window(), self.color, (self.left_edge, self.top_edge, self.length, self.height))

    def got_clicked(self):
        area = pygame.Rect(self.left_edge, self.top_edge, self.length, self.height)
        mouse_left_edge, mouse_top_edge = pygame.mouse.get_pos()

        return mouse_is_clicked() and area.collidepoint(mouse_left_edge, mouse_top_edge)
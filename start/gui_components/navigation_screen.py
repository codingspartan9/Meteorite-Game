from math import sqrt

from base.colors import pleasing_green, white
from base.dimensions import Dimensions
from base.utility_functions import key_is_hit
from gui_components.grid import Grid
from gui_components.screen import Screen
from gui_components.text_box import TextBox
from base.important_variables import *


class NavigationScreen(Screen):
    buttons = []
    screens = []
    selected_screen = None

    def __init__(self, screen_names, screens):
        self.screens = screens

        for screen_name in screen_names:
            self.buttons.append(TextBox(screen_name, 18, pleasing_green, white, True))

        columns = int(sqrt(len(screen_names)))
        button_grid = Grid(Dimensions(0, 0, screen_length, screen_height), columns, None)
        button_grid.turn_into_grid(self.buttons, None, None)

        self.components = self.buttons
        self.selected_screen = self

    def run(self):
        for x in range(len(self.buttons)):
            if self.buttons[x].got_clicked() and self.selected_screen == self:
                self.selected_screen = self.screens[x]

        if key_is_hit(pygame.K_ESCAPE):
            self.selected_screen = self

        if self.selected_screen != self:
            self.selected_screen.run()

    def render_background(self):
        if self.selected_screen != self:
            self.selected_screen.render_background()

    def get_components(self):
        return self.components if self.selected_screen == self else self.selected_screen.get_components()

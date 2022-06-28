import random

import pygame

from base.colors import black, blue, red, white, pleasing_green
from base.engines import CollisionsEngine
from base.lines import Path, Point, LineSegment
from base.utility_functions import key_is_hit
from base.velocity_calculator import VelocityCalculator
from gui_components.grid import Grid
from gui_components.intermediate_screen import IntermediateScreen
from gui_components.screen import Screen
from base.dimensions import Dimensions
from base.important_variables import *
from gui_components.text_box import TextBox
from meteorite import Meteorite
from player import Player


class MeteoriteGameScreen(Screen):
    players = []
    is_versus = False
    time_between_meteorites = Path(Point(0, 4),[Point(1000, 3.5), Point(1500, 3.2), Point(2000, 3), Point(2500, 2.5), Point(3500, 1.6), Point(float("inf"), 1.6)])
    time_for_meteorites_to_fall = Path(Point(0, 5),[Point(1000, 5), Point(1500, 4.5), Point(2000, 3), Point(2500, 2.5), Point(3500, 2), Point(float("inf"), 2)])
    points_per_meteorite_destroyed = 200
    meteorites = []
    time_since_last_meteorite = 0
    number_of_players = 0
    player_total_score = 0
    player_scores = []
    player_score_fields = []
    high_score = 0
    high_score_field = None
    hud = []
    game_is_reset = False

    intermediate_screen = None
    is_high_score = False

    def __init__(self, number_of_players, is_versus):
        self.basic_variable_setup(number_of_players, is_versus)
        self.setup_players()
        self.set_up_hud()

        self.create_meteorites(self.time_for_meteorites_to_fall.get_y_coordinate(0))

    def basic_variable_setup(self, number_of_players, is_versus):
        self.number_of_players, self.is_versus = number_of_players, is_versus
        Dimensions.__init__(self, 0, 0, screen_length, screen_height)
        super().__init__("images/galaxy.png")
        self.players, self.meteorites, self.player_score_fields, self.player_scores = [], [], [], []

    def setup_players(self):
        players_keys = [[pygame.K_a, pygame.K_d, pygame.K_f], [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SLASH]]
        self.players = []

        for x in range(self.number_of_players):
            player_keys = players_keys[x]
            self.players.append(Player(player_keys[0], player_keys[1], player_keys[2], f"images/player{x + 1}.png", f"images/laser{x + 1}.png"))

        self.set_players_left_edge()

    def set_up_hud(self):
        colors = [blue, red]

        for x in range(self.number_of_players):
            if (x == 0 or (x >= 1 and self.is_versus)):
                self.player_score_fields.append(TextBox("", 18, white, colors[x], True))
                self.player_scores.append(0)

        self.high_score_field = TextBox("", 18, pleasing_green, white, True)
        self.hud = [self.high_score_field] + self.player_score_fields
        grid = Grid(Dimensions(0, 0, screen_length, screen_height * .1), 1, None)
        grid.turn_into_grid(self.hud, None, None)

    def run(self):
        self.run_meteorite_creation()
        self.update_high_score()
        self.update_hud()

    def update_hud(self):
        for x in range(len(self.player_scores)):
            self.player_score_fields[x].text = f"Player #{x + 1} Score: {self.player_scores[x]}"

        self.high_score_field.text = f"High Score {self.high_score}"

    def update_high_score(self):
        for player_score in self.player_scores:
            if player_score >= self.high_score:
                self.high_score = player_score
                self.is_high_score = True

    def run_meteorite_creation(self):
        self.time_since_last_meteorite += VelocityCalculator.time

        player_create_meteorite = key_is_hit(pygame.K_s) or key_is_hit(pygame.K_PERIOD)

        if player_create_meteorite or self.time_since_last_meteorite >= self.time_between_meteorites.get_y_coordinate(self.player_total_score):
            self.create_meteorites(self.time_for_meteorites_to_fall.get_y_coordinate(self.player_total_score))
            self.time_since_last_meteorite = 0

    def create_meteorites(self, time_for_meteorite_to_fall):
        for x in range(self.number_of_players):
            self.create_meteorite(time_for_meteorite_to_fall)

    def create_meteorite(self, time_for_meteorite_to_fall):
        min_left_edge = 0
        max_left_edge = screen_length - Meteorite.length
        start_left_edge = random.randint(min_left_edge, max_left_edge)

        max_change = screen_length / 2

        min_end_left_edge = min_left_edge if start_left_edge - max_change < min_left_edge else start_left_edge - max_change
        max_end_left_edge = max_left_edge if start_left_edge + max_change > max_left_edge else start_left_edge + max_change

        end_left_edge = random.randint(min_end_left_edge, max_end_left_edge)
        meteorite_path = LineSegment(Point(start_left_edge, -Meteorite.height), Point(end_left_edge, screen_height - Meteorite.height))
        meteorite = Meteorite(meteorite_path, time_for_meteorite_to_fall)
        self.meteorites.append(meteorite)

    def set_players_left_edge(self):
        previous_player_left_edge = (screen_length / 2) + Player.length

        for player in self.players:
            player.left_edge = previous_player_left_edge - player.length
            previous_player_left_edge = player.left_edge

    def get_components(self):
        player_components = []

        for player in self.players:
            player_components += player.get_components()

        return self.hud + player_components + self.meteorites
import random

import pygame

from base.lines import Path, Point, LineSegment
from base.utility_functions import key_is_hit
from gui_components.screen import Screen
from player import Player
from meteorite import Meteorite
from base.velocity_calculator import VelocityCalculator
from base.engines import CollisionsEngine
from base.important_variables import *


class MeteoriteGameScreen(Screen):
    players = []
    is_versus = False
    meteorites = []
    time_since_last_meteorite = 0
    time_between_meteorites = Path(Point(0, 4),[Point(1000, 3.5), Point(1500, 3.2), Point(2000, 3), Point(2500, 2.5), Point(3500, 1.6), Point(float("inf"), 1.6)])
    time_for_meteorites_to_fall = Path(Point(0, 5),[Point(1000, 5), Point(1500, 4.5), Point(2000, 3), Point(2500, 2.5), Point(3500, 2), Point(float("inf"), 2)])
    number_of_players = 0
    player_points = []
    total_score = 0
    player_points_field = []
    high_score_field = None
    high_score = 0

    def __init__(self, number_of_players, is_versus):
        super().__init__("images/galaxy.png")
        self.is_versus = is_versus

        self.players, self.meteorites, self.player_points_field = [], [], []
        self.player_points = [0] * number_of_players
        self.number_of_players = number_of_players
        players_keys = [[pygame.K_a, pygame.K_d, pygame.K_f], [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SLASH]]
        self.create_meteorites(self.time_for_meteorites_to_fall.get_y_coordinate(0))

        for x in range(number_of_players):
            player_keys = players_keys[x]
            self.players.append(Player(player_keys[0], player_keys[1], player_keys[2], f"images/player{x + 1}.png", f"images/laser{x + 1}.png"))

    def run(self):
        self.run_meteorite_creation()

    def run_meteorite_creation(self):
        self.time_since_last_meteorite += VelocityCalculator.time
        player_created_meteorite = key_is_hit(pygame.K_s)

        time_needed_for_new_meteorite = self.time_between_meteorites.get_y_coordinate(self.total_score)

        if player_created_meteorite or self.time_since_last_meteorite >= time_needed_for_new_meteorite:
            self.create_meteorites(self.time_for_meteorites_to_fall.get_y_coordinate(self.total_score))
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

        self.meteorites.append(Meteorite(LineSegment(Point(start_left_edge, -Meteorite.height), Point(end_left_edge, screen_height - Meteorite.height)), time_for_meteorite_to_fall))

    def get_components(self):
        player_components = []

        for player in self.players:
            player_components += player.get_components()

        return player_components + self.meteorites
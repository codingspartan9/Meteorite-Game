import pygame

from base.important_variables import screen_length
from gui_components.screen import Screen
from player import Player


class MeteoriteGameScreen(Screen):
    players = []
    is_versus = False

    def __init__(self, number_of_players, is_versus):
        super().__init__("images/galaxy.png")
        self.is_versus = is_versus

        players_keys = [[pygame.K_a, pygame.K_d, pygame.K_f], [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_SLASH]]
        self.players = []

        for x in range(number_of_players):
            player_keys = players_keys[x]
            self.players.append(Player(player_keys[0], player_keys[1], player_keys[2], f"images/player{x + 1}.png", f"images/laser{x + 1}.png"))

        self.set_players_left_edge()

    def set_players_left_edge(self):
        previous_player_left_edge = (screen_length / 2) + Player.length

        for player in self.players:
            player.left_edge = previous_player_left_edge - player.length
            previous_player_left_edge = player.left_edge

    def get_components(self):
        player_components = []

        for player in self.players:
            player_components += player.get_components()

        return player_components
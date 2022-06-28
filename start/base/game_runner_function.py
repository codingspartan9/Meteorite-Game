import pygame.event
import time

from base.important_variables import *
from base.history_keeper import HistoryKeeper
from base.velocity_calculator import VelocityCalculator

def run_game(main_screen):
    game_window.add_screen(main_screen)

    while True:
        start_time = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keyboard.run()
        game_window.run()

        total_time = time.time() - start_time
        HistoryKeeper.last_time = VelocityCalculator.time
        VelocityCalculator.time = total_time

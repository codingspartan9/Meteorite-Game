import os

from base.file_reader import FileReader
from gui_components.navigation_screen import NavigationScreen
from gui.meteorite_game_screen import MeteoriteGameScreen


class MainScreen(NavigationScreen):
    meteorite_game_screens = [MeteoriteGameScreen(1, False), MeteoriteGameScreen(2, False), MeteoriteGameScreen(2, True)]

    def __init__(self):
        super().__init__(["Single Player", "2 Player Co-op", "2 Player Versus"], self.meteorite_game_screens)

        file_reader = FileReader("high_score.txt")
        high_scores = file_reader.get_float_list("high_scores")

        for x in range(len(self.meteorite_game_screens)):
            self.meteorite_game_screens[x].high_score = int(high_scores[x])

    def save_data(self):
        high_scores = []

        for screen in self.meteorite_game_screens:
            high_scores.append(screen.high_score)

        high_score_string = high_scores.__str__().replace(" ", "")
        file_writer = open(os.getcwd() + "\\" + "high_score.txt", "w+")
        file_writer.write(f"high_scores:{high_score_string}")

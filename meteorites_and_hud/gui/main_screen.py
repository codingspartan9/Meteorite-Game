from gui_components.navigation_screen import NavigationScreen
from gui.meteorite_game_screen import MeteoriteGameScreen


class MainScreen(NavigationScreen):
    meteorite_game_screens = [MeteoriteGameScreen(1, False), MeteoriteGameScreen(2, False), MeteoriteGameScreen(2, True)]

    def __init__(self):
        super().__init__(["Single Player", "2 Player Co-op", "2 Player Versus"], self.meteorite_game_screens)




from base.game_runner_function import run_game
from gui.main_screen import MainScreen

main_screen = MainScreen()

try:
    run_game(main_screen)
except:
    main_screen.save_data()

from fishcode.src.window import WINDOW
from fishcode.src.game import Game

def run(game: Game):
    WINDOW.init()
    game.init()

    while WINDOW.running:
        WINDOW.update()
        game.update()
        game.draw()

def exit_game(window):
    window.running = False

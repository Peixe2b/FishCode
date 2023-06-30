from fishcode.src.game import Game
from fishcode.src.window import Window
from fishcode.src.wrapper import *

def run(game: Game):
    game.init()

    while True:
        game.update()
        game.draw()
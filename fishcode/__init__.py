from fishcode.src.wrapper import SDL
from fishcode.src.window import WINDOW
from fishcode.src.game import Game

def run(game: Game):
    SDL.SDL_Init()
    game.init()

    while WINDOW.running:
        game.update()
        game.draw()

from fishcode.src.window import WINDOW, GLFW
from fishcode.src.game import Game

def run(game: Game):
    WINDOW.init()
    game.init()

    while not GLFW.window_should_close(WINDOW.window):
        WINDOW.update()
        game.update()
        game.draw()

def terminate():
    GLFW.terminate()

def get_version():
    print(f"FishCode = 0.0.6")
    print(f"GLFW = {GLFW.get_version()}")

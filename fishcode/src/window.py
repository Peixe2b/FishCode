from fishcode.src.wrapper import SDL


class Window:
    def __init__(self):
        self.title = "FishCode"
        self.width = 500
        self.height = 500
        self.x = 120
        self.y = 120
        self.running = True
        self.window = SDL.SDL_CreateWindow(self.title, self.x, self.y, self.width, self.height, None, None)

WINDOW = Window()
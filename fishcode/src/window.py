import glfw as GLFW
from OpenGL import *
from OpenGL.GL import *


class Window:
    def __init__(self):
        self.__title = "FishCode"
        self.width = 720
        self.height = 480
        self.x = 120
        self.y = 120
        self.resizable = False
        self.bg_color = (0, 0, 0)
    
    def init(self):
        GLFW.init()
        GLFW.window_hint(GLFW.RESIZABLE, self.resizable)
        self.window = GLFW.create_window(self.width, self.height, self.__title, None, None)
        GLFW.make_context_current(self.window)

    def update(self):
        GLFW.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(
            self.bg_color[0], 
            self.bg_color[1],
            self.bg_color[2],
            0
        )
        GLFW.swap_buffers(self.window)

    def set_title(arg, title):
        self.__title = title

WINDOW = Window()

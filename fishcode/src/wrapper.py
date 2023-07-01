from ctypes import *

SDL = cdll.LoadLibrary("fishcode/libs/SDL2.dll")

def quit_sdl(window):
    SDL.SDL_Quit()
    SDL.SDL_DestroyWindow(window)
    window.running = False

def add_dll():
    pass

def remove_dll():
    pass

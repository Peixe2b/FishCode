import win32gui as gui
import win32con as con
import win32api as api


def window_proc(hwnd, msg, wparam, lparam):
    if msg == con.WM_QUIT:
        gui.PostQuitMessage(0)
        WINDOW.running = False
        return 0
    return gui.DefWindowProc(hwnd, msg, wparam, lparam)


class Window:
    def __init__(self):
        self.title = "FishCode"
        self.width = 500
        self.height = 500
        self.x = 120
        self.y = 120
        self.running = True
    
    def init(self):
        self.mainWindow = gui.WNDCLASS()
        self.mainWindow.lpszClassName = "MainWindow"
        self.mainWindow.lpfnWndProc = window_proc
        gui.RegisterClass(self.mainWindow)
        self.window = gui.CreateWindow(
            self.mainWindow.lpszClassName, self.title, 0, self.x, self.y,
            self.width, self.height, None, None, gui.GetModuleHandle(None),
            None
        )
        gui.ShowWindow(self.window, con.SW_SHOW)
        gui.UpdateWindow(self.window)

    def update(self):
        message = gui.GetMessage(None, 0, 0)
        if message[1] == con.WM_QUIT:
            gui.DestroyWindow(self.window)
            print("Exit")
        gui.TranslateMessage(message[1])
        gui.DispatchMessage(message[1])

WINDOW = Window()
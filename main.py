import fishcode


class App(fishcode.Game):
    def init(self):
        print("FISH")
    
    def update(self):
        print("LOADING")
    
    def draw(self):
        pass

app = App()
fishcode.run(app)
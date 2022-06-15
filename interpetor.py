import pyglet 
from pathlib import Path


class Interpetor:
    def __init__(self, statements):
        self.statement = statements
        
    def raise_error(self):
        raise Exception("Not in Library")
    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None
            
    def output(self):
        for i in self.statement:
            path = "Images/"+i+".jpg"
            window = pyglet.window.Window(1280, 900)
            image = pyglet.resource.image(path)

            @window.event
            def on_draw():
                window.clear()
                image.blit(0, 0)

            pyglet.app.run()
            
        
    
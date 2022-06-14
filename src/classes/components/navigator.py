from ursina import *

class Navigator(Entity):
    def __init__(self):
        super().__init__()
        self.left = Button("Anterior", model="circle", 
                        position = (-.62, .38, -20), 
                        color = color.rgba(80,80,80,100),
                        scale = .4,
                        _on_click = ())
        self.right = Button("Siguiente", model="circle", 
                        position = (.62, .38, -20), 
                        color = color.rgba(80,80,80,100),
                        scale = .4,
                        _on_click = ())
        self.title = ()
        self.back = Button("Regresar", model="circle", 
                        position = (-.62, .42, -20), 
                        color = color.rgba(80,80,80,100),
                        scale = .4,
                        _on_click = ())

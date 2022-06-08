from ursina import *

class Incidencia(WindowPanel):
    def __init__(self):
        super().__init__(
            title='Matriz de incidencia',
            content=(
                Text('V={}'),
                Space(height=1),
                Space(height=1),
                Space(height=1),
            ),
            enabled=False,
            position=(-.62,-.32))
    
        
    def show(self,state=()):
        if state != ():
            self.enabled = state
        else: 
            self.enabled = not self.enabled
        
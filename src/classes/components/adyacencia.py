from ursina import *

class Adyacencia(WindowPanel):
    def __init__(self):
        super().__init__(
            title='Matriz de adyacencia',
            content=(
                Text('V={}'),
                Space(height=5)
            ),
            enabled=False,
            position=(-.62,-.1))
    
        
    def show(self,state=()):
        if state != ():
            self.enabled = state
        else: 
            self.enabled = not self.enabled
        
    def update(self, text=()):
        if text:
            self.content[0].text = text
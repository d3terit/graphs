from ursina import *

class Content(WindowPanel):
    def __init__(self):
        super().__init__(
            title='Definición del grafo',
            content=(
                Text('V={}'),
                Space(height=1),
                Text('A={}'),
                Space(height=1)
            ),
            enabled=False,
            color = color.rgba(60,60,60,100),
            position=(.62,-.2))
    
        
    def update(self, nodes=(), edges=()):
        if nodes:
            self.content[0].text=nodes
        if edges:
            self.content[2].text=edges
        
    def show(self,state=()):
        if state != ():
            self.enabled = state
        else: 
            self.enabled = not self.enabled
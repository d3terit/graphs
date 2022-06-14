from ursina import *

class Hamilton(WindowPanel):
    def __init__(self, previous, next, reset):
        super().__init__(
            title='Circuitos Hamiltonianos',
            content=(
                Text('Recorridos'),
                Space(height=1),
                Button(text='Ver recorridos', color=color.black66, 
                _on_click = self.toggleContent, enabled = False),
                Button(text="Anterior", color=color.black33, 
                _on_click = previous, enabled = False),
                Button(text="Siguiente", color=color.black33, 
                _on_click = next, enabled = False)
            ),
            enabled=False,
            color = color.rgba(60,60,60,100),
            position=(.62,.4))
        self.reset = reset
        self.first = next
            
        
    def show(self):
        self.enabled = not self.enabled
        
    def data(self, data):
        self.enabled = True
        self.content[2].enabled = self.content[3].enabled = self.content[4].enabled = False
        if data:
            self.content[0].text = f'Recorridos encontrados:    {data}'
            self.content[2].enabled = True
        else:
            self.content[0].text = f'No hay recorridos hamiltonianos'
    
    def toggleContent(self):
        if self.content[2].text == "Ver recorridos":
            self.content[3].enabled = self.content[4].enabled = True
            self.first()
            self.content[2].text = "Ocultar recorridos"
        else:
            self.content[3].enabled = self.content[4].enabled = False
            self.reset()
            self.content[2].text = "Ver recorridos"


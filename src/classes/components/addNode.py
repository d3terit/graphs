from ursina import *

class AddNode(WindowPanel):
    def __init__(self, addNode):
        super().__init__(
            title='AÑADIR NODO',
            content=(
                Text('Nombre:'),
                InputField(),
                Space(height=1),
                Button(text='Añadir nodo', color=color.black66, 
                _on_click = self.add),
                Text('¡Nombre invalido!', color=color.red, enabled=False)
            ),
            popup=True,
            enabled=False,
            position=(0, .25))
        self.addNode = addNode
        self.bg.color = color.black90
        self.bg.highlight_color = color.black90
        self.bg.pressed_color = color.black90
        
    def show(self):
        self.content[1].text_field.text='A'
        self.content[1].text_field.render()
        self.enabled = True
        self.content[4].enabled=False

    def add(self):
        if len(self.content[1].text) == 1:
            self.addNode(self.content[1].text)
            self.enabled = False
        else:
            self.content[4].enabled=True
        
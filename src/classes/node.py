from ursina import *
from ursina.prefabs.radial_menu import *
from ursina.shaders import colored_lights_shader

class Node(Entity):
    def __init__(self, name, position, graph, uiconfig, active=True):
        super().__init__(position=position)
        self.name = name
        self.active = active
        self.obj = NodeObj(self, self.active)
        self.text = Title(self, name)
        self.graph = graph
        self.ui = uiconfig
        self.options = RadialMenu(self)

    def enable_radial_menu(self):
        self.options.enabled = True

    def remove(self):
        self.graph.removeNode(self)
        destroy(self)

    def moveCam(self):
        self.ui.moveCamera(self.position)

    def addEdge(self):
        self.graph.addPosition(self)

    def edit(self):
        self.graph.editNode(self)

    def currentState(self):
        return (self.graph.currentState())

    def updateEdges(self):
        self.graph.updateEdges(self)


class NodeObj(Button):
    def __init__(self, node=(), active=True):
        super().__init__(
            parent=node,
            model= 'sphere',
            collider = 'mesh',
            color=color.light_gray,
            highlight_color=color.white,
            shader = colored_lights_shader
        )
        self.node = node
        if not active:
            self.color = color.white10

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                if self.node.currentState():
                    self.node.addEdge()
                else:
                    self.node.moveCam()
            if key == 'right mouse down':
                self.node.enable_radial_menu()


class Title(Text):
    def __init__(self, node=(), text='Node'):
        super().__init__(
            text=text,
            parent=node,
            position=(-.1, .85, 0),
            scale=13
        )


class RadialMenu(RadialMenu):
    def __init__(self, node):
        self.e = RadialMenuButton(text='Eliminar', color=color.red)
        self.e.on_click = node.remove
        self.a = RadialMenuButton(text='Añadir\narista')
        self.a.on_click = node.addEdge
        self.r = RadialMenuButton(text='Editar')
        self.r.on_click = node.edit
        super().__init__(
            buttons=(self.a, self.r, self.e),
            enabled=False
        )

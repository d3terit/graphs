from ursina import *
from ursina.prefabs.radial_menu import *
import uuid

class Node(Entity):
    def __init__(self, name, position, graph, uiconfig, id = "", active=True):
        super().__init__(position=position)
        if len(id) == 0: self.id = uuid.uuid4()
        else: self.id = uuid.UUID(id)
        self.name = name
        self.active = active
        self.obj = NodeObj(self, self.active)
        self.text = Title(self, name)
        self.graph = graph
        self.ui = uiconfig
        self.options = RadialMenu(self)
        self.degrees = 0

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

    def hamilton(self):
        self.graph.testHamilton(self)

    def currentState(self):
        return (self.graph.currentState())

    def updateEdges(self):
        self.graph.updateEdges(self)

    def showName(self, state):
        self.text.enabled = state

    def getData(self):
        return ({"id":str(self.id),
                "name":self.name,
                "active":self.active,
                "position":list(self.position)})

class NodeObj(Button):
    def __init__(self, node=(), active=True):
        super().__init__(
            parent=node,
            model= 'sphere',
            collider = 'mesh',
            color=color.rgba(250,250,250,150),
            highlight_color=color.rgba(250,250,250,200),
            # shader = colored_lights_shader,
            texture = "./../assets/base"
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
    
    def update(self):
        if self.hovered:
            self.node.showName(True)
        else:
            self.node.showName(False)


class Title(Text):
    def __init__(self, node=(), text='Node'):
        super().__init__(
            text=text,
            parent=node,
            position=(-.1, .85, 0),
            scale=13
        )
        self.enabled=False


class RadialMenu(RadialMenu):
    def __init__(self, node):
        self.e = RadialMenuButton(text='Eliminar', color=color.red)
        self.e.on_click = node.remove
        self.a = RadialMenuButton(text='Añadir\narista')
        self.a.on_click = node.addEdge
        self.r = RadialMenuButton(text='Editar')
        self.r.on_click = node.edit
        self.h = RadialMenuButton(text='HMLTN')
        self.h.on_click = node.hamilton
        super().__init__(
            buttons=(self.a, self.r, self.e, self.h),
            enabled=False
        )

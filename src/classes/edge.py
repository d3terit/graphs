import numpy as np
from ursina import *
from ursina.prefabs.radial_menu import *

class Edge(Button):
    def __init__(self, nodeStart, nodeEnd, graph,  direction, weight):
        super().__init__(
            model='edge',
            parent=nodeStart,
            collider = 'mesh',
            color=color.rgba(0, 250, 250, 150),
            highlight_color = color.rgba(250, 0, 0, 200),
            texture = "./../assets/edge",
            scale = 2
        )
        self.nodeStart = nodeStart
        self.nodeEnd = nodeEnd
        self.graph = graph
        self.direction = direction
        self.weight = weight
        self.reEstructure()
        self.options = RadialMenu(self)
        self.texoffset = 0.0
        self.state = True
        self.flowTo = 1
    
    def reEstructure(self):
        dist = distance(self.nodeStart.position, self.nodeEnd.position)
        dist_xz = distance_xz(self.nodeStart.position, self.nodeEnd.position)
        dir = self.nodeEnd.position - self.nodeStart.position
        ry = np.degrees(np.arccos(dir.x/dist_xz))
        rz = np.degrees(np.arccos(dir.y/dist))
        if dir.z > 0: ry *= -1
        self.rotation = (0,ry,rz)
        self.scale_y = dist/2

    def input(self, key):
        if self.hovered and self.state and key  == 'right mouse down':
                self.enable_radial_menu()

    def enable_radial_menu(self):
        self.options.enabled = True
    
    def remove(self):
        self.graph.removeEdge(self)

    def edit(self):
        print('edit')

    def getData(self):
        return ({"nodeStart":str(self.nodeStart.id),
                "nodeEnd":str(self.nodeEnd.id),
                "direction":self.direction,
                "weight":self.weight})

    def update(self):                               
        self.texoffset -= time.dt * 0.5 * self.flowTo
        self.texture_offset = (0,self.texoffset) 

    def setState(self, state, flowTo):
        self.state = state
        self.flowTo = flowTo
        if flowTo == 0:
            self.color = color.rgba(250,0,250,150)
            self.highlight_color = color.rgba(250,0,250,150)
        else:
            self.color=color.rgba(0, 250, 250, 150)
            if state: self.highlight_color = color.rgba(250, 0, 0, 200)
            else: self.highlight_color = color.rgba(0, 250, 250, 150)

class RadialMenu(RadialMenu):
    def __init__(self, edge):
        self.e = RadialMenuButton(text='Eliminar', color=color.red, on_click = edge.remove)
        self.r = RadialMenuButton(text='Editar', on_click = edge.edit)
        super().__init__(
            buttons=(self.r, self.e),
            enabled=False
        )

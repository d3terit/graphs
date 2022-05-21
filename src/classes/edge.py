import numpy as np
from ursina import *
from ursina.prefabs.radial_menu import *

class Edge(Button):
    def __init__(self, nodeStart, nodeEnd, graph, direction=False):
        super().__init__(
            model='edge',
            parent=nodeStart,
            collider = 'mesh',
            color=color.cyan,
            highlight_color = color.red
        )
        self.nodeStart = nodeStart
        self.nodeEnd = nodeEnd
        self.reEstructure()
        self.direction = direction
        self.graph = graph
        self.weight = 0
        self.options = RadialMenu(self)
    
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
        if self.hovered and key == 'right mouse down':
                self.enable_radial_menu()

    def enable_radial_menu(self):
        self.options.enabled = True
    
    def remove(self):
        self.graph.removeEdge(self)

    def edit(self):
        print('edit')

class RadialMenu(RadialMenu):
    def __init__(self, edge):
        self.e = RadialMenuButton(text='Eliminar', color=color.red, on_click = edge.remove)
        self.r = RadialMenuButton(text='Editar', on_click = edge.edit)
        super().__init__(
            buttons=(self.r, self.e),
            enabled=False
        )

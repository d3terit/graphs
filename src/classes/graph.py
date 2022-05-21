from ursina import *

from ..utils.controller import Controller
from .node import Node
from .edge import Edge


class Graph(Entity):
    nodes = []
    edges = []
    subGraphs = []

    def __init__(self, name, uiconfig):
        super().__init__(
            parent=scene
        )
        self.name = name
        self.nodes = []
        self.edges = []
        self.subGraphs = []
        self.uiconfig = uiconfig
        self.select = []
        self.controller = Controller()

    def addNode(self, position=Vec3(0, 0, 0),name=''):
        for n in self.nodes:
            dist = distance(n.position, position)
            if(dist <= 1.3):
                return False
        self.nodes.append(Node(name, position, self, self.uiconfig))
        return True

    def removeNode(self, node):
        # [self.edgesCompar2(node, edge) for edge in self.edges]
        self.edgesCompar(node)
        if self.controller.node == node:
            self.controller.setNode(())
        self.nodes.remove(node)
    
    def removeEdge(self, edge):
        self.edges.remove(edge)
        destroy(edge)

    def edgesCompar(self, node):
        current = False
        for edge in self.edges:
            if edge.nodeStart == node or edge.nodeEnd == node:
                current = True
                destroy(edge)
                self.edges.remove(edge)
                pass
        if current:
            self.edgesCompar(node)

    def edgesCompar2(self, node, edge):
        if edge.nodeStart == node or edge.nodeEnd == node:
            destroy(edge)
            self.edges.remove(edge)

    def addPosition(self, node):
        self.select.append(node)
        if len(self.select) == 2:
            self.addEdge()
            self.select = []

    def addEdge(self):
        self.edges.append(Edge(self.select[0], self.select[1], self))

    def editNode(self, node):
        self.controller.setNode(node)

    def currentState(self):
        if len(self.select) > 0:
            return True
        return False

    def updateEdges(self, node):
        for edge in self.edges:
            if edge.nodeStart == node or edge.nodeEnd == node:
                edge.reEstructure()

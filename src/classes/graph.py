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
        self.id = 1;

    def addNode(self, position=Vec3(0, 0, 0),name=''):
        for n in self.nodes:
            dist = distance(n.position, position)
            if(dist <= 1.3):
                return False
        self.nodes.append(Node(self.id, name.upper(), position, self, self.uiconfig))
        self.id += 1
        self.calNodes()
        self.adyacencia()
        return True

    def calNodes(self):
        v = ""
        for n in self.nodes:
            v+= f' {n.name},'
        v= "V = {" + f'{v[:-1]}' + " }"
        self.uiconfig.content.update(nodes=v)
    
    def calEdges(self):
        a = ""
        i = 0
        for e in self.edges:
            i+= 1
            a+= f' {e.nodeStart.name}{e.nodeEnd.name},'
            if i>8:
                a+='\n'
                i = 0
        a = "A= {" + f'{a[:-1]}' + " }"
        self.uiconfig.content.update(edges=a)
    
    def adyacencia(self):
        m = [[]]
        m[0].append('  ')
        for n in self.nodes:
            m[0].append(n.name)
            m.append([n.name])
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                m[i+1].append(0)
        for e in self.edges:
            i = self.nodes.index(e.nodeStart)
            j = self.nodes.index(e.nodeEnd)
            m[i+1][j+1] = 1
            m[j+1][i+1] = 1
        r = ""
        for i in m:
            for j in i:
                r += f'{str(j)} '
            r+='\n'
        self.uiconfig.adyacencia.update(r)

    def removeNode(self, node):
        self.edgesCompar(node)
        if self.controller.node == node:
            self.editNode(())
        self.nodes.remove(node)
        self.calNodes()
        self.adyacencia()
        self.calEdges()
        self.adyacencia()
    
    def removeEdge(self, edge):
        self.edges.remove(edge)
        destroy(edge)
        self.calEdges()
        self.adyacencia()

    def edgesCompar(self, node):
        current = False
        for edge in self.edges:
            if edge.nodeStart == node or edge.nodeEnd == node:
                current = True
                self.removeEdge(edge)
                pass
        if current:
            self.edgesCompar(node)

    def addPosition(self, node):
        self.select.append(node)
        if len(self.select) == 2:
            self.addEdge()
            self.select = []

    def addEdge(self):
        state = True
        for e in self.edges:
            if (e.nodeStart == self.select[0] and e.nodeEnd == self.select[1]) or (e.nodeStart == self.select[1] and e.nodeEnd == self.select[0]):
                state = False
                pass
        if state and self.select[0] != self.select[1]:
            self.edges.append(Edge(self.select[0], self.select[1], self))
            self.calEdges()
            self.adyacencia()

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

    def getData(self):
        data = {}
        data["nodes"] = []
        data["edges"] = []
        for node in self.nodes:
            data["nodes"].append(node.getData())
        for edge in self.edges:
            data["edges"].append(edge.getData())
        return data
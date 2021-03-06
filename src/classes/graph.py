import uuid
from ursina import *

from ..utils.hamiltoniano import Hamiltoniano
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
        self.hamilton = Hamiltoniano(self)
        self.edit = True

    def addNode(self, position=Vec3(0, 0, 0),name=''):
        self.uiconfig.resetHamilton()
        for n in self.nodes:
            dist = distance(n.position, position)
            if(dist <= 1.3):
                return False
        self.nodes.append(Node(name.upper(), position, self, self.uiconfig))
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
            if e.flowTo != 0:
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
            if e.flowTo != 0:
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
        self.uiconfig.resetHamilton()
        self.edgesCompar(node)
        if self.controller.node == node:
            self.editNode(())
        self.nodes.remove(node)
        self.calNodes()
        self.adyacencia()
    
    def removeEdge(self, edge):
        self.uiconfig.resetHamilton()
        edge.nodeStart.degrees -= 1
        edge.nodeEnd.degrees -= 1
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
                break
        if current:
            self.edgesCompar(node)

    def addPosition(self, node):
        self.select.append(node)
        if len(self.select) == 2:
            self.addEdge(self.select[0], self.select[1])
            self.select.clear()

    def addEdge(self, nodeStart, nodeEnd, direction = False, weight = 0):
        self.uiconfig.resetHamilton()
        state = True
        for e in self.edges:
            if (e.nodeStart == nodeStart and e.nodeEnd == nodeEnd) or (e.nodeStart == nodeEnd and e.nodeEnd == nodeStart):
                state = False
                break
        if state and nodeStart != nodeEnd:
            nodeStart.degrees += 1
            nodeEnd.degrees += 1
            self.edges.append(Edge(nodeStart, nodeEnd, self, direction, weight))
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
    
    def getNode(self, id):
        for node in self.nodes:
            if id == str(node.id):
                return (node)
        return False

    def loadData(self,data):
        self.uiconfig.resetHamilton()
        self.subGraphs.clear()
        [destroy(node) for node in self.nodes]
        self.nodes.clear() 
        for node in data["nodes"]:
            pos = Vec3(node["position"][0],node["position"][1],node["position"][2])
            self.nodes.append(Node(node["name"].upper(), pos, self, self.uiconfig, node["id"],node["active"]))
        [destroy(edge) for edge in self.edges]
        self.edges.clear()
        for edge in data["edges"]:
            nodeStart = self.getNode(edge["nodeStart"])
            nodeEnd = self.getNode(edge["nodeEnd"])
            self.addEdge(nodeStart, nodeEnd, edge["direction"], edge["weight"])
        self.calNodes()
        self.edit = True

    def testHamilton(self, nodeStart):
        self.uiconfig.events.showHamilton = True
        result = True
        for node in self.nodes:
            if node.degrees < 2:
                result = False
        if result: result = self.hamilton.test(nodeStart)
        if result: 
            self.subGraphs = result
            self.uiconfig.dataHamilton(len(result))
        else: self.uiconfig.dataHamilton(False)

    def showSubGraph(self, index):
        self.edit= False
        if index < 0: path = f"{len(self.subGraphs) + index + 1}: "
        else: path = f"{index+1}: "
        for edge in self.edges:
            edge.setState(False,0)
        for i in range(len(self.subGraphs[index])-1):
            path += f" {self.subGraphs[index][i].name}  - "
            for edge in self.edges:
                if str(edge.nodeStart.id) == str(self.subGraphs[index][i].id) and str(edge.nodeEnd.id) == str(self.subGraphs[index][i+1].id):
                    edge.setState(False,1)
                else:
                    if str(edge.nodeEnd.id) == str(self.subGraphs[index][i].id) and str(edge.nodeStart.id) == str(self.subGraphs[index][i+1].id):
                        edge.setState(False,-1)
        path += f" {self.subGraphs[index][0].name}"
        self.adyacencia()
        self.calEdges()
        return path
                    
    def exitSubGraphs(self):
        self.edit = True
        for edge in self.edges:
            edge.setState(True,1)
        self.adyacencia()
        self.calEdges()
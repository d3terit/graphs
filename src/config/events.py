from ursina import *

from ..classes.graph import Graph
from .uiConfig import UiConfig

class Events():
    def __init__(self, uiConfig:UiConfig, graph:Graph):
        self.uiConfig = uiConfig
        self.uiConfig.events = self
        self.graph = graph

    def event(self, key):
        if key == 'n':
            self.uiConfig.showAddNode()
        if key == 'k':
            self.uiConfig.moveCamera((0,0,0))

    def addNode(self, position,name):
        if not self.graph.addNode(position,name):
            print('Ya existe el nodo')

    
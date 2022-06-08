from ursina import *

from ..classes.graph import Graph
from .uiConfig import UiConfig

class Events():
    def __init__(self, uiConfig:UiConfig, graph:Graph):
        self.uiConfig = uiConfig
        self.uiConfig.events= self
        self.graph = graph

    def event(self, key):
        match key:
            case 'n':
                self.uiConfig.showAddNode() 
            case 'k':
                self.uiConfig.moveCamera((0,0,0))
            case 'r':
                self.graph.editNode(())
            case 'i':
                self.uiConfig.toggleContent()
            case 'g':
                self.uiConfig.showSaveData(self.graph.getData())

    def addNode(self, position,name):
        return self.graph.addNode(position,name)

    
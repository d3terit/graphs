from ursina import *

from ..classes.graph import Graph
from .uiConfig import UiConfig

class Events():
    def __init__(self, uiConfig:UiConfig, graph:Graph):
        self.uiConfig = uiConfig
        self.uiConfig.events= self
        self.graph = graph
        self.showHamilton = False

    def event(self, key):
        openData = self.uiConfig.openData.enabled
        saveData = self.uiConfig.saveData.enabled
        newNodo = self.uiConfig.add.enabled
        match key:
            case 'n':
                if not (saveData or openData): self.uiConfig.showAddNode() 
            case 'k':
                if not (saveData or openData or newNodo): self.uiConfig.moveCamera((0,0,0))
            case 'r':
                self.graph.editNode(())
            case 'i':
                if not (saveData or openData): self.uiConfig.toggleContent()
            case 'g':
                if not (openData or newNodo): self.uiConfig.showSaveData(self.graph.getData())
            case 'o':
                if not (saveData or newNodo): self.uiConfig.showOpenData()
            case 'h':
                if not(newNodo or saveData or openData) and self.showHamilton: self.uiConfig.showHamilton()
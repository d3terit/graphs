import json
from ursina import *

from ..classes.components.navigator import Navigator
from ..classes.components.hamilton import Hamilton
from ..classes.components.openData import OpenData
from ..classes.components.saveData import SaveData
from ..classes.components.incidencia import Incidencia
from ..classes.components.adyacencia import Adyacencia
from ..classes.components.content import Content
from ..classes.components.addNode import AddNode
class UiConfig:
    def __init__(self,events=()):
        # window.fullscreen = True
        window.borderless = False
        window.exit_button.visible = False
        window.title = "3D Graphs"
        window.color = color.black90
        self.editor = EditorCamera()
        self.coor = Entity(parent=camera.ui, position=(-.85,.42))
        self.x = Text('x: 0', parent=self.coor, position=(0,.03,0), scale=.8)
        self.y = Text('y: 0', parent=self.coor, position=(0,0,0), scale=.8)
        self.z = Text('z: 0', parent=self.coor, position=(0,-.03,0), scale=.8)
        self.events = events
        self.add = AddNode(self.addNode)
        self.content = Content()
        self.incidencia = Incidencia()
        self.adyacencia = Adyacencia()
        self.hamilton = Hamilton()
        self.saveData = SaveData()
        self.openData = OpenData(self.submit)
        # self.navigator = Navigator()

    def moveCamera(self, position, zoom=-20):
        self.editor.set_position(position)
        self.editor.target_z = zoom
    def updateCoor(self):
        coor = camera.world_position + (camera.forward)*10
        self.x.text = f'x: {round(coor.x,3)}'
        self.y.text = f'y: {round(coor.y,3)}'
        self.z.text = f'z: {round(coor.z,3)}'

    def updateUi(self):
        self.updateCoor()

    def addNode(self,name):
        return self.events.graph.addNode((camera.world_position + (camera.forward)*10),name)
            
    def showAddNode(self):
        self.add.show()
        # self.content.show(False)
        
    def toggleContent(self):
        self.adyacencia.show()
        self.content.show()

    def showHamilton(self):
        self.hamilton.show()
    
    def dataHamilton(self, data):
        self.hamilton.data(data)
    
    def showSaveData(self,data):
        self.saveData.show(data)

    def showOpenData(self):
        self.openData.show()

    def submit(self,paths):
        file = open(paths[0])
        data = json.load(file)
        self.events.graph.loadData(data)

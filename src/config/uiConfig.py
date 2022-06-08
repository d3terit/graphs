from ursina import *

from ..classes.components.saveData import SaveData
from ..classes.components.incidencia import Incidencia
from ..classes.components.adyacencia import Adyacencia
from ..classes.components.content import Content
from ..classes.components.addNode import AddNode
class UiConfig:
    def __init__(self,events=()):
        # window.fullscreen = True
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
        self.saveData = SaveData()

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
        return self.events.addNode((camera.world_position + (camera.forward)*10),name)
            
    def showAddNode(self):
        self.add.show()
        # self.content.show(False)
        
    def toggleContent(self):
        # self.adyacencia.show()
        self.adyacencia.show()
        self.content.show()
    
    def showSaveData(self,data):
        self.saveData.show(data)

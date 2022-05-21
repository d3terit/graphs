from ursina import *

from ..classes.components.addNode import AddNode
class UiConfig:
    def __init__(self):
        #window.fullscreen = True
        window.color = color.black90
        self.editor = EditorCamera()
        self.coor = Entity(parent=camera.ui, position=(-.85,.42))
        self.x = Text('x: 0', parent=self.coor, position=(0,.03,0), scale=.8)
        self.y = Text('y: 0', parent=self.coor, position=(0,0,0), scale=.8)
        self.z = Text('z: 0', parent=self.coor, position=(0,-.03,0), scale=.8)
        self.events = ()
        self.add = AddNode(self.addNode)

    def moveCamera(self, position, zoom=-20):
        self.editor.set_position(position)
        self.editor.target_z = zoom
    def updateCoor(self):
        coor = camera.world_position + (camera.forward)*10
        self.x.text = f'x: {coor.x}'
        self.y.text = f'y: {coor.y}'
        self.z.text = f'z: {coor.z}'

    def updateUi(self):
        self.updateCoor()

    def addNode(self,name):
        self.events.addNode((camera.world_position + (camera.forward)*10),name)
            
    def showAddNode(self):
        self.add.show()
        
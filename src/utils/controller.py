from ursina import *

from ..classes.axis import Axis
class Controller:
    def __init__(self):
        self.axisX = Axis(
            node=(),
            lineRotate = (0,0,-90),
            parent=scene, model='../assets/arrow.obj',
            collider = "mesh",
            rotation = (0,0,90),
            position = (.5,0,0),
            color=color.yellow,
            plane_direction=(0, 0, 0),
            lock=(0, 1, 0),
            enabled = False)
        self.axisY = Axis(
            node=(),
            lineRotate = (0,0,90),
            parent=scene, model='../assets/arrow.obj',
            collider = "mesh",
            rotation = (0,0,0),
            position = (0,.5,0),
            color=color.red,
            plane_direction=(0, 0, 0),
            lock=(1, 0, 0),
            enabled = False)
        self.axisZ = Axis(
            node=(),
            lineRotate = (0,0,90),
            parent=scene, model='../assets/arrow.obj',
            collider = "mesh",
            rotation = (-90,0,0),
            position = (0,0,-.5),
            color=color.blue,
            plane_direction=(1, 0, 0),
            lock=(0, 1, 0),
            enabled = False)
        self.node = ()

    def setNode(self,node):
        self.node = node
        self.axisX.changeNode(node)
        self.axisY.changeNode(node)
        self.axisZ.changeNode(node)
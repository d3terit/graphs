from ursina import *
from src.classes.graph import Graph
from src.config.events import Events
from src.config.uiConfig import UiConfig

app = Ursina()

uiconfig = UiConfig()

i = Graph('1', uiconfig)

events = Events(uiconfig, i)

i.addNode(position=(0, 2, 4))
i.addNode(position=(-5, 3, 0))
i.addNode(position=(5, -4, 1))

graphs = []

def showGraph(currentGraph):
    scene.clear()
    scene.entities.append(currentGraph)

def addGraph():
    g = Graph('new')
    showGraph(g)

def input(key): 
    events.event(key)

def update():
    uiconfig.updateUi()


app.run()

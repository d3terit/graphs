from ursina import *
from src.classes.graph import Graph
from src.config.events import Events
from src.config.uiConfig import UiConfig

app = Ursina()

uiconfig = UiConfig()

i = Graph('1', uiconfig)

events = Events(uiconfig, i)

i.addNode((0, 2, 4),"a")
i.addNode((-5, 3, 0),"b")
i.addNode((5, -4, 1),"c"),

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

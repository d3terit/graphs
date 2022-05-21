from ursina import *

class Axis(Button):

    _z_plane = Entity(name='_z_plane', scale=(9999,9999), enabled=False, eternal=True)

    def __init__(self, node, lineRotate, **kwargs):
        super().__init__(**kwargs)
        self.dragging = False
        self.start_offset = (0,0,0)
        self.plane_direction = (0,0,1)
        self.lock = Vec3(0,0,0)
        self.node = node
        self.line =  Entity(model='line',
                    scale=9999, 
                    parent=self, 
                    enabled=False, 
                    rotation = lineRotate, 
                    color = self.color)
        
        if not Axis._z_plane.model: # set these after game start so it can load the model
            Axis._z_plane.model = 'quad'
            Axis._z_plane.collider = Mesh(vertices=((-0.5, -0.5, 0.0), (0.5, -0.5, 0.0), (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0)), triangles=((0,1,2,3),), mode='triangle')
            Axis._z_plane.color = color.clear


        for key, value in kwargs.items():
            if key in self.attributes:
                continue
            setattr(self, key, value)

    def input(self, key):
        if self.hovered and key == 'left mouse down':
            self.start_dragging()

        if self.dragging and key == 'left mouse up':
            self.stop_dragging()


    def start_dragging(self):
        point = Vec3(0,0,0)
        if mouse.world_point:
            point = mouse.world_point
        Axis._z_plane.world_position = point
        Axis._z_plane.look_at(Axis._z_plane.position - Vec3(*self.plane_direction))
        Axis._z_plane.world_parent = scene
        self.start_offset = point - self.world_position
        self.dragging = True
        Axis._z_plane.enabled = True
        mouse.traverse_target = Axis._z_plane
        self.line.enabled = True

    def stop_dragging(self):
        self.dragging = False
        Axis._z_plane.enabled = False
        mouse.traverse_target = scene
        self.line.enabled = False

    def update(self):
        if self.dragging:
            if mouse.world_point:
                if not self.lock[0]:
                    self.node.x = mouse.world_point[0] - self.start_offset[0]
                if not self.lock[1]:
                    self.node.y = mouse.world_point[1] - self.start_offset[1]
                if not self.lock[2]:
                    self.node.z = mouse.world_point[2] - self.start_offset[2]
                self.node.updateEdges()

    def changeNode(self, node):
        self.node = node
        if node: 
            self.parent = node
            self.enabled = True
        else: 
            self.parent = scene
            self.enabled = False
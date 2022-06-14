from ursina import *
cubes = []
app = Ursina()
EditorCamera()
cube = Entity(model='cube', color=color.white, scale=(2,6,2), texture="./src/assets/water")
cubes.append(cube)                                  # Add the cube to the list
cube2 = Entity(model='cube', color=color.rgba(255,255,255,128), scale=(2.5,6,2.5), texture="./src/assets/water")
cubes.append(cube2)         
...
random_generator = random.Random()      # Create a random number generator
texoffset = 0.0         
texoffset2 = 0.0                     # define a variable that will keep the texture offset
...
...
def update():
    for entity in cubes:
        entity.rotation_y += time.dt * 5                # Rotate all the cubes every time update is called
    if held_keys['q']:                               # If q is pressed
        camera.position += (0, time.dt, 0)                 # move up vertically
    if held_keys['a']:                               # If a is pressed
        camera.position -= (0, time.dt, 0)                 # move down vertically

    global texoffset                                 
    global texoffset2                                 
    texoffset += time.dt * 0.2                       
    setattr(cube, "texture_offset", (0, texoffset))  
    texoffset2 += time.dt * 0.3                       # Add a value to this variable, but different to the first one
    setattr(cube2, "texture_offset", (0, texoffset2))  # Assign as a texture offset of the second cube
...
app.run()
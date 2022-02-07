from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
#cube = Entity(model='cube', color=color.red, texture='white_cube', scale=2)



#def update():
#    cube.rotation_x = cube.rotation_x + 0.25
#    cube.rotation_y = cube.rotation_y + 0.05

player = Entity(model='cube', color=color.green, texture='white_cube', scale=2)
#player = Entity(model='model.obj', color=color.green, texture='white_cube', scale=2)


def update():
    player.x += held_keys['d'] * 0.1
    player.x -= held_keys['a'] * 0.1
    player.y += held_keys['w'] * 0.1
    player.y -= held_keys['s'] * 0.1

    if held_keys['t']:
        player.rotation_x = 0 
        player.rotation_y = 0  

    player.rotation_x += held_keys['r'] * 5
    player.rotation_y += held_keys['r'] * 5 





app.run()


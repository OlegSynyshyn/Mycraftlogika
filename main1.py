from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
from settings import *
from models import Block, Map

sky = Sky(texture=' sky_sunset')

map = Map()
map.generate()

tree = Entity(model="assets\\minecraft_tree\\scene.gltf", scale=5, collider='box', origin_y=-.5)


ground = Entity(model='plane', collider='box', scale=150, texture='grass', texture_scale=(4,4))
ground.y=0


player = FirstPersonController()
window.fullscreen = True
app.run()
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
from settings import *
from models import Block, Map, Player

sky = Sky(texture=' sky_sunset')
sun = DirectionalLight(shadows=True)
sun.look_at(Vec3(1, -1, 1))

map = Map()
map.generate()

player = Player(map)
window.fullscreen = True
app.run()
from ursina import *
from ursina import scene
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.scene import instance as scene
from settings import *


class Block(Button):
    def __init__(self, pos, texture_id=1, **kwargs):
        super().__init__(parent=scene,
                         color=color.white,
                         highlight_color=color.gray,
                         model='cube',
                         texture=block_textures[texture_id],
                         position = pos, 
                         scale=1,
                         collider='box',
                         origin_y=-0.5,
                         **kwargs)

class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, collider=None, **kwargs)
        self.blocks = {}

    def generate(self):
        for x in range(MAP_SIZE):
            for z in range(MAP_SIZE):
                cube = Block((x, 0, z), 4)
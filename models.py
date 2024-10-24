from ursina import *
from ursina import scene
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.scene import instance as scene
from settings import *
from ursina.shaders import basic_lighting_shader
from perlin_noise import PerlinNoise
from numpy import floor


class Tree(Button):
    def __init__(self, pos, **kwargs):
        super().__init__(parent=scene,
                         color=color.color(0,0, random.uniform(0.9, 1)),
                         highlight_color=color.gray,
                         model="minecraft_tree\\scene.gltf",
                         position = pos, 
                         scale=5,
                         collider='box',
                         origin_y=.5,
                         shader = basic_lighting_shader,
                         **kwargs)



class Block(Button):

    current = DEFAULT_BLOCK
    def __init__(self, pos, texture_id=3, **kwargs):
        super().__init__(parent=scene,
                         color=color.color(0,0, random.uniform(0.9, 1)),
                         highlight_color=color.gray,
                         model='cube',
                         texture=block_textures[texture_id],
                         position = pos, 
                         scale=1,
                         collider='box',
                         origin_y=-.5,
                         shader = basic_lighting_shader,
                         **kwargs)

class Map(Entity):
    def __init__(self, **kwargs):
        super().__init__(model=None, collider=None, **kwargs)
        self.blocks = {}
        self.noise = PerlinNoise(octaves=2, seed=3505)

    def generate(self):
        for x in range(MAP_SIZE):
            for z in range(MAP_SIZE):
                y = floor(self.noise([x/24, z/24])*6)
                cube = Block((x, y, z), DEFAULT_BLOCK)

                rand_num = random.randint(1,TREE_DENSITY)
                if rand_num == 75:
                    Tree((x,y+1,z))




class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.held_block = Entity(model='cube', texture=block_textures[Block.current], parent=camera.ui,
                                 position=(0.75, -0.4), rotation=Vec3(0, 0, 0),
                                 shader=basic_lighting_shader,
                                 scale = 0.2
                                 )


    def input(self, key):
        super().input(key)

        if key == "left mouse down" and mouse.hovered_entity:
            destroy(mouse.hovered_entity)

        if key == "right mouse down" and mouse.hovered_entity:
            hit_info = raycast(camera.world_position, camera.forward, distance=10)
            if hit_info.hit and isinstance(hit_info.entity, Block):
                Block(hit_info.entity.position + hit_info.normal, Block.current)
        if key == "scroll up":
            Block.current += 1
            if Block.current >= len(block_textures):
                Block.current = 0
            self.held_block.texture = block_textures[Block.current]
        if key == "scroll down":
            Block.current -= 1
            if Block.current < 0:
                Block.current = len(block_textures)-1
            self.held_block.texture = block_textures[Block.current]

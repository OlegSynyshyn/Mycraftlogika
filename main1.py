from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
from settings import *
from models import *

class GameController:
    def __init__(self):
        sky = Sky(texture=' sky_sunset')
        sun = DirectionalLight(shadows=True)
        sun.look_at(Vec3(1, -1, 1))

        scene.blocks = {}

        self.map = Map()
        self.map.generate()

        self.player = Player(self.map)

    def save(self):
        game_data = {
            "player_pos": (self.player.x, self.player.y, self.player.z),
            "blocks": [],
            "trees": [],


        }

        for block_pos, block_id in scene.blocks.items():
            game_data["blocks"].append((block_pos, block_id))

        with open('save.dat', "wb") as file:
            pickle.dump(game_data, file)

   

game = GameController()

def input(key):
    if key == 'k':
        game.save()
window.fullscreen = True
app.run()
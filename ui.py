from ursina import *

Text.default_font = "Frijole-Regular.ttf"

class MenuButton(Button):
    def __init__(self, text, action, x, y, parent):
        super().__init__(text=text, on_click=action, x=x, y=y, parent=parent,
                         scale=(0.6, 0.1),
                         origin=(0, 0),
                         ignore_paused=True,
                         texture='blocks\stone.png',
                         color=color.color(0, 0, random.uniform(0.9, 1)),
                         highlight_color=color.gray,
                         highlight_scale=1.05,
                         pressed_scale=1.05,
                         )



class Menu(Entity):
    def __init__(self, game, **kwargs):
        super().__init__(parent=camera.ui, ignore_paused = True, **kwargs)
        self.bg = Sprite(texture='w11288-small.png', parent=self,z=1, color=color.white, scale = 0.10 )
        
        self.title = Text(text="Minecraft", scale=5,
                          parent=self, origin=(0, 0), x=0, y=0.35)
        
        MenuButton("New game", application.quit, 0, 0.15, self)
        MenuButton("Load", application.quit, 0, 0.02, self)
        MenuButton("Save", application.quit, 0, -0.11, self)
        MenuButton("Exit", application.quit, 0, 0.02, self)


    def toggle_menu(self):
        application.paused = not application.paused
        self.enabled = application.paused
        self.visible = self.visible
        mouse.locked = not mouse.locked
        mouse.visible = not mouse.visible


if __name__ == "__main__":
    app = Ursina()
    menu = Menu(app)
    app.run()


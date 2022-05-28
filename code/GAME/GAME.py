# import main_class_lib as Pix
from GAME_ENGINE import *
from PG_TOOLS import *
# from UI_0 import *
# from enum import Enum


class Game:
    def __init__(self, engine, width = 360, height = 480, name = "Busy_game💀", FPS = 60):
        self.name = name
        self.running = True
        self.width   = width
        self.height  = height
        # /////////////////////////////// #

        self.tools = PG_tools()

        self.UI_pg = UI_Pygame(width, height, FPS)
        self.engine = engine

    def start(self):
        self.UI_pg.set_caption(self.name)
        self.UI_pg.start()

        while self.running:
            self.game_cycle()
            self.UI_pg.draw(self.engine.update())
            self.UI_pg.tick()
            self.events()

    def events(self, *args):
        for event in self.UI_pg.get_events():
            if event.type == self.UI_pg.EVENTS.QUIT.value:
                self.running = False
            for fnk in args:
                fnk(event)

    def game_cycle(self):
        pass

    def check_any_pressed_key(self):
        keys = pygame.key.get_pressed()
        if any(key for key in keys):
            # self.condition = status.START_GAME
            return 1
        return 0


class Menu:
    def __init__(self):
        self.button = None

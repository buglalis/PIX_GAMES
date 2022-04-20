import main_class_lib as Pix
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
        self.tools.set_caption(self.name)
        self.tools.start()

        while self.running:
            self.game_cycle()
            self.UI_pg.draw(self.engine.update())
            self.UI_pg.tick()
            self.events()
            self.tests()
            # self.tools.key_events()


    def events(self, *args):
        for event in self.tools.get_events():
            if event.type == self.tools.EVENTS.QUIT.value:
                self.running = False
            for fnk in args:
                fnk()

    def game_cycle(self):
        pass

    def tests(self):
        pass

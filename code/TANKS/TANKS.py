import sys
sys.path.insert(0, "../GAME")
from GAME import *
from TANKS_ENGINE import *

PLAYER_TANK_SPEED = 5
BULLED_SPEED      = 1




class Tanks(Game):
    def __init__(self):
        super().__init__(Tanks_engine(), width = 1000, height = 650, name = "TANKS💀")

    def start(self):
        self.engine.test()
        super().start()

    def game_cycle(self):
        self.UI_pg.fill((24, 59, 100))

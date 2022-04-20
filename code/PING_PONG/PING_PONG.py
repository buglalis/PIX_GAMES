import sys
sys.path.insert(0, "../GAME")
from GAME import *
from PING_PONG_ENGINE import *

PLAYER_SPEED = 5
BALL_SPEED   = 1
GATE_WIDTH   = 25



class Ping_Pong(Game):
    def __init__(self):
        super().__init__(Ping_Pong_engine(), width = 1000, height = 650, name = "Ping Pong💀")

    def start(self):
        self.engine.TEST()
        super().start()



        # ########
        # while self.running:
        #     super().events()
        #     # self.key_events()
        #     self.game_cycle()


    # def draw(self, obj):
    #     self.UI.screen.blit(obj,[1, 1])

    def game_cycle(self):
        self.UI_pg.fill((24, 59, 100))
        # self.UI_pg.TEST()

        # self.UI_pg.draw(self.engine.update())
        # self.customizer.tick(self.FPS)
        # self.UI_pg.tick()
        # self.events()
        # self.customizer.key_events()
        # super().game_cycle()

import sys
sys.path.insert(0, "PING_PONG")
sys.path.insert(0, "GAME")

from GAME import *
from GAME_ENGINE import *
from PING_PONG_ENGINE import *
from PING_PONG import *


game = Ping_Pong()
game.start()

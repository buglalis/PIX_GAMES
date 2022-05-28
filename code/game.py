import subprocess, sys, enum
from termcolor import colored, cprint
import pygame, pygame_widgets, pygame_menu
from pygame_widgets.button import Button


class PIX_GAME:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def start(self):
        subprocess.Popen(['python3', self.path])

    def get_name(self):
        return self.name

class GAMES(enum.Enum):
    PING_PONG = PIX_GAME("PING_PONG", "./PING_PONG/P_start.py")
    Squirrels = PIX_GAME("Squirrels", "./Squirrels/squirrel.py")

#############################################################################
logo =  "██████╗░██╗██╗░░██╗  ░██████╗░░█████╗░███╗░░░███╗███████╗░██████╗\n"\
        "██╔══██╗██║╚██╗██╔╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝██╔════╝\n"\
        "██████╔╝██║░╚███╔╝░  ██║░░██╗░███████║██╔████╔██║█████╗░░╚█████╗░\n"\
        "██╔═══╝░██║░██╔██╗░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░░╚═══██╗\n"\
        "██║░░░░░██║██╔╝╚██╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗██████╔╝\n"\
        "╚═╝░░░░░╚═╝╚═╝░░╚═╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═════╝░"
#############################################################################
cprint(colored(logo, 'yellow'))

pygame.init()
pygame.display.set_caption('PIX GAMES')
surface = pygame.display.set_mode((500, 400))

menu = pygame_menu.Menu('PIX GAMES', 500, 400, theme=pygame_menu.themes.THEME_SOLARIZED)
for game in GAMES:
    menu.add.button(game.value.name, game.value.start)

menu.mainloop(surface)

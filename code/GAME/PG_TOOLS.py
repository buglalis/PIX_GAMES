import pgzero, pgzrun, pygame
import math, sys, random
import enum
from PIL import Image

class PG_tools:
    def __init__(self):
        pass


    # CONSTANTS
    class KEY(enum.Enum):
        Z = pygame.K_z
        A = pygame.K_a
        M = pygame.K_m
        K = pygame.K_k

    class EVENTS(enum.Enum):
        QUIT = pygame.QUIT


    # SETTING FUNCTIONS
    def set_caption(self, text):
        pygame.display.set_caption(text)

    # EVENT FUNCTIONS
    def start(self):
        pygame.init()

    def get_pressed(self):
        return pygame.key.get_pressed()

    def get_events(self):
        return pygame.event.get()

    # DRAWING FUNCTIONS
    def draw(self, objects):
        for obj in objects:
            obj.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.FPS)

    def events(self, *args):
        for event in self.CTRL.get_events():
            if event.type == self.CTRL.EVENTS.QUIT.value:
                self.running = False
            for fnk in args:
                fnk()

    def key_events(self):
            keys = self.get_pressed()




    # def set_caption(self, text):
    #     pygame.display.set_caption(text)
    #
    # # EVENT FUNCTIONS
    # def start(self):
    #     pygame.init()
    #
    # def get_pressed(self):
    #     return pygame.key.get_pressed()
    #
    # def get_events(self):
    #     return pygame.event.get()

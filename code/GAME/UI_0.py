import pgzero, pgzrun, pygame
import math, sys, random
import enum
from PIL import Image

# /////////////////////////////////////////////// #
class UI_Pygame:
    class KEY(enum.Enum):
        Z = pygame.K_z
        A = pygame.K_a
        M = pygame.K_m
        K = pygame.K_k

    class EVENTS(enum.Enum):
        QUIT = pygame.QUIT
        
    def __init__(self, width, height, FPS):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = FPS

    def tick(self):
        self.clock.tick(self.FPS)

    def get_events(self):
        return pygame.event.get()

    # DRAWING FUNCTIONS
    def draw(self, objects):
        for obj in objects:
            obj.draw(self.screen)
        pygame.display.flip()
        # self.TEST(self.screen)

    def fill(self, color):
        self.screen.fill(color)

    def set_caption(self, text):
        pygame.display.set_caption(text)

    def start(self):
        pygame.init()

    def TEST(self):
        pygame.draw.line(self.screen, ((23, 45, 80)),
               [200, 100],
               [270, 400], 4)

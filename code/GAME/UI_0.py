import pgzero, pgzrun, pygame
import math, sys, random
import enum
from PIL import Image

# /////////////////////////////////////////////// #
class UI_Pygame:
    def __init__(self, width, height, FPS):
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = FPS

    def tick(self):
        self.clock.tick(self.FPS)

    # DRAWING FUNCTIONS
    def draw(self, objects):
        for obj in objects:
            obj.draw(self.screen)
        pygame.display.flip()
        # self.TEST(self.screen)

    def fill(self, color):
        self.screen.fill(color)

    def TEST(self):
        pygame.draw.line(self.screen, ((23, 45, 80)),
               [200, 100],
               [270, 400], 4)

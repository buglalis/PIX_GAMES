import pgzero, pgzrun, pygame
import pygame_widgets
from pygame_widgets.button import Button
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
        # self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
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

    def fill(self, color):
        self.screen.fill(color)

    def set_caption(self, text):
        pygame.display.set_caption(text)

    def start(self):
        pygame.init()

    def text(self, text, font, pos, color = (223, 100, 232), font_size = 72 ):
        font = pygame.font.Font(font, font_size)
        text = font.render(text, True, color)
        self.screen.blit(text, pos)

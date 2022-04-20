import sys
sys.path.insert(0, "PING_PONG")
sys.path.insert(0, "GAME")
from GAME import *
from GAME_ENGINE import *
from PING_PONG_ENGINE import *
from PING_PONG import *



game = Ping_Pong()
game.start()








































# import pygame
# import random
#
# class Square(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super(Square, self).__init__()
#
#         self.win = win
#         self.color = (128, 128, 128)
#         self.speed = 3
#         self.angle = 0
#
#         self.side = random.randint(15, 40)
#
#         self.surface = pygame.Surface((self.side, self.side), pygame.SRCALPHA)
#         self.surface.set_colorkey((200,200,200))
#         self.rect = self.surface.get_rect(center=(x, y))
#
#     def update(self, win):
#         center = self.rect.center
#         self.angle = (self.angle + self.speed) % 360
#         image = pygame.transform.rotate(self.surface , self.angle)
#         self.rect = image.get_rect()
#         self.rect.center = center
#
#         self.rect.y += 1.5
#
#         if self.rect.top >= HEIGHT:
#             self.kill()
#
#         pygame.draw.rect(self.surface, self.color, (0,0, self.side, self.side), 4)
#         win.blit(image, self.rect)
#
# if __name__ == '__main__':
#     pygame.init()
#     SCREEN = WIDTH, HEIGHT = 288, 512
#     win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)
#
#     clock = pygame.time.Clock()
#     FPS = 60
#     count = 0
#
#     square_group = pygame.sprite.Group()
#
#     running = True
#     while running:
#         win.fill((200,200,200))
#
#         for event in pygame.event.get():
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     running = False
#
#         count += 1
#         if count % 100 == 0:
#             x = random.randint(40, WIDTH-40)
#             y = 0
#             square = Square(x, y)
#             square_group.add(square)
#             count = 0
#
#         square_group.update(win)
#
#         pygame.draw.rect(win, (30,30,30), (0, 0, WIDTH, HEIGHT), 8)
#         clock.tick(FPS)
#         pygame.display.update()
# pygame.quit()























# import pygame as py
#
# # define constants
# WIDTH = 500
# HEIGHT = 500
# FPS = 30
#
# # define colors
# BLACK = (255, 255, 255)
# GREEN = (0 , 255 , 0)
#
# # initialize pygame and create screen
# py.init()
# screen = py.display.set_mode((WIDTH , HEIGHT))
# # for setting FPS
# clock = py.time.Clock()
#
# rot = 0
# rot_speed = 0.1
#
# # define a surface (RECTANGLE)
# image_orig = py.Surface((100 , 100))
# # for making transparent background while rotating an image
# image_orig.set_colorkey(BLACK)
# # fill the rectangle / surface with green color
# image_orig.fill(GREEN)
# # creating a copy of orignal image for smooth rotation
# image = image_orig.copy()
# image.set_colorkey(BLACK)
# # define rect for placing the rectangle at the desired position
# rect = image.get_rect()
# rect.center = (WIDTH // 2 , HEIGHT // 2)
# # keep rotating the rectangle until running is set to False
# running = True
# while running:
#     # set FPS
#     clock.tick(FPS)
#     # clear the screen every time before drawing new objects
#     screen.fill(BLACK)
#     # check for the exit
#     for event in py.event.get():
#         if event.type == py.QUIT:
#             running = False
#
#     # making a copy of the old center of the rectangle
#     old_center = rect.center
#     # defining angle of the rotation
#     rot = (rot + rot_speed) % 360
#     # rotating the orignal image
#     new_image = py.transform.rotate(image_orig , rot)
#     rect = new_image.get_rect()
#     rect.center = old_center
#     screen.blit(new_image , rect)
#     py.display.flip()
#
# py.quit()

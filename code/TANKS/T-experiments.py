# import pygame
# import sys  # for us to quit the game
# import math
# import numpy as np
# from PIL import Image
#
# def image_size(filename):
#     im = Image.open(filename)
#     return im.size
#
# class Object(pygame.sprite.Sprite):
#     def __init__(self, filename):
#         super().__init__()
#         self.image = pygame.image.load(filename).convert_alpha()
#         # self.image = pygame.image.load(filename)
#         # self.image.fill((0,0,0))
#
# class Vector:
#     def __init__(self, coordinates):
#         self.x = coordinates[0]
#         self.y = coordinates[1]
#
#     def get_pos(self):
#         return [self.x, self.y]
#
#     def __add__(self, vec):
#         x = self.x + vec.x
#         y = self.y + vec.y
#         return Vector([x,y])
#
#     def __sub__(self, vec):
#         x = self.x - vec.x
#         y = self.y - vec.y
#         return Vector([x, y])
#
#     def rotate(self, angle):
#         angle = (angle/180) * np.pi
#         Matrix = np.array([[np.cos(angle), -np.sin(angle)],
#                            [np.sin(angle),  np.cos(angle)]])
#         self.x, self.y =  list(  np.dot( Matrix, list(np.array([[self.x], [self.y]])) )  )
#
#     def set_angle(self, angle):
#         self.rotate(angle - self.angle)
#
#     def distance(self, vec):
#         return ((self.x - vec.x)**2 + (self.y - vec.y)**2)**(0.5)
#
#     def distance_to_line(self, A, B):
#         C = (A.x* (B.y - A.y) + A.y*(B.x - A.x))
#         vec = Vector([B.x - A.x, B.y - A.y])
#         # vec = B - A
#         vec = vec.normal()
#         if vec.len()!= 0:
#             return abs((A.y - B.y) * self.x + (B.x - A.x) * self.y + C )/vec.len()
#         return -1
#
#     def len(self):
#         return (self.x**2 + self.y**2)**(0.5)
#
#     def scalar(self, vec):
#         return self.x * vec.x + self.y * vec.y
#
#     def scale(self, k):
#         if k != 0:
#             self.x *= k
#             self.y *= k
#         return self
#
#     def normal(self):
#         return Vector([self.y, -self.x])
#
#     def reverse(self):
#         return self.scale(-1)
#
#     def reb(self):
#         self.y = -1
#
#     def rebound(self, vec):
#         if self.scalar(vec) != 0:
#             p = vec.scale( vec.scalar(self)/(vec.len()**2))
#             n = Vector([self.x - p.x, self.y - p.y])
#             self -= n.scale(2)
#         else:
#             self = self.reverse()
#
# class Figure(Object):
#     def __init__(self, point, points, filename, draw_point = [0,0], angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
#         super().__init__(filename)
#         self.center  = Vector(point)
#         self.points  = points
#         self.angle   = angle
#         self.speed   = Vector( (vx, vy) )
#         self.accel   = Vector( (ax, ay))
#         self.ang_vel = angular_velocity
#         self.draw_point = Vector(draw_point)
#         # if self.points != None:
#         #      self.effective_diameter = max([self.center.distance(x) for x in self.points])
#
#     def rotate(self, angle):
#         #self.angle += angle
#         angle = (angle*np.pi/180)  # 1 degree is 0.0175 rad
#
#         for point in self.points:
#             point.x, point.y = (self.center.x + math.cos(angle)*(point.x - self.center.x) + math.sin(angle)*(point.y - self.center.y),
#                                 self.center.y - math.sin(angle)*(point.x - self.center.x) + math.cos(angle)*(point.y - self.center.y))
#         self.angle += angle
#     def set_angle(self, angle):
#         angle = angle % 360
#         self.rotate(angle-self.angle)
#         #self.angle = angle
#
#
#     def move(self, pointer):
#         for point in self.points:
#             point +=  pointer
#             # print(point.get_pos(),end = '****')
#             # point = Vector([99,8])
#         self.center += pointer
#         # print("center:",self.center.get_pos())
#
#     def shift_to_vector(self, vector):
#         self.center += Vector(vector)
#         for point in self.points: point +=  Vector(vector)
#
#     def set_image_size(self):
#         self.len_1, self.len_2 = image_size(self.filename)
#
#     def set_draw_point(self, point):
#         self.draw_point = Vector(point)
#
#     def update(self):
#         # self.speed += self.accel
#         # if self.points != None:
#         #     for point in self.points:
#         #         self.rotate(self.ang_vel)
#         #         point += self.speed
#         # self.angle = (self.angle + self.ang_vel)
#         # self.center += self.speed
#
#         self.speed += self.accel
#         if self.points != None:
#             for point in self.points:
#                 self.rotate(self.ang_vel)
#                 point += self.speed
#         self.angle += self.ang_vel
#         self.center += self.speed
#
#
#     def draw(self, screen, point, angle):
#         rotate_image = pygame.transform.rotate(self.image, self.angle )
#         rotate_image.set_colorkey((255, 255, 255))
#         screen.blit(rotate_image, (point[0] - int(rotate_image.get_width() / 2), point[1] - int(rotate_image.get_height() / 2)))
#
#     def perimeter(self):
#         L = 0
#         for i in range(-1, len(self.points)-1):
#             L += Vector([self.points[i].x - self.points[i+1].x, self.points[i].y - self.points[i+1].y]).len()
#         return L
#
#
# class Rect(Figure):
#     def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
#         super().__init__(point, self.set_rect_points(point, filename), filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)
#         self.rotate(angle)
#         # self.rotate(angle)
#         self.set_radius(filename)
#
#     def set_radius(self, filename):
#         w, h = list(image_size(filename))
#         self.effective_diameter = ((w/2)**2 + (h/2)**2)**(0.5)
#
#     def set_rect_points(self, center, filename):
#         cx, cy = center
#         w, h = list(image_size(filename))
#         # points = [  Vector([center[0] + height/2*i, center[1] + width/2*j]) for i in [-1, 1] for j in [-1, 1]  ]
#         points = [ Vector(position) for position in [
#                                     [cx - w/2, cy - h/2],
#                                     [cx + w/2, cy - h/2],
#                                     [cx + w/2, cy + h/2],
#                                     [cx - w/2, cy + h/2] ] ]
#         return points
#
#     def get_draw_point(self):
#         return self.center.get_pos()
#
#     def draw(self, screen):
#         super().draw(screen, self.get_draw_point(), self.angle)
#         pygame.draw.aalines(screen, (255,255,255), True,  [x.get_pos() for x in self.points])
#         pygame.draw.circle(screen, (255,255,255), (self.center.get_pos()), 5)
#
# class Game:
#     def __init__(self, width = 360, height = 480, name = "tanks", FPS = 60):
#         self.objects = []
#         self.name = name
#         self.screen = pygame.display.set_mode((width, height))
#         self.clock = pygame.time.Clock()
#         self.FPS = FPS
#         self.running = True
#
#     def push_back(self, obj):
#         self.objects.append(obj)
#
#     def game_cycle(self, *args):
#         self.screen.fill((0, 255, 255))
#         self.clock.tick(self.FPS)
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.running = False
#         for obj in self.objects:
#             obj.update()
#         for obj in self.objects:
#             obj.draw(self.screen)
#         pygame.display.flip()
#
#     def start(self):
#         pygame.init()
#         pygame.mixer.init()
#         pygame.display.set_caption(self.name)
#         while self.running:
#             self.game_cycle()
#         pygame.quit()
#         sys.exit()
#
# # class Point:
# #     def __init__(self,x,y):
# #         self.x=x
# #         self.y=y
# #
# #     def get(self):
# #         return (self.x, self.y)
# #     def get_center(self,width,height):
# #         return (self.x-width//2,self.y-height//2)
# #
# #     # add overload for convenient point+vector operations
# #     def __add__(self, vector):
# #         x=self.x+vector.x
# #         y=self.y+vector.y
# #         return Point(x, y)
#
#
#
#
# class Tank:
#     def __init__(self, pos, picture):
#         pygame.sprite.Sprite.__init__(self)
#         self.SPEED = 1
#         self.pos = pos
#         # self.image = pygame.image.load(picture).convert_alpha()
#         # self.image0 = pygame.image.load(picture).convert_alpha()
#         self.rect = Rect(pos, picture)
#
#     def draw(self, screen):
#         #self.image.fill((0, 0, 0))
#         self.rect.draw(screen)
#         #screen.blit(self.image, self.pos.get())
#
#     def update(self):
#         # a dict with required moves(they're vectors) to be used conveniently
#         key = pygame.key.get_pressed()
#         dir_ = {key[pygame.K_w]: (Vector([0, -1]),0),
#                 key[pygame.K_s]: (Vector([0, 1]),180),
#                 key[pygame.K_a]: (Vector([-1, 0]),90),
#                 key[pygame.K_d]: (Vector([1, 0]),-90),
#                 key[pygame.K_w] and key[pygame.K_a]: (Vector([-0.5 ** 0.5, -0.5 ** 0.5]),45),
#                 key[pygame.K_w] and key[pygame.K_d]: (Vector([0.5 ** 0.5, -0.5 ** 0.5]),-45),
#                 key[pygame.K_s] and key[pygame.K_a]: (Vector([-0.5 ** 0.5, 0.5 ** 0.5]),135),
#                 key[pygame.K_s] and key[pygame.K_d]: (Vector([0.5 ** 0.5, 0.5 ** 0.5]),-135)}
#
#     #move() в точку
#
#         for pressed_butts in dir_.keys():
#             if pressed_butts:
#                 self.rect.move(dir_[pressed_butts][0])
#                 self.rect.set_angle(dir_[pressed_butts][1])
#                 # return
#
#
#
# # class Key:
# #     key = pygame.key.get_pressed()
# #     dir_ = {key[pygame.K_w]: (Point(0, -1), 0),
# #             key[pygame.K_s]: (Point(0, 1), 180),
# #             key[pygame.K_a]: (Point(-1, 0), 90),
# #             key[pygame.K_d]: (Point(1, 0), -90),
# #             key[pygame.K_w] and key[pygame.K_a]: (Point(-0.5 ** 0.5, -0.5 ** 0.5), 45),
# #             key[pygame.K_w] and key[pygame.K_d]: (Point(0.5 ** 0.5, -0.5 ** 0.5), -45),
# #             key[pygame.K_s] and key[pygame.K_a]: (Point(-0.5 ** 0.5, 0.5 ** 0.5), 135),
# #             key[pygame.K_s] and key[pygame.K_d]: (Point(0.5 ** 0.5, 0.5 ** 0.5), -135)}
# #
# #     # move() в точку
# #
# #     for pressed_butts in dir_.keys():
# #         if pressed_butts:
# #             self.pos += dir_[pressed_butts][0]
# #             self.rotate(dir_[pressed_butts][1])
#
#
#
# t = Game()
# a = Tank((20,20), "player00.png")
# t.push_back(a)
# t.start()
# # screen = pygame.display.set_mode((20,20))
# # pygame.init()
# # pygame.mixer.init()
# # pygame.display.set_caption("self")
# # p = Rect([0,0],"exp20.png", angle =10)
# # print(p.angle)
# # p.rotate(10)
# # print(p.angle)

import numpy as np
import time
from UI_0 import *



# █▀▀ █░█ █▄░█ █▀▀ ▀█▀ █ █▀█ █▄░█ █▀
# █▀░ █▄█ █░▀█ █▄▄ ░█░ █ █▄█ █░▀█ ▄█

def image_size(filename):
    im = Image.open(filename)
    return im.size


# █▄▄ ▄▀█ █▀ █▀▀   █▀▀ █░░ ▄▀█ █▀ █▀ █▀▀ █▀
# █▄█ █▀█ ▄█ ██▄   █▄▄ █▄▄ █▀█ ▄█ ▄█ ██▄ ▄█

class Game_engine():
    def __init__(self):
        self.version = 2


class Vector:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_pos(self):
        return [self.x, self.y]

    def __add__(self, vec):
        self.x += vec.x
        self.y += vec.y
        return self

    def __sub__(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        return self

    def rotate(self, angle):
        angle = (angle/180) * np.pi
        Matrix = np.array([[np.cos(angle), -np.sin(angle)],
                           [np.sin(angle),  np.cos(angle)]])
        self.x, self.y =  list(  np.dot( Matrix, list(np.array([[self.x], [self.y]])) )  )

    def set_angle(self, angle):
        self.rotate(angle - self.angle)

    def distance(self, vec):
        return ((self.x -vec.x)**2 + (self.y -vec.y)**2)**(0.5)

    def len(self):
        return (self.x**2 + self.y**2)**(0.5)

    def scalar(self, vec):
        return self.x * vec.x + self.y * vec.y

    def scale(self, k):
        if k != 0:
            self.x *= k
            self.y *= k
        return self

    def normal(self):
        return Vector([self.y, -self.x])

    def reverse(self):
        self = self.scale(-1)

    def reb(self):
        self.y = -1

    def rebound(self, vec):
        if self.scalar(vec) != 0:
            # p = vec.scale( vec.scalar(self)/(vec.len()**2))
            # n = self - p
            # self -= n.scale(2)
            # self += Vector( [0.1, -0.1])

            #################################
            p = vec.scale( vec.scalar(self)/(vec.len()**2))
            n = Vector([self.x - p.x, self.y - p.y])
            # t = Vector([n.x*2, n.y*2])
            self -= n.scale(2)
        else:
            self.reverse()

class Object(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        # self.image = pygame.image.load(filename)
        # self.image.fill((0,0,0))


class Figure(Object):
    def __init__(self, point, points, filename, draw_point = [0,0], angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(filename)
        self.center  = Vector(point)
        self.points  = points
        self.angle   = angle
        self.speed   = Vector( (vx, vy) )
        self.accel   = Vector( (ax, ay))
        self.ang_vel = angular_velocity
        self.draw_point = Vector(draw_point)
        if self.points != None:
             self.effective_diameter = max([self.center.distance(x) for x in self.points])

    def rotate(self, angle):
        angle = ((angle/360) * np.pi/2)
        # angle = ((angle/180) * np.pi)

        for point in self.points:
            point.x, point.y = (self.center.x + math.cos(angle)*(point.x - self.center.x) + math.sin(angle)*(point.y - self.center.y),
                                self.center.y - math.sin(angle)*(point.x - self.center.x) + math.cos(angle)*(point.y - self.center.y))

    def set_angle(self, angle):
        angle = angle % 360
        self.rotate(-self.angle)
        self.rotate(angle)

    def move(self, point):
        for point in self.points: point +=  Vector(point) - self.center
        self.center = point

    def shift_to_vector(self, vector):
        self.center += Vector(vector)
        for point in self.points: point +=  Vector(vector)

    def set_image_size(self):
        self.len_1, self.len_2 = image_size(self.filename)

    def set_draw_point(self, point):
        self.draw_point = Vector(point)

    def update(self):
        # self.speed += self.accel
        # if self.points != None:
        #     for point in self.points:
        #         self.rotate(self.ang_vel)
        #         point += self.speed
        # self.angle = (self.angle + self.ang_vel)
        # self.center += self.speed

        self.speed += self.accel
        if self.points != None:
            for point in self.points:
                self.rotate(self.ang_vel)
                point += self.speed
        self.angle += self.ang_vel
        self.center += self.speed


    def draw(self, screen, point, angle):
        rotate_image = pygame.transform.rotate(self.image, self.angle )
        rotate_image.set_colorkey((255, 255, 255))
        screen.blit(rotate_image, (point[0] - int(rotate_image.get_width() / 2), point[1] - int(rotate_image.get_height() / 2)))


    class Player:
        def __init__(self, name = ""):
            pass

        def add_to_control(self):
            pass

        def key_events(self):
            return


# █▀ █▀█ █▀▀ █▀▀ █ ▄▀█ █░░   █▀▀ █░░ ▄▀█ █▀ █▀ █▀▀ █▀
# ▄█ █▀▀ ██▄ █▄▄ █ █▀█ █▄▄   █▄▄ █▄▄ █▀█ ▄█ ▄█ ██▄ ▄█

class Rect(Figure):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, self.set_rect_points(point, filename), filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)
        self.rotate(angle*4)
        # self.rotate(angle)



    def set_rect_points(self, center, filename):
        cx, cy = center
        w, h = list(image_size(filename))
        # points = [  Vector([center[0] + height/2*i, center[1] + width/2*j]) for i in [-1, 1] for j in [-1, 1]  ]
        points = [ Vector(position) for position in [
                                    [cx - w/2, cy - h/2],
                                    [cx + w/2, cy - h/2],
                                    [cx + w/2, cy + h/2],
                                    [cx - w/2, cy + h/2] ] ]
        return points

    def get_draw_point(self):
        return self.center.get_pos()

    def draw(self, screen):
        super().draw(screen, self.get_draw_point(), self.angle)
        pygame.draw.aalines(screen, (255,255,255), True,  [x.get_pos() for x in self.points])
        # pygame.draw.circle(screen, (255,255,255), (self.center.get_pos()), 5)



class Circle(Figure): #  Sell strictly square pictures
    def __init__(self, point, filename, vx = 0, vy = 0, ax = 0, ay = 0, angle = 0, angular_velocity = 0):
        Figure.__init__(self, point, None, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)
        self.radius = self.set_circle_radius(filename)

    def set_circle_radius(self, filename):
        return image_size(filename)[0]/2

    def draw(self, screen):
        super().draw(screen, self.get_draw_point(), self.angle)
        pygame.draw.circle(screen, (255,255,255), (self.center.get_pos()), self.radius)

    def get_draw_point(self):
        # return self.center.x - self.radius, self.center.y - self.radius
        return self.center.x, self.center.y



###################################################

class Polygon:
    pass


class Counter:
    def __init__(self):
        self.count = 0

    def count(self, value = 1):
        self.count += value

    def reset(self, value = 0):
        self.count = value



# def rotate(self, angle):
#     angle = (angle/180) * np.pi
#     Matrix = np.array([[np.cos(angle), -np.sin(angle)],
#     [np.sin(angle),  np.cos(angle)]])
#     self.x, self.y =  list(  np.dot( Matrix, list(np.array([[self.x], [self.y]])) )  )
#

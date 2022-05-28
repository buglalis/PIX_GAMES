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

    def pause(self, t):
        time.sleep(t)

    # ANY AUXILIARY FUNCTIONS
    def point_inside_rect(self, P, rect_points):
        A,B,C,D = [x for x in rect_points]
        def f(P, A, B):
            return (B.x - A.x) * (P.y - A.y) - (B.y - A.y) * (P.x - A.x)

        p1 = f(P, A, B)
        p2 = f(P, B, C)
        p3 = f(P, C, D)
        p4 = f(P, D, A)

        return ((p1 <= 0 and p2 <= 0 and p3 <= 0 and p4 <= 0) or (p1 >= 0 and p2 >= 0 and p3 >= 0 and p4 >= 0))

    def point_inside_circle(self, point, center, radius):
        return (center.x - point.x)**2 + (center.y - point.y)**2 <= radius**2

    def line_segment_intersect(self, p_1, p_2, center, vec):
        def check(matrix_A, matrix_B, C):
            return (np.dot(matrix_A, matrix_B) + C) > 0

        D = center + vec
        C = (center.x * (D.y - center.y) - center.y * (D.x - center.x))
        A = np.array([vec.normal().get_pos()])
        # print(p_1.get_pos())
        B1 = np.array(p_1.get_pos())
        B2 = np.array(p_2.get_pos())
        if check(A, B1, -C) != check(A, B2, -C):
            return True
        return False

    def insert_two_lines(self, A, B, C, D):
        n1 = (A - B).normal()
        n2 = (C - D).normal()
        C1 = (A.x* (B.y - A.y) - A.y*(B.x - A.x))
        C2 = (C.x* (D.y - C.y) - C.y*(D.x - C.x))

        # print([n1.x, n1.y],[n2.x, n2.y])
        # print(n1.y)
        M = np.array([[n1.x, n1.y],[n2.x, n2.y]])
        # M = np.array([[1,5],[4,9
        K = np.array([-C1,-C2])
        return np.linalg.solve(M, K)

    def insert_two_lines_check(self, A, B, C, D):
        return ((A - B).scalar( (C - D).normal())) != 0

    def line_normal(self, A, B):
        return (A - B).normal()



class Vector:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_pos(self):
        return [self.x, self.y]

    def __add__(self, vec):
        x = self.x + vec.x
        y = self.y + vec.y
        return Vector([x, y])

    def __iadd__(self, vec):
        self.x += vec.x
        self.y += vec.y
        return self

    def __sub__(self, vec):
        x = self.x - vec.x
        y = self.y - vec.y
        return Vector([x, y])

    def __isub__(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        return self

    def rotate(self, angle):
        angle = (angle/180) * np.pi
        self.x, self.y = x, y = (math.cos(angle)*self.x + math.sin(angle)*self.y,
                            -math.sin(angle)*self.x + math.cos(angle)*self.y)

    def rotate_ng(self, angle):
        angle = (angle/180) * np.pi
        x, y = (math.cos(angle)*self.x + math.sin(angle)*self.y,
                            -math.sin(angle)*self.x + math.cos(angle)*self.y)
        return Vector([x,y])

    def set_angle(self, angle):
        self.rotate(angle - self.angle)

    def distance(self, vec):
        return ((self.x - vec.x)**2 + (self.y - vec.y)**2)**(0.5)

    def distance_to_line(self, A, B):
        C = (A.x* (B.y - A.y) + A.y*(B.x - A.x))
        vec = B - A
        vec = vec.normal()
        if vec.len()!= 0:
            return abs((A.y - B.y) * self.x + (B.x - A.x) * self.y + C )/vec.len()
        return -1

    def reflect(self, A, B):
        vec = B - A
        a   = self - A
        if a.scalar(vec) != 0:
            p = vec.scale_ng( vec.scalar(a)/(vec.len()**2))
            n = p - a
            self += n.scale_ng(2)
        # else:
        #     self.reverse()

    def len(self):
        return (self.x**2 + self.y**2)**(0.5)

    def scalar(self, vec):
        return self.x * vec.x + self.y * vec.y

    def scale(self, k):
        if k != 0:
            self.x *= k
            self.y *= k

    def scale_ng(self, k):
        if k != 0:
            return Vector((self.x * k, self.y * k))
        return Vector(self.get_pos())

    def normal(self):
        return Vector([self.y, -self.x])

    def reverse(self):
        self.scale(-1)

    def reverse_ng(self):
        return self.scale_ng(-1)


    def rebound(self, vec):
        if self.scalar(vec) != 0:
            p = vec.scale_ng( vec.scalar(self)/(vec.len()**2))
            n = self - p
            self -= n.scale_ng(2)
        else:
            self.reverse()

    def rebound_ng(self, vec):
        if self.scalar(vec) != 0:
            p = vec.scale_ng( vec.scalar(self)/(vec.len()**2))
            n = self - p
            ans = self - n.scale_ng(2)
        else:
            ans = self.reverse_ng()

    def rebound_special(self, A, B, P, angle = 45):
        vec = B - A
        if self.scalar(vec) != 0:
            p = vec.scale_ng( vec.scalar(self)/(vec.len()**2))
            n = self - p
            self -= n.scale_ng(2)
        else:
            self.reverse()
        self.rotate(self.proection_special( A, B, P) * angle)

    def proection_special(self, A, B, P):
        vec = B - A
        a   = P - A
        p = vec.scale_ng( vec.scalar(a)/(vec.len()**2))
        n = p - a
        M = P + n
        ############
        if A.distance(M) <= B.distance(M):
            return (p.len()%(vec.len()/2))/(vec.len()/2)
        else:
            return -(p.len()%(vec.len()/2))/(vec.len()/2)

    def see_angle(self, point): # Это функция возвращает угол под которым видно точку относительно нашей
        if (point.x != self.x) and (point.y != self.y):
            return np.arctan( (point.y - self.y)/(point.x - self.x) )
        if point.x == self.x:
            return -np.pi/2 if (point.y - self.y) > 0 else np.pi/2
        elif point.y == self.y:
            return 0 if (point.x - self.x) < 0 else np.pi

    def get_angle(self):
        if (self.y != 0) and (self.x != 0):
            return np.arctan(self.y/self.x)
        if self.y == 0:
            return 0 if self.x > 0 else np.pi
        if self.x == 0:
            return -np.pi/2 if self.y > 0 else np.pi/2


class Object(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.image = pygame.image.load(filename).convert_alpha()
        # self.image = pygame.image.load(filename)
        # self.image.fill((0,0,0))


class Figure(Object):
    def __init__(self, point, points, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(filename)
        self.center  = Vector(point)
        self.points  = points
        self.angle   = angle
        self.speed   = Vector( (vx, vy) )
        self.accel   = Vector( (ax, ay))
        self.ang_vel = angular_velocity
        # self.draw_point = Vector(draw_point)
        if self.points != None:
             self.effective_diameter = max([self.center.distance(x) for x in self.points])

    def rotate(self, angle):
        angle = ((angle/180) * np.pi)
        # angle = ((angle/180) * np.pi)

        for point in self.points:
            point.x, point.y = (self.center.x + math.cos(angle)*(point.x - self.center.x) + math.sin(angle)*(point.y - self.center.y),
                                self.center.y - math.sin(angle)*(point.x - self.center.x) + math.cos(angle)*(point.y - self.center.y))

    def set_angle(self, angle):
        angle = angle % 360
        self.rotate(angle - self.angle)

    def move(self, vec):
        self.points = [point + vec for point in self.points]
        self.center += vec

    def move_to(self, point):
        vec = point - self.center
        # self.move(vec)
        self.points = [point + vec for point in self.points]
        self.center += vec

    def shift_to_vector(self, vector):
        self.center += Vector(vector)
        for point in self.points: point +=  Vector(vector)

    def set_image_size(self):
        self.len_1, self.len_2 = image_size(self.filename)

    def set_draw_point(self, point):
        self.draw_point = Vector(point)

    def update(self):
        # self.speed += self.accel
        self.angle += self.ang_vel
        if self.points != None:
            for point in self.points:
                point += self.speed
            self.rotate(self.ang_vel)
        self.center += self.speed


    def draw(self, screen, point, angle):
        rotate_image = pygame.transform.rotate(self.image, self.angle )
        rotate_image.set_colorkey((255, 255, 255))
        screen.blit(rotate_image, (point[0] - int(rotate_image.get_width() / 2), point[1] - int(rotate_image.get_height() / 2)))

    def perimeter(self):
        L = 0
        for i in range(-1, len(self.points)-1):
            L += Vector([self.points[i].x - self.points[i+1].x, self.points[i].y - self.points[i+1].y]).len()
        return L


# █▀ █▀█ █▀▀ █▀▀ █ ▄▀█ █░░   █▀▀ █░░ ▄▀█ █▀ █▀ █▀▀ █▀
# ▄█ █▀▀ ██▄ █▄▄ █ █▀█ █▄▄   █▄▄ █▄▄ █▀█ ▄█ ▄█ ██▄ ▄█

class Rect(Figure):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, self.set_rect_points(point, filename), filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)
        self.rotate(angle)
        self.set_radius(filename)

    def set_radius(self, filename):
        w, h = list(image_size(filename))
        self.effective_diameter = ((w/2)**2 + (h/2)**2)**(0.5)

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


class Circle(Figure): #  Sell strictly square pictures
    def __init__(self, point, filename, vx = 0, vy = 0, ax = 0, ay = 0, angle = 0, angular_velocity = 0):
        Figure.__init__(self, point, None, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)
        self.radius = self.set_circle_radius(filename)

    def set_circle_radius(self, filename):
        return image_size(filename)[0]/2

    def draw(self, screen):
        super().draw(screen, self.get_draw_point(), self.angle)
        # pygame.draw.circle(screen, (255,255,255), (self.center.get_pos()), self.radius)
        a = (self.speed.scale_ng(5) + self.center).get_pos()

    def get_draw_point(self):
        # return self.center.x - self.radius, self.center.y - self.radius
        return self.center.x, self.center.y

###################################################

class Polygon:
    pass


class Counter:
    def __init__(self):
        self.num = 0

    def count(self, value = 1):
        self.num += value

    def reset(self, value = 0):
        self.num = value


class Player:
    def __init__(self, name = ""):
        pass

    def add_to_control(self):
        pass

    def key_events(self):
        return

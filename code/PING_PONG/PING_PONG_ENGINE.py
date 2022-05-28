from GAME_ENGINE import *
from random import randint
sys.path.insert(1, "PING_PONG/images")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def pos(self):
        return (self.x, self.y)

class status(enum.Enum):
    START       = enum.auto()
    MENU        = enum.auto()
    GAME        = enum.auto()
    START_GAME  = enum.auto()
    ROUND_L     = enum.auto()
    ROUND_R     = enum.auto()
    GAME_OVER   = enum.auto()
    PAUSE_FL    = enum.auto()
    TEST        = enum.auto()

class EVENTS(enum.Enum):
    GOAL_L = pygame.USEREVENT + 1
    GOAL_R = pygame.USEREVENT + 2
    FINAL  = pygame.USEREVENT + 3

class FONTS(enum.Enum):
    BIG_FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'

class COLORS(enum.Enum):
    MENU_COLOR           = (24, 13, 100)
    TEXT_GAME_OVER_COLOR = (234, 100, 0)

class PARAMS(enum.Enum):
    PLAYER_SPEED = 5
    BALL_SPEED   = 9
    GATE_WIDTH   = 25
    # WINDOW_WIDTH = 1920
    # WINDOW_HEIGHT = 1080
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 650
    MAX_GOALS = 10

    BUTTON_W = 300
    BUTTON_H = 150

class KEYS(enum.Enum):
    W    = pygame.K_w
    S    = pygame.K_s
    UP   = pygame.K_UP
    DOWN = pygame.K_DOWN

class IMAGES(enum.Enum):
    BALL   = "PING_PONG/images/ball_2.png"
    WALL_W = "PING_PONG/images/wall_w.png"
    # GUEST =

class POS(enum.Enum): # POSITIONS
    BUTTON_POS     = Point(PARAMS.WINDOW_WIDTH.value/2 - PARAMS.BUTTON_W.value/2, PARAMS.WINDOW_HEIGHT.value/2 - PARAMS.BUTTON_H.value/2)
    TEXT_GAME_OVER = Point(PARAMS.WINDOW_WIDTH.value/4,  PARAMS.WINDOW_HEIGHT.value/2)


# ENGINE
class Ping_Pong_engine(Game_engine):
    def __init__(self):
        self.balls   = []
        self.walls   = []
        self.players = []
        self.rounds_counter = 0

    def add(self, array, *objects):
        for obj in objects: array.append(obj)

    def clear(self):
        self.balls = []
        self.walls = []
        self.players = []

    def check_final(self):
        if self.rounds_counter == PARAMS.MAX_GOALS.value:
            self.game_final()
            self.rounds_counter = 0

    # def update(self):
    #     all_obj = []
    #     wall_obj = []
    #     for p in self.players:
    #         p.update()
    #         wall_obj.append(p.requet)
    #
    #     for ball in self.balls:
    #         for wall in self.walls + wall_obj:
    #             self.collision_final(ball, wall)
    #         for p in self.players:
    #             p.guest.update(ball.center)
    #     # all_obj += self.walls + self.balls
    #     all_obj += self.walls + wall_obj + self.balls
    #     for obj in all_obj:
    #         obj.update()
    #
    #     for p in self.players: all_obj.append(p.guest)
    #     # return all_obj
    #     if self.players: self.rounds_counter = max([player.counter.get_num() for player in self.players])
    #     return self.players + self.walls + self.balls

    def update(self): # Старая
        all_obj = []
        wall_obj = []
        for p in self.players:
            p.update()
            wall_obj.append(p.requet)

        for ball in self.balls:
            for wall in self.walls + wall_obj:
                self.collision_final(ball, wall)
            for p in self.players:
                p.guest.update(ball.center)
        # all_obj += self.walls + self.balls
        all_obj += self.walls + wall_obj + self.balls
        for obj in all_obj:
            obj.update()

        for p in self.players: all_obj.append(p.guest)
        # return all_obj
        if self.players: self.rounds_counter = max([player.counter.get_num() for player in self.players])
        return self.players + self.walls + self.balls



    # █▀▀ █▀▀█ █░░ █░░ ░▀░ █▀▀ ░▀░ █▀▀█ █▀▀▄
    # █░░ █░░█ █░░ █░░ ▀█▀ ▀▀█ ▀█▀ █░░█ █░░█
    # ▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀░░▀
    def collision_0(self, ball, wall):
        if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return
        else:
            rebound_wall = [Vector((0,0)), Vector((0,0))]
            mn_len = float("inf")
            insert_point_mn = Vector((0,0))
            for i in range(-1, 3):
                if self.line_segment_intersect(wall.points[i], wall.points[i+1], ball.center, ball.speed):
                    if self.insert_two_lines_check(wall.points[i], wall.points[i+1], ball.center, ball.center + ball.speed):
                        insert_point = Vector(self.insert_two_lines(wall.points[i], wall.points[i+1], ball.center, ball.center + ball.speed))
                        if ball.center.distance(insert_point) < mn_len:
                            rebound_wall = wall.points[i] - wall.points[i+1]
                            mn_len = ball.center.distance(insert_point)
                            insert_point_mn = insert_point

            if mn_len != float("inf"):
                if ball.center.distance(insert_point_mn) < ball.speed.len():
                    # ball.center += ball.speed.scale_ng(0.5)
                    ball.speed.rebound(rebound_wall)

                else:
                    for i in range(-1, 3):
                            vec = wall.points[i] - wall.points[i+1]
                            C = (wall.points[i].x* (wall.points[i+1].y - wall.points[i].y) - wall.points[i].y*(wall.points[i+1].x - wall.points[i].x))

                            if (abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len() <= ball.radius):
                                nA = vec.normal().scale_ng( abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len()**2)
                                V = nA + ball.center
                                # if (min(wall.points[i].x, wall.points[i+1].x) <= V.x <= max(wall.points[i].x, wall.points[i+1].x)) or (min(wall.points[i].y, wall.points[i+1].y) <= V.y <= max(wall.points[i].y, wall.points[i+1].y)):
                                if (wall.points[i].x <= V.x <= wall.points[i+1].x) or (wall.points[i].y <= V.y < wall.points[i+1].y):
                                    ball.speed.rebound(vec)
                                    return

    ###################################################################################################
    def collision_final(self, obj_1, obj_2):
        if (type(obj_1) is Ball) and (type(obj_2) is Ball):
            self.balls_collision(obj_1, obj_2)
        elif (type(obj_1) is Ball) and (issubclass(type(obj_2), Rect)):
            # self.collision_0(obj_1, obj_2)
            if (type(obj_2) is Requet):
                self.requet_ball_cillision(obj_1, obj_2)
            else: self.ball_wall_collision(obj_1, obj_2)
        elif issubclass(type(obj_2), Rect) and issubclass(type(obj_2), Rect):
            self.wall_wall_collision(obj_1, obj_2)

    def balls_collision(self, ball_1, ball_2):
        if ball_1.center.distance(ball_2.center) > ball_1.radius + ball_2.radius: return

    def requet_ball_cillision(self, ball, wall):

        ################################################### OLD
        # if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return
        # else:
        #     for i in range(-1, 3):                                                                                                      # Проход по всем точка стены
        #         vec = wall.points[i] - wall.points[i+1]
        #         C = (wall.points[i].x* (wall.points[i+1].y - wall.points[i].y) - wall.points[i].y*(wall.points[i+1].x - wall.points[i].x))
        #
        #         if (abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len() <= ball.radius):
        #             nA = vec.normal().scale_ng( abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len()**2)
        #             V = nA + ball.center
        #             if (wall.points[i].x <= V.x <= wall.points[i+1].x) or (wall.points[i].y <= V.y < wall.points[i+1].y):
        #                 ball.speed.rebound_special(wall.points[i], wall.points[i+1], ball.center)
        #                 return
        ###################################################
        if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return
        else:
            rebound_wall = [Vector((0,0)), Vector((0,0))]
            mn_len = float("inf")
            insert_point_mn = Vector((0,0))
            for i in range(-1, 3):
                if self.line_segment_intersect(wall.points[i], wall.points[i+1], ball.center, ball.speed):
                    if self.insert_two_lines_check(wall.points[i], wall.points[i+1], ball.center, ball.center + ball.speed):
                        insert_point = Vector(self.insert_two_lines(wall.points[i], wall.points[i+1], ball.center, ball.center + ball.speed))
                        if ball.center.distance(insert_point) < mn_len:
                            rebound_wall = [wall.points[i], wall.points[i+1]]
                            mn_len = ball.center.distance(insert_point)
                            insert_point_mn = insert_point

            if mn_len != float("inf"):
                if ball.center.distance(insert_point_mn) <= ball.speed.len():
                    # ball.center += ball.speed.scale_ng(0.5)
                    # ball.speed.rebound_special(rebound_wall)
                     ball.speed.rebound_special(rebound_wall[0], rebound_wall[1], ball.center)

                else:
                    for i in range(-1, 3):
                            vec = wall.points[i] - wall.points[i+1]
                            C = (wall.points[i].x* (wall.points[i+1].y - wall.points[i].y) - wall.points[i].y*(wall.points[i+1].x - wall.points[i].x))

                            if (abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len() <= ball.radius):
                                nA = vec.normal().scale_ng( abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len()**2)
                                V = nA + ball.center
                                # if (min(wall.points[i].x, wall.points[i+1].x) <= V.x <= max(wall.points[i].x, wall.points[i+1].x)) or (min(wall.points[i].y, wall.points[i+1].y) <= V.y <= max(wall.points[i].y, wall.points[i+1].y)):
                                if (wall.points[i].x <= V.x <= wall.points[i+1].x) or (wall.points[i].y <= V.y < wall.points[i+1].y):
                                    ball.speed.rebound_special(wall.points[i], wall.points[i+1], ball.center)
                                    # ball.speed.rebound_special(vec)
                                    return

    def ball_wall_collision(self, ball, wall):
        if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return
        else:
            rebound_wall = [Vector((0,0)), Vector((0,0))]
            mn_len = float("inf")
            insert_point_mn = Vector((0,0))
            for i in range(-1, 3):
                if self.line_segment_intersect(wall.points[i], wall.points[i+1], ball.center, ball.speed):
                    if self.insert_two_lines_check(wall.points[i], wall.points[i+1], ball.center, ball.center + ball.speed):
                        insert_point = Vector(self.insert_two_lines(wall.points[i], wall.points[i+1], ball.center, ball.center + ball.speed))
                        if ball.center.distance(insert_point) < mn_len:
                            rebound_wall = wall.points[i] - wall.points[i+1]
                            mn_len = ball.center.distance(insert_point)
                            insert_point_mn = insert_point

            if mn_len != float("inf"):
                if ball.center.distance(insert_point_mn) < ball.speed.len():
                    # ball.center += ball.speed.scale_ng(0.5)
                    ball.speed.rebound(rebound_wall)

                else:
                    for i in range(-1, 3):
                            vec = wall.points[i] - wall.points[i+1]
                            C = (wall.points[i].x* (wall.points[i+1].y - wall.points[i].y) - wall.points[i].y*(wall.points[i+1].x - wall.points[i].x))

                            if (abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len() <= ball.radius):
                                nA = vec.normal().scale_ng( abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len()**2)
                                V = nA + ball.center
                                # if (min(wall.points[i].x, wall.points[i+1].x) <= V.x <= max(wall.points[i].x, wall.points[i+1].x)) or (min(wall.points[i].y, wall.points[i+1].y) <= V.y <= max(wall.points[i].y, wall.points[i+1].y)):
                                if (wall.points[i].x <= V.x <= wall.points[i+1].x) or (wall.points[i].y <= V.y < wall.points[i+1].y):
                                    ball.speed.rebound(vec)
                                    return

    def wall_wall_collision(self, wall_1, wall_2):
        pass

    # ▄▀ ▄▀▄ █▄░█ █▀▄ ▀ ▀█▀ ▀ ▄▀▄ █▄░█ ▄▀▀
    # █░ █░█ █░▀█ █░█ █ ░█░ █ █░█ █░▀█ ░▀▄
    # ░▀ ░▀░ ▀░░▀ ▀▀░ ▀ ░▀░ ▀ ░▀░ ▀░░▀ ▀▀░
    def new_round(self, right = False, left = False):
        for pl in self.players:
            pl.requet.reset()

        self.balls = []
        if right:
            self.add(self.balls, Ball( [500, 325], IMAGES.BALL.value, angular_velocity = 0, vx = PARAMS.BALL_SPEED.value, vy = 0))
        elif left:
            self.add(self.balls, Ball( [500, 325], IMAGES.BALL.value, angular_velocity = 0, vx = -PARAMS.BALL_SPEED.value, vy = 0))

    def game_final(self):
        pygame.event.post(pygame.event.Event(EVENTS.FINAL.value))
        self.pause()

    def pause(self):
        for pl in self.players:
            pl.requet.reset()
            self.balls = []
            pl.counter.reset(value = 0)

    # ▄▀▀░ ▄▀▄ █▄░▄█ █▀▀
    # █░▀▌ █▀█ █░█░█ █▀▀
    # ▀▀▀░ ▀░▀ ▀░░░▀ ▀▀▀
    def GAME(self):
        self.clear()

        guest_l  = Guest([-30, 325], "images/guest.png", EVENTS.GOAL_L.value,  angle = 0)
        guest_r  = Guest([1030, 325], "images/guest.png", EVENTS.GOAL_R.value, angle = 0)

        requet_l = Requet([20, 325], "images/platform.png", 650-100, 5, KEYS.W.value, KEYS.S.value, angle = 90)
        requet_r = Requet([980, 325], "images/platform.png", 650-100, 5, KEYS.DOWN.value, KEYS.UP.value, angle = -90)
        # requet_r = Requet([900, 325], "images/platform.png", 650-100, 5, pygame.K_m, pygame.K_k, angle = -70)

        self.add(self.players,
                 Player_ping_pong( requet_l, guest_l, PP_counter("Player 2", [800,100])),
                 Player_ping_pong( requet_r, guest_r, PP_counter("Player 1",[100,100])))


        self.add(self.walls,
                 Rect_Wall( [500, 5], IMAGES.WALL_W.value, angle = 0),
                 Rect_Wall( [500, 645], IMAGES.WALL_W.value, angle = 0))

        self.add(self.balls,
                 Ball( [500, 325], IMAGES.BALL.value, angular_velocity = 0, vx = -6, vy = 0))

        # self.add(self.walls,
        #          Rect_Wall( [230, 425], "images/walls/wall_1.png", angle = 90, angular_velocity = 2),
        #          # Rect_Wall( [230, 425], "BUR.png", angle = 90, angular_velocity = 2),
        #          Rect_Wall( [803, 460], "images/walls/wall_1.png", angle = 90, angular_velocity = 1))

        # ▀█▀ █▀▀ █▀ ▀█▀ █▀
        # ░█░ ██▄ ▄█ ░█░ ▄█

    def TEST(self):
        self.test_2()

    def test_1(self):
          self.clear()
          self.add(self.walls,
                   Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0.1, angle = 45, vx = -1),
                   Rect_Wall( [450, 500], "images/walls/Sergi.jpg", angular_velocity = 2, angle = 45),


                   Rect_Wall( [500, 5], "images/walls/wall_w.png", angle = 0),
                   Rect_Wall( [520, 645], "images/walls/wall_w.png", angle = 0),
                   Rect_Wall( [5, 325], "images/walls/wall_w.png", angle = 90),
                   Rect_Wall( [995, 325], "images/walls/wall_w.png", angle = 90))
                   # Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0, angle = 45))
                   # Rect_Wall( [600, 230], "images/walls/wall_test.png", angle = 0))
          self.add(self.balls,
                   Ball( [500, 200], "images/walls/ball_test.png", angular_velocity = 0, vx = -4, vy = 0),
                   Ball( [500, 200], "images/ball_small.png", angular_velocity = 0, vx = -4, vy = 8) )

    def test_2(self):
      self.clear()
      self.add(self.walls,
               Rect_Wall( [150, 150], "images/walls/wall_test.png", angular_velocity = 0.5, angle = 30),

               Rect_Wall( [500, 5], "images/walls/wall_w.png", angle = 0),
               Rect_Wall( [500, 300], "images/walls/wall_w.png", angle = 0),
               Rect_Wall( [5, 325], "images/walls/wall_w.png", angle = 90),
               Rect_Wall( [420, 325], "images/walls/wall_w.png", angle = 90))
      speed = -4
      b = "images/ball.png"
      # b = "images/ball_small.png"

      self.add(self.balls,
               Ball( [400, 210], b, angular_velocity = 0, vx = speed, vy = 5),
               Ball( [400, 215], b, angular_velocity = 0, vx = speed, vy = 5),
               Ball( [400, 220], b, angular_velocity = 0, vx = speed, vy = 5),
               Ball( [400, 225], b, angular_velocity = 0, vx = speed, vy = -2),
               # Ball( [400, 230], b, angular_velocity = 0, vx = speed, vy = 8),
               Ball( [400, 235], b, angular_velocity = 0, vx = speed, vy = 4),
               Ball( [400, 240], b, angular_velocity = 0, vx = speed, vy = 1),
               Ball( [400, 245], b, angular_velocity = 0, vx = speed, vy = 8),
               Ball( [400, 250], b, angular_velocity = 0, vx = speed, vy = 0),

               # Ball( [400, 217], b, angular_velocity = 0, vx = speed, vy = 7),
               Ball( [400, 200], b, angular_velocity = 0, vx = speed, vy = -2),
               Ball( [400, 222], b, angular_velocity = 0, vx = speed, vy = -5),
               Ball( [400, 215], b, angular_velocity = 0, vx = speed, vy = 3),

               Ball( [400, 210], b, angular_velocity = 0, vx = speed, vy = -4),
               Ball( [400, 234], b, angular_velocity = 0, vx = speed, vy = 3),
               Ball( [400, 221], b, angular_velocity = 0, vx = speed, vy = 2),
               Ball( [400, 210], b, angular_velocity = 0, vx = speed, vy = 6))

    def test_3(self):
      self.clear()
      self.add(self.walls,
               Rect_Wall( [200, 240], "images/walls/wall_test.png", angular_velocity = 0, angle = -45))


               # Rect_Wall( [500, 5], "images/walls/wall_w.png", angle = 0),
               # Rect_Wall( [500, 645], "images/walls/wall_w.png", angle = 0),
               # Rect_Wall( [5, 325], "images/walls/wall_w.png", angle = 90),
               # Rect_Wall( [995, 325], "images/walls/wall_w.png", angle = 90))
               # Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0, angle = 45))
               # Rect_Wall( [600, 230], "images/walls/wall_test.png", angle = 0))
      self.add(self.balls,
               Ball( [500, 230], "images/ball.png", angular_velocity = 0, vx = -10, vy = 0) )





class Ball(Circle):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)


class Rect_Wall(Rect):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity )


class Requet(Rect_Wall):
    def __init__(self, point, filename, border, player_speed, key_1, key_2, angle = 0):
        super().__init__(point, filename, angle = angle)
        self.border = border
        self.cur_pos = border/2
        self.destination = Vector([1, 0])
        self.pl_speed = player_speed
        self.key_1 = key_1
        self.key_2 = key_2
        self.start_point = Vector(point)

    def move(self, up = 1):
        if up:
            if (self.cur_pos + self.pl_speed <= self.border):
                super().move(self.destination.rotate_ng(self.angle).scale_ng(self.pl_speed))
                self.cur_pos += self.pl_speed
        elif  up == 0:
            if(0 <= self.cur_pos - self.pl_speed ):
                super().move(self.destination.rotate_ng(self.angle + 180).scale_ng(self.pl_speed))
                self.cur_pos -= self.pl_speed

    def reset(self):
        self.move_to(self.start_point)
        self.cur_pos = self.border/2


class Guest(Rect):
    def __init__(self, point, filename, event, angle = 0):
        super().__init__(point, filename, angle = angle)
        self.event = event
        self.flag  = False

    def draw(self, screen):
        pygame.draw.aalines(screen, (255,255,255), True,  [x.get_pos() for x in self.points])

    def check(self, P):
        A = self.points[0]
        B = self.points[1]
        C = self.points[2]
        D = self.points[3]

        def f(P, A, B):
            return (B.x - A.x) * (P.y - A.y) - (B.y - A.y) * (P.x - A.x)

        p1 = f(P, A, B)
        p2 = f(P, B, C)
        p3 = f(P, C, D)
        p4 = f(P, D, A)

        return ((p1 <= 0 and p2 <= 0 and p3 <= 0 and p4 <= 0) or (p1 >= 0 and p2 >= 0 and p3 >= 0 and p4 >= 0))

    def update(self, point):
        if self.check(point):
            pygame.event.post(pygame.event.Event(self.event))
            self.flag = True

    def goal(self):
        if self.flag:
            self.flag = False
            return 1
        return 0

class PP_counter(Counter):
    def __init__(self, name, point):
        super().__init__()
        self.name = name
        self.center = Vector(point)
        self.color = (180, 0, 0)

    def update(self, goal = False, reset = False):
        if goal: self.count()
        if reset: self.reset()

    def draw(self, screen):
        f1 = pygame.font.Font(None, 36)
        text1 = f1.render(f'{self.name} : {self.num}', True,self.color)
        screen.blit(text1, self.center.get_pos())

    def get_num(self):
        return self.num


class Player_ping_pong:
    def __init__(self, requet, guest, counter):
        self.requet  = requet
        self.guest   = guest
        self.counter = counter

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.requet.key_1]:
            self.requet.move(up = 1)
        elif keys[self.requet.key_2]:
            self.requet.move(up = 0)
        goal = self.guest.goal()
        self.counter.update(goal = goal)

    def draw(self, screen):
        self.requet.draw(screen)
        self.counter.draw(screen)

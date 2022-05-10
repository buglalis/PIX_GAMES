from GAME_ENGINE import *

class Ping_Pong_engine(Game_engine):
    def __init__(self):
        # super().__init__()
        self.balls = []
        self.walls = []

    def add(self, array, *objects):
        for obj in objects: array.append(obj)

    def clear(self):
        self.balls = []
        self.walls = []

    def update(self):
        for ball in self.balls:
            for wall in self.walls:
                self.collision_0(ball, wall)

        for obj in (self.walls + self.balls):
            obj.update()

        return self.walls + self.balls

    def collision_0(self, ball, wall):
        if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return                                        # Проверка на возможность столкновения
        for i in range(-1, 3):                                                                                                      # Проход по всем точка стены
            vec = wall.points[i] - wall.points[i+1]
            C = (wall.points[i].x* (wall.points[i+1].y - wall.points[i].y) - wall.points[i].y*(wall.points[i+1].x - wall.points[i].x))

            if (abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len() <= ball.radius):

                nA = Vector([vec.y,-vec.x]).scale_ng( abs(vec.y * ball.center.x - vec.x * ball.center.y + C )/vec.len()**2)
                V = nA + ball.center

                if (wall.points[i].x <= V.x <= wall.points[i+1].x) or (wall.points[i].y <= V.y < wall.points[i+1].y):
                    ball.speed.rebound(vec)
                    return

    def collision_1(self, obj_1, obj_2):
        if (type(obj_1) is Ball) and (type(obj_2) is Ball):
            self.balls_collision(obj_1, obj_2)
        elif (type(obj_1) is Rect_Wall) and (type(obj_2) is Rect_Wall):
            self.walls_collision(obj_1, obj_2)
        elif (type(obj_1) is Ball) and (type(obj_2) is Rect_Wall):
            self.ball_wall_collision_distance(obj_1, obj_2)

    def balls_collision(self, ball_1, ball_2):
        if ball_1.center.distance(ball_2.center) > ball_1.radius + ball_2.radius: return

    def walls_collision(self, wall_1, wall_2):
        if wall_1.center.distance(wall_2.center) > wall_1.effective_diameter + wall_2.effective_diameter: return

    def ball_wall_collision_distance(self, ball, wall):
        # ball.speed = Vector([0,0])
        # print(ball.center.distance_to_line(Vector([0,0]),Vector([1,1])),  ball.center.y)#(ball.center.x**2 + ball.center.y**2)**(0.5) )
        if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return
        dist = float('inf')
        L = 0
        for i in range(-1, len(wall.points)-1):
                dist = ball.center.distance_to_line(wall.points[i+1], wall.points[i])
                print(dist)
                L += dist
                vec = Vector([wall.points[i+1].x - wall.points[i].x, wall.points[i+1].y - wall.points[i].y])
        # print(L)
        if (int(L) <= wall.perimeter()):
            dist = float('inf')
            for i in range(-1, len(wall.points)-1):
                if ball.center.distance_to_line(wall.points[i], wall.points[i+1]) < dist:
                    vec = Vector([wall.points[i+1].x - wall.points[i].x, wall.points[i+1].y - wall.points[i].y])
                    dist = ball.center.distance_to_line(wall.points[i+1], wall.points[i])
            ball.speed.rebound(vec)
        ball.speed.rebound(vec)


    def ball_wall_collision_radius(self, ball, wall):
        pass






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
                 Ball( [400, 230], b, angular_velocity = 0, vx = speed, vy = 8),
                 Ball( [400, 235], b, angular_velocity = 0, vx = speed, vy = 4),
                 Ball( [400, 240], b, angular_velocity = 0, vx = speed, vy = 1),
                 Ball( [400, 245], b, angular_velocity = 0, vx = speed, vy = 8),
                 Ball( [400, 250], b, angular_velocity = 0, vx = speed, vy = 0),

                 Ball( [400, 217], b, angular_velocity = 0, vx = speed, vy = 7),
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
                 Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0, angle = 50))


                 # Rect_Wall( [500, 5], "images/walls/wall_w.png", angle = 0),
                 # Rect_Wall( [500, 645], "images/walls/wall_w.png", angle = 0),
                 # Rect_Wall( [5, 325], "images/walls/wall_w.png", angle = 90),
                 # Rect_Wall( [995, 325], "images/walls/wall_w.png", angle = 90))
                 # Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0, angle = 45))
                 # Rect_Wall( [600, 230], "images/walls/wall_test.png", angle = 0))
        self.add(self.balls,
                 Ball( [500, 230], "images/ball_small.png", angular_velocity = 0, vx = -2, vy = 0) )



class Ball(Circle):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)


class Rect_Wall(Rect):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity )


class Requet(Rect_Wall):
    def __init__(self, max_speed = 0, borders = []):
        self.borders = borders



    # def key_events(self):
    #         if keys[self.UI.KEY.Z]:
    #              self.requet_l.update(int(PLAYER_SPEED))
    #         elif keys[self.UI.KEY.A]:
    #              self.requet_l.update(int(-PLAYER_SPEED))
    #         if keys[self.UI.KEY.M]:
    #              self.requet_r.update(int(PLAYER_SPEED))
    #         elif keys[self.UI.KEY.K]:
    #              self.requet_r.update(int(-PLAYER_SPEED))

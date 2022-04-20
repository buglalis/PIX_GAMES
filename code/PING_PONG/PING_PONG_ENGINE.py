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
            # self.collisin_test(ball)
            for wall in self.walls:
                self.collision(ball, wall)

        for obj in (self.walls + self.balls):
            obj.update()

        return self.walls + self.balls

    def collision(self, ball, wall):
        if ball.center.distance(wall.center) > ball.radius + wall.effective_diameter: return                                        # Проверка на возможность столкновения
        for i in range(-1, 3):                                                                                                      # Проход по всем точка стены
            vec = Vector([wall.points[i].x - wall.points[i+1].x, wall.points[i].y - wall.points[i+1].y])                            # Направляющий вектор прямой
            b = (wall.points[i].x* (wall.points[i+1].y - wall.points[i].y) - wall.points[i].y*(wall.points[i+1].x - wall.points[i].x))

            if (abs(vec.y * ball.center.x - vec.x * ball.center.y + b )/vec.len() <= ball.radius):

                nA = Vector([vec.y,-vec.x]).scale( abs(vec.y * ball.center.x - vec.x * ball.center.y + b )/vec.len()**2)
                V = nA + ball.center

                if (wall.points[i].x <= V.x <= wall.points[i+1].x) or (wall.points[i].y <= V.y < wall.points[i+1].y):
                    ball.speed.rebound(vec)

                # if (wall.points[i].x <= ball.center.x <= wall.points[i+1].x) or (wall.points[i].y <= ball.center.y <= wall.points[i+1].y):
                #     ball.speed.rebound(vec)


    # ▀█▀ █▀▀ █▀ ▀█▀ █▀
    # ░█░ ██▄ ▄█ ░█░ ▄█

    def TEST(self):
        self.test_2()

    def test_1(self):
        self.clear()
        self.add(self.walls,
                 Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0.1, angle = 45),
                 Rect_Wall( [450, 500], "images/walls/Sergi.jpg", angular_velocity = 2, angle = 45, vx = 0.2, vy = -0.4),


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
                 Rect_Wall( [150, 150], "images/walls/wall_test.png", angular_velocity = 0, angle = 71),

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
                 Ball( [400, 210], b, angular_velocity = 0, vx = speed, vy = 8),
                 Ball( [400, 234], b, angular_velocity = 0, vx = speed, vy = 3),
                 Ball( [400, 221], b, angular_velocity = 0, vx = speed, vy = 2),)

    def test_3(self):
        self.clear()
        self.add(self.walls,
                 Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0, angle = 180),


                 Rect_Wall( [500, 5], "images/walls/wall_w.png", angle = 0),
                 Rect_Wall( [500, 645], "images/walls/wall_w.png", angle = 0),
                 Rect_Wall( [5, 325], "images/walls/wall_w.png", angle = 90),
                 Rect_Wall( [995, 325], "images/walls/wall_w.png", angle = 90))
                 # Rect_Wall( [200, 230], "images/walls/wall_test.png", angular_velocity = 0, angle = 45))
                 # Rect_Wall( [600, 230], "images/walls/wall_test.png", angle = 0))
        self.add(self.balls,
                 Ball( [400, 230], "images/ball_small.png", angular_velocity = 0, vx = -3) )



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

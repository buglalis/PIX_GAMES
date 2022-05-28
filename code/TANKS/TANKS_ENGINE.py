from GAME_ENGINE import *

class Tanks_engine(Game_engine):
    def __init__(self):
        # super().__init__()
        self.tanks = []
        self.players = []

    def add(self, array, *objects):
        for obj in objects: array.append(obj)

    def clear(self):
        self.tanks = []
        self.players = []

    def update(self):
        for player in self.players:
            player.update()
            yield player.tank


    def test(self):
        self.clear()
        tank = Tank([200, 230], "images/walls/wall_test.png" )
        self.add(self.players,
                 Tank_Player( tank ))


class Tank:
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        self.rect = Rect(point, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity)


    def draw(self, screen):
        self.rect.draw(screen)

    def update(self):
        # a dict with required moves(they're vectors) to be used conveniently
        key = pygame.key.get_pressed()
        dir = {key[pygame.K_w]: (Vector([0, -1]),0),
                key[pygame.K_s]: (Vector([0, 1]),180),
                key[pygame.K_a]: (Vector([-1, 0]),90),
                key[pygame.K_d]: (Vector([1, 0]),-90),
                key[pygame.K_w] and key[pygame.K_a]: (Vector([-0.5 ** 0.5, -0.5 ** 0.5]),45),
                key[pygame.K_w] and key[pygame.K_d]: (Vector([0.5 ** 0.5, -0.5 ** 0.5]),-45),
                key[pygame.K_s] and key[pygame.K_a]: (Vector([-0.5 ** 0.5, 0.5 ** 0.5]),135),
                key[pygame.K_s] and key[pygame.K_d]: (Vector([0.5 ** 0.5, 0.5 ** 0.5]),-135)}

        for butt in dir.keys():
            if butt:
                # self.rect.move(Vector([10,0]))
                self.rect.move(dir[butt][0])
                self.rect.set_angle(dir[butt][1])
                self.rect.update()
                return


class Rect_Wall(Rect):
    def __init__(self, point, filename, angle = 0, vx = 0, vy = 0, ax = 0, ay = 0, angular_velocity = 0):
        super().__init__(point, filename, vx = vx, vy = vy, ax = ax, ay = ay, angle = angle, angular_velocity = angular_velocity )

class Box(Rect_Wall):
    def __init__(self, point, filename, angle = 0 ):
        super().__init__(point, filename, angle = angle)


class Tank_Player(Player):
    def __init__(self, tank, speed = 5):
        self.tank = tank
        self.speed = speed

    def update(self):
        self.tank.update()





    # def key_events(self):
    #         if keys[self.UI.KEY.Z]:
    #              self.requet_l.update(int(PLAYER_SPEED))
    #         elif keys[self.UI.KEY.A]:
    #              self.requet_l.update(int(-PLAYER_SPEED))
    #         if keys[self.UI.KEY.M]:
    #              self.requet_r.update(int(PLAYER_SPEED))
    #         elif keys[self.UI.KEY.K]:
    #              self.requet_r.update(int(-PLAYER_SPEED))

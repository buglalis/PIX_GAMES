from PIL import Image
from GAME_ENGINE import Rect,Circle,Rect_Wall
from TankGame import*
from Acts import Acts,Vector

def image_size(filename):
    im = Image.open(filename)
    return im.size

class Tank:

    def __init__(self, pos: Vector, picture: str, move_keyboard: dict, other_keyboard:dict):

        self.SPEED = 1
        self.pos = pos
        self.body = Rect([self.pos.x, self.pos.y], picture)
        self.direc = Vector([0, -1])
        self.objects = []
        self.m_keyboard = move_keyboard
        self.o_keyboard = other_keyboard
        self.d_ticks = 0

    def draw(self, screen):
        # self.image.fill((0, 0, 0))
        self.body.draw(screen)
        for obj in self.objects:
            obj.draw(screen)
        # screen.blit(self.image, self.pos.get())

    def __get_clicks(self, ticks):
        """self.keyboard has the following structure -
        {*a button of a bunch of them(in tuple)* : a function from class Acts, ..... }"""
        key = pygame.key.get_pressed()
        pressings = list()
        def length(obj):
            if isinstance(obj, int):
                return 1
            else:
                return len(obj)
        for k in range(len(key)):
            if key[k]:
                pressings.append(k)
        for butts1 in self.o_keyboard.keys():
            if key[butts1]:
                if ticks-self.d_ticks > 1000:
                    self.d_ticks = pygame.time.get_ticks()
                    self.o_keyboard[butts1](self)
                    if len(self.objects) >= 3:
                        self.objects.pop(0)
        for butts0 in sorted(self.m_keyboard.keys(), key=length, reverse=True):
            if isinstance(butts0, int):
                butts = {butts0}
            else:
                butts = set(butts0)

            if butts.issubset(pressings):
                self.m_keyboard[butts0](self)
                return

    def shoot(self):
        self.objects.append(
            Circle([self.body.center.x, self.body.center.y], 'ball.png', vx=self.direc.x * 5, vy=self.direc.y * 5))

    def update(self):
        ticks = pygame.time.get_ticks()
        #print(ticks)
        # a dict with required moves(they're vectors) to be used conveniently
        self.__get_clicks(ticks)
        for obj in self.objects:
            obj.update()

t = TankGame()
a = Tank(Vector([60, 50]), "player00.png",
         {pygame.K_w: Acts.forward,
          pygame.K_s: Acts.backward,
          pygame.K_a: Acts.left,
          pygame.K_d: Acts.right,
          (pygame.K_w, pygame.K_a): Acts.forwardleft,
          (pygame.K_w, pygame.K_d): Acts.forwardright,
          (pygame.K_s, pygame.K_a): Acts.backwardleft,
          (pygame.K_s, pygame.K_d): Acts.backwardright},
         {pygame.K_x: Acts.shoot})
b = Tank(Vector([300, 50]), "player00.png",
         {pygame.K_i: Acts.forward,
          pygame.K_k: Acts.backward,
          pygame.K_j: Acts.left,
          pygame.K_l: Acts.right,
          (pygame.K_i, pygame.K_j): Acts.forwardleft,
          (pygame.K_i, pygame.K_l): Acts.forwardright,
          (pygame.K_k, pygame.K_j): Acts.backwardleft,
          (pygame.K_k, pygame.K_l): Acts.backwardright},
         {pygame.K_m: Acts.shoot})

t.push_back(a)
t.push_back(b)
t.push_back(Rect_Wall( [t.width/2, t.height-5], "wall_w.png", angle = 0))
t.push_back(Rect_Wall( [t.width/2, 5], "wall_w.png", angle = 0))
t.push_back(Rect_Wall( [5, t.height/2], "wall_w.png", angle = 85))
t.push_back(Rect_Wall( [t.width-5, t.height/2], "wall_w.png", angle = 90))
t.start()

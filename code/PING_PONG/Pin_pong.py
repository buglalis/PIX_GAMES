from Pin_Pong_lib import *
from UI import *
from GAME import *

PLAYER_SPEED = 5
BALL_SPEED   = 1
GATE_WIDTH   = 25



class Pin_Pong(Game):
    def __init__(self, width = 700, height = 500):
        super().__init__(self, width, height, name = "Pin Pong💀")

        # self.requet_l = Raquet((0, self.height/2-60), 24, 120, "./images/bat00_2.png", (0,self.height), PLAYER_SPEED)
        # self.requet_r = Raquet((self.width-24, self.height/2-60), 24, 120, "./images/bat10_2.png", (0,self.height), PLAYER_SPEED)
        #
        # self.ball = Ball((self.width/2, self.height/2), 10, "./images/ball.png", BALL_SPEED)



    def start(self):
        super().start()
        self.screen = pygame.display.set_mode((self.width, self.eight))

        ########
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # self.events(event)
            self.key_events()


            self.game_cycle()


    def draw(self):
        self.requet_l.draw(self.screen)
        self.requet_r.draw(self.screen)
        self.ball.draw(self.screen)


    def game_cycle(self):

        #
        self.regular_events_update()
        #

        self.screen.fill((255, 255, 255))
        # self.gate_r.update(self.screen)
        # self.gate_l.update(self.screen)

        # self.requet_l.update(5, self.screen)
        # pygame.display.update()

        self.draw()

        pygame.display.flip()

        super().game_cycle()


    def collisions_find(self):
            pass


    def regular_events_update(self):
        self.ball.update( (self.requet_l.rect.x, self.requet_l.rect.y, self.requet_l.rect.width, self.requet_l.rect.height),
                            (self.requet_r.rect.x, self.requet_r.rect.y, self.requet_r.rect.width, self.requet_r.rect.height),
                            (0,0,700,20),(480,0,700,20))


    def key_events(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                 self.requet_l.update(int(PLAYER_SPEED))
            elif keys[pygame.K_a]:
                 self.requet_l.update(int(-PLAYER_SPEED))
            if keys[pygame.K_m]:
                 self.requet_r.update(int(PLAYER_SPEED))
            elif keys[pygame.K_k]:
                 self.requet_r.update(int(-PLAYER_SPEED))

    # Not used NOW!
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.requet_l.update(int(PLAYER_SPEED))
            elif event.key == pygame.K_z:
                self.requet_l.update(int(-PLAYER_SPEED))

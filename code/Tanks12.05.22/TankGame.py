import pygame
import sys  # for us to quit the game
class TankGame:
    def __init__(self, width=360, height=480, name="tanks", FPS=60):
        self.objects = []
        self.name = name
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.running = True

    def push_back(self, obj):
        self.objects.append(obj)

    def game_cycle(self, *args):
        self.screen.fill((0, 255, 255))
        self.clock.tick(self.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        for obj in self.objects:
            obj.update()
        for obj in self.objects:
            obj.draw(self.screen)
        pygame.display.flip()

    def start(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(self.name)
        while self.running:
            self.game_cycle()
        pygame.quit()
        sys.exit()
from Game_lib import *
# from collision_lib import *

#   Interactive objects

class Ball(Move_obj):
    def __init__(self, point, radius, filename,):
        super().__init__( pos[0], pos[1], filename)
        self.radius = radius
        # self.image.fill((50,50,50))
        self.rect = pygame.Rect((pos[0]-20, pos[1]-20, 20, 20))
        self.rect.width  = 20
        self.rect.height = 20
        self.speed = speed
        #
        self.vy = 0
        self.vx = 1  #-speed



    #  This is inefficient and needs in redoing
    def update(self, requet_l, requel_r, wall_hi, wall_low):
        for i in (requet_l, requel_r, wall_hi, wall_low):
            if point_in_rect((self.rect.x, self.rect.y+10),i):
                self.vx = -self.vx
            elif point_in_rect((self.rect.x+10, self.rect.y),i):
                self.vy = -self.vy
            elif point_in_rect((self.rect.x+20, self.rect.y+10),i):
                self.vx = -self.vx
            elif point_in_rect((self.rect.x+10, self.rect.y+20),i):
                self.vy = -self.vy
        self.rect.x += self.vx
        self.rect.y += self.vy
            # [ (self.x, self.y+10), (self.x+10, self.y), (self.x+20, self.y+10), (self.x+10, self.y+20) ]


    def draw(self, *args): #ARGS => 1: screen;
        args[0].blit(self.image,(self.rect.x, self.rect.y)) #  args[0] -> it is work screen



class Raquet(Wall, Move_obj):
    def __init__(self, pos, width, height, filename, border, speed):
        Wall.__init__(self, pos[0], pos[1], width, height, filename)
        # self.surf = pygame.Surface((10, 10))
        # self.image.fill((50,50,50))
        # self.rect = self.image.get_rect()
        self.rect = pygame.Rect((pos[0], pos[1], 20, 160))
        self.rect.width  = 24
        self.rect.height = 120
        # self.rect.center = (self.width / 2, self.height / 2)
        self.border = border
        self.speed = speed


    def update(self, *args): #ARGS => 1: dy;
        if (self.height/2 < self.rect.center[1] < self.border[1] - self.height/2): #  So that it does not fly out of the window
            self.rect.y += args[0]
        elif(self.rect.y == 0 and args[0] > 0) or (self.rect.y >= self.border[1]-120 and args[0] < 0 ):
            self.rect.y += args[0]

        # print(self.rect.y, self.rect.center[1], self.image)


        # args[1].blit(self.image,(self.rect.x, self.rect.y))
        # args[1].blit(args[2],(self.rect.x, self.rect.y))
        # args[1].blit(self.image, self.rect)


    def draw(self, *args): #ARGS => 1: screen;
        args[0].blit(self.image,(self.rect.x, self.rect.y)) #  args[0] -> it is work screen



# class Basic_Wall(Wall):
#     def __init__(self, x, y, width, height, color = "Gray"):
#         super().__init__(self,  x, y, width, height)
#         self.color = color
#
#
#     def update(self, *args):
#         pass


class Gate(Wall):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.condition = True

    def update(self, *args):
        pygame.draw.rect(args[0], (0,0,0), (self.x, self.y, self.width, self.height))

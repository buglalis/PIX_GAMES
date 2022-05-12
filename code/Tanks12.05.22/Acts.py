from GAME_ENGINE import Vector
class Acts:
    @staticmethod
    def forward(lord):
        lord.direc = Vector([0, -1])
        lord = lord.body
        lord.move(Vector([0, -1]))
        lord.set_angle(0)

    @staticmethod
    def backward(lord):
        lord.direc = Vector([0, 1])
        lord = lord.body
        lord.move(Vector([0, 1]))
        lord.set_angle(180)

    @staticmethod
    def right(lord):
        lord.direc = Vector([1, 0])
        lord = lord.body
        lord.move(Vector([1, 0]))
        lord.set_angle(-90)

    @staticmethod
    def left(lord):
        lord.direc = Vector([-1, 0])
        lord = lord.body
        lord.move(Vector([-1, 0]))
        lord.set_angle(90)

    # there is a diagonal movements. for object to move with const speed
    #  they are like trigonometry circle = sqrt(2)/2
    @staticmethod
    def forwardright(lord):
        lord.direc = Vector([0.5 ** 0.5, -0.5 ** 0.5])
        lord = lord.body
        lord.move(Vector([0.5 ** 0.5, -0.5 ** 0.5]))
        lord.set_angle(-45)

    @staticmethod
    def forwardleft(lord):
        lord.direc = Vector([-0.5 ** 0.5, -0.5 ** 0.5])
        lord = lord.body
        lord.move(Vector([-0.5 ** 0.5, -0.5 ** 0.5]))
        lord.set_angle(45)

    @staticmethod
    def backwardright(lord):
        lord.direc = Vector([0.5 ** 0.5, 0.5 ** 0.5])
        lord = lord.body
        lord.move(Vector([0.5 ** 0.5, 0.5 ** 0.5]))
        lord.set_angle(-135)

    @staticmethod
    def backwardleft(lord):
        lord.direc = Vector([-0.5 ** 0.5, 0.5 ** 0.5])
        lord = lord.body
        lord.move(Vector([-0.5 ** 0.5, 0.5 ** 0.5]))
        lord.set_angle(135)

    @staticmethod
    def shoot(lord):
        lord.shoot()


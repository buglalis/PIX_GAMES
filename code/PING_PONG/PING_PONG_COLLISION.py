import numpy as np

def interaction_of_ball_wall(self, ball, wall, splitting = 10):
    points = np.zeros((splitting, 3))

    # Setting the coordinates of the points

    # Checking intersections
    for point in points:
        if ( (ball.center.x - point[0])**2 + (ball.center.y - point[1])**2 <= ball.size[0] ):
            ball.rebound(normal)

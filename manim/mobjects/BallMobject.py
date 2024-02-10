from manim import *
import numpy as np

class Ball(Mobject):

    def __init__(self, x=0, y=0, **kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.create_ball()
    
    def create_ball(self):
        ball = Circle(color=BLACK, fill_opacity=1)
        ball.scale(1/5)
        ball.move_to(np.array([self.x, self.y, 0]))
        self.add(ball)
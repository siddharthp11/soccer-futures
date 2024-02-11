from manim import *
import numpy as np

class Ball(VMobject):

    def __init__(self, position=(0, 0), **kwargs):
        super().__init__(**kwargs)
        self.x = position[0]
        self.y = position[1]
        self.create_ball()
    
    def create_ball(self):
        ball = Circle(color=GREEN_A, fill_opacity=1)
        ball.scale(1/8)
        ball.move_to((self.x, self.y, 0))
        self.add(ball)
from manim import *
from mobjects.SoccerFieldMobject import SoccerField  # Make sure soccer_field.py is in the same directory
from mobjects.BallMobject import Ball

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        ball = Ball(x=2, y=1)
        self.add(soccer_field, ball)
        self.wait(1)
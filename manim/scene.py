from manim import *
from mobjects.SoccerFieldMobject import SoccerField  # Make sure soccer_field.py is in the same directory

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        self.add(soccer_field)
        self.wait(1)
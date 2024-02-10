from manim import *
from mobjects.SoccerFieldMobject import SoccerField
from mobjects.SoccerPlayerMobject import SoccerPlayer
from mobjects.BallMobject import Ball

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        player_1 = SoccerPlayer(player_x=1, player_y=3, player_team=1)
        ball = Ball(x=2, y=1)
        self.add(soccer_field, player_1, ball)
        self.wait(1)
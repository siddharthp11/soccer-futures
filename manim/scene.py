from manim import *
from mobjects.SoccerFieldMobject import SoccerField
from mobjects.SoccerPlayerMobject import SoccerPlayer
from mobjects.BallMobject import Ball
from utils.transform_coor import transform_coor

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        player_1 = SoccerPlayer(player_x=1, player_y=3, player_team=1)
        ball_x, ball_y = transform_coor(x=1921.000, y=1078.000)
        ball = Ball(x=ball_x, y=ball_y)
        self.add(soccer_field, player_1, ball)
        self.wait(1)
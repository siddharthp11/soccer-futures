from manim import *
from mobjects.SoccerFieldMobject import SoccerField
from mobjects.SoccerPlayerMobject import SoccerPlayer

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        player_1 = SoccerPlayer(player_x=1, player_y=3, player_team=1)
        self.add(soccer_field, player_1)
        self.wait(1)
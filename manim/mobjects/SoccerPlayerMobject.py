from manim import *

class SoccerPlayer(Mobject):
    def __init__(self, player_x, player_y, player_team, **kwargs):
        super().__init__(**kwargs)
        self.player_x = player_x
        self.player_y = player_y
        self.player_team = player_team
        self.player_colors = {0: RED, 1: BLUE}
        self.create_player()
    
    def create_player(self):
        # Create soccer player as a circle
        player_circle = Circle(color=self.player_colors[self.player_team], fill_opacity=1, stroke_width=0)
        player_circle.scale(1/4)
        player_circle.move_to(self.player_x * RIGHT + self.player_y * UP)
        self.add(player_circle)
        
    
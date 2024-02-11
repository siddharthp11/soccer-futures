from manim import VMobject, Circle, np, RED, BLUE

class SoccerPlayer(VMobject):
    def __init__(self, position, team, **kwargs):
        super().__init__(**kwargs)
        self.x = position[0]
        self.y = position[1]
        self.team = team
        self.colors = {0: RED, 1: BLUE}
        self.create_player()
    
    def create_player(self):
        # Create soccer player as a circle
        player = Circle(color=self.colors[self.team], fill_opacity=1)
        player.scale(1/6)
        player.move_to(np.array([self.x, self.y, 0]))
        self.add(player)

    
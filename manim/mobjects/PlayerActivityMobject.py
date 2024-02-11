from manim import VMobject, Ellipse, Text, BLUE, RED, np

class PlayerEllipse(VMobject):

    def __init__(self, mean_x, mean_y, angle, ellipse_width, ellipse_height, player_team, **kwargs):
        super().__init__(**kwargs)
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.angle = angle
        self.ellipse_width = ellipse_width
        self.ellipse_height = ellipse_height
        self.player_team = player_team
        self.colors = {0: RED, 1: BLUE}
        self.createActivityArea()

    def createActivityArea(self):
        ellipse = Ellipse(width=self.ellipse_width, height=self.ellipse_height, color=self.colors[self.player_team])
        ellipse.set_fill(color=self.colors[self.player_team], opacity=0.5)
        ellipse.rotate(np.radians(self.angle))

        ellipse.move_to((self.mean_x, self.mean_y, 0))
        x_symbol = Text("X", color=self.colors[self.player_team])
        x_symbol.scale(0.3)
        x_symbol.move_to((self.mean_x, self.mean_y, 0))
        self.add(ellipse)
        self.add(x_symbol)



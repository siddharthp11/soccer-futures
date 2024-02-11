from manim import *

class PlayerEllipse(VMobject):
    def __init__(self, mean_x, mean_y, angle, ellipse_width, ellipse_height, **kwargs):
        super().__init__(**kwargs)
        self.mean_x = mean_x
        self.mean_y = mean_y
        self.angle = angle
        self.ellipse_width = ellipse_width
        self.ellipse_height = ellipse_height
        self.createActivityArea()
    
    def createActivityArea(self):
        ellipse = Ellipse(width=self.ellipse_width, height=self.ellipse_height, color=BLUE)
        ellipse.set_fill(BLUE, opacity=0.5)
        ellipse.rotate(np.radians(self.angle))

        ellipse.move_to(np.array([self.mean_x, self.mean_y, 0]))
        self.add(ellipse)



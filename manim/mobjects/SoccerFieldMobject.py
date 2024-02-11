from manim import *

class SoccerField(Mobject):
    def __init__(self, field_color=BLACK, **kwargs):
        super().__init__(**kwargs)
        self.field_color = field_color
        self.create_field()
    
    def create_field(self):
        frame_width = config.frame_width
        frame_height = config.frame_height
        # Create a green rectangle to represent the field
        field = Rectangle(width=frame_width, height=frame_height, color=WHITE, fill_color=self.field_color, fill_opacity=1)
        
        # Define field markings
        center_circle = Circle(radius=0.8, color=WHITE)
        center_line = Line(start=field.get_top(), end=field.get_bottom(), color=WHITE)
        
        # Penalty areas
        penalty_area_width = 1.8
        penalty_area_height = 4.4
        penalty_area_left = Rectangle(width=penalty_area_width, height=penalty_area_height, color=WHITE)
        penalty_area_right = Rectangle(width=penalty_area_width, height=penalty_area_height, color=WHITE)
        penalty_area_left.align_to(field, LEFT)
        penalty_area_right.align_to(field, RIGHT)

        # Goal areas
        goal_area_width = 0.8
        goal_area_height = 2.4
        goal_area_left = Rectangle(width=goal_area_width, height=goal_area_height, color=WHITE).shift(LEFT * 5.3)
        goal_area_right = Rectangle(width=goal_area_width, height=goal_area_height, color=WHITE).shift(RIGHT * 5.3)
        goal_area_left.align_to(field, LEFT).shift(LEFT/2)
        goal_area_right.align_to(field, RIGHT).shift(RIGHT/2)
        # 44*18, 24*8

        # Center spot
        center_spot = Dot(point=ORIGIN, color=WHITE)

        # Group everything together and add to the custom Mobject
        self.add(field, center_circle, center_line, penalty_area_left, penalty_area_right, goal_area_left, goal_area_right, center_spot)

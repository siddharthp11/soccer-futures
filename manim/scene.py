from manim import *
from mobjects.SoccerFieldMobject import SoccerField
from mobjects.SoccerPlayerMobject import SoccerPlayer
from mobjects.BallMobject import Ball
from utils.transform_coor import transform_coor

import pandas as pd

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        self.add(soccer_field)
        position_data = pd.read_csv("../test_data/processed_data.csv")

        # Extract initial positions for players and ball from the first row of the data
        initial_player_positions = {}
        for i in range(22):
            player_x_col = f"player_{i}_x"
            player_y_col = f"player_{i}_y"
            player_x, player_y = position_data[player_x_col][0], position_data[player_y_col][0]
            transformed_x, transformed_y = transform_coor(player_x, player_y)
            initial_player_positions[i] = (transformed_x, transformed_y)
        
        ball_x, ball_y = position_data["ball_x"][0], position_data["ball_y"][0]
        transformed_ball_x, transformed_ball_y = transform_coor(ball_x, ball_y)
        ball_initial_position = (transformed_ball_x, transformed_ball_y)

        # Create player and ball objects
        players = VGroup(*[SoccerPlayer(position=initial_player_positions[i], team=0 if i < 11 else 1) for i in range(22)])
        ball = Ball(position=ball_initial_position)

        # Add players and ball to scene
        self.add(players, ball)

        # Animate movement frame by frame
        for _, frame_data in position_data.iterrows():
            animations = []
            # Update positions for players
            for i in range(22):
                player_x_col = f"player_{i}_x"
                player_y_col = f"player_{i}_y"
                new_x, new_y = transform_coor(frame_data[player_x_col], frame_data[player_y_col])
                players[i].generate_target()  # Prepare the target for animation
                players[i].target.move_to((new_x, new_y, 0))
                animations.append(MoveToTarget(players[i]))
            
            # Update ball position
            new_ball_x, new_ball_y = transform_coor(frame_data["ball_x"], frame_data["ball_y"])
            ball.generate_target()
            ball.target.move_to((new_ball_x, new_ball_y, 0))
            animations.append(MoveToTarget(ball))

            # Play all animations simultaneously for a smooth transition
            self.play(*animations, run_time=0.005)
        
        self.wait(1)

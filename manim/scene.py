from manim import *
from mobjects.SoccerFieldMobject import SoccerField
from mobjects.SoccerPlayerMobject import SoccerPlayer
from mobjects.BallMobject import Ball
from mobjects.PlayerActivityMobject import PlayerEllipse

from utils.transform_coor import transform_coor
from utils.find_initial_position import find_initial_position
from utils.player_ellipses import plot_std_dev_ellipses

import pandas as pd

class SoccerFieldScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        self.add(soccer_field)
        
        # Extract initial positions for players and ball from the first row of the data
        position_data = pd.read_csv("../test_data/processed_data.csv")
        initial_player_positions, ball_initial_position = find_initial_position(position_data)

        # Create player and ball objects
        players = VGroup(*[SoccerPlayer(position=initial_player_positions[i], team=0 if i < 11 else 1) for i in range(22)])
        ball = Ball(position=ball_initial_position)

        # Add players and ball to scene
        self.add(players, ball)

        # Animate movement frame by frame
        for frame_n, frame_data in position_data.iterrows():
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
            self.play(*animations, run_time=20)

        self.wait(1)

        '''
        # Creating Characteristic Area
        mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(
            player_data=position_data.iloc[1, 0:22], 
            player_ids=list(range(11)))
        team_ellipse_0 = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                       angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                       player_team=0)
        self.add(team_ellipse_0)

        # # Creating Characteristic Area
        mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(
            player_data=position_data.iloc[1, 22:44], 
            player_ids=list(range(11, 22)))
        team_ellipse_1 = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                       angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                       player_team=1)
        self.add(team_ellipse_1)

        # Animate movement frame by frame
        for frame_no, frame_data in position_data.iterrows():
            animations = []
            # Calculate characteristic area for frame_no for team 0
            mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(player_data=position_data.iloc[frame_no, :22], player_ids=list(range(11)))
            team_ellipse_0.set_mean_x(mean_x)
            team_ellipse_0.set_mean_x(mean_y)
            team_ellipse_0.set_ellipse_width(ellipse_width)
            team_ellipse_0.set_ellipse_height(ellipse_height)
            # = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                            # angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                            # player_team=0)
            team_ellipse_0.generate_target()
            team_ellipse_0.move_to((mean_x, mean_y, 0))
            animations.append(MoveToTarget(team_ellipse_0))

            # Calculate characteristic area for frame_no for team 0
            mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(player_data=position_data.iloc[frame_no, 22:44], player_ids=list(range(11, 22)))
            character_ellipse = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                            angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                            player_team=1)
            # team_ellipse_1.set_mean_x(mean_x)
            # team_ellipse_1.set_mean_x(mean_y)
            # team_ellipse_1.set_ellipse_width(ellipse_width)
            # team_ellipse_1.set_ellipse_height(ellipse_height)
            # = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                            # angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                            # player_team=0)
            team_ellipse_1.generate_target()
            team_ellipse_1.target.move_to((mean_x, mean_y, 0))
            team_ellipse_1.move_to((mean_x, mean_y, 0))
            animations.append(MoveToTarget(team_ellipse_1))

        self.play(*animations, run_time=0.0005)
        '''


class ActivityAreasScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        self.add(soccer_field)

        # Extract initial positions for players and ball from the first row of the data
        position_data = pd.read_csv("../test_data/processed_data.csv")

        team1_ellipses_group = VGroup()
        team2_ellipses_group = VGroup()

        # Creating Ellipse Activity Areas for Team 0
        for i in range(11):
            player_data = position_data[[f'player_{i}_x', f'player_{i}_y']]
            mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(player_data, [i])
            team_ellipse = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, player_team=0 if i < 11 else 1)
            team1_ellipses_group.add(team_ellipse)
        
         # Creating Ellipse Activity Areas for Team 1
        for i in range(11, 22):
            player_data = position_data[[f'player_{i}_x', f'player_{i}_y']]
            mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(player_data, [i])
            team_ellipse = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, player_team=0 if i < 11 else 1)
            team2_ellipses_group.add(team_ellipse)
        
        self.add(team1_ellipses_group)
        self.play(Create(team1_ellipses_group))

        self.add(team2_ellipses_group)
        self.play(Create(team2_ellipses_group))

        self.wait(1)


class CharacteristicAreaScene(Scene):
    def construct(self):
        soccer_field = SoccerField()
        self.add(soccer_field)
        
        # Extract initial positions for players and ball from the first row of the data
        position_data = pd.read_csv("../test_data/processed_data.csv")
        initial_player_positions, ball_initial_position = find_initial_position(position_data)

        # Create player and ball objects
        players = VGroup(*[SoccerPlayer(position=initial_player_positions[i], team=0 if i < 11 else 1) for i in range(22)])
        ball = Ball(position=ball_initial_position)

        # Add players and ball to scene
        self.add(players, ball)

        mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(
        player_data=position_data.iloc[:, 0:22], 
        player_ids=list(range(11)))
        team_ellipse = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                       angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                       player_team=0)
        self.add(team_ellipse)

        # Creating Characteristic Area
        mean_x, mean_y, angle, ellipse_width, ellipse_height = plot_std_dev_ellipses(
            player_data=position_data.iloc[:, 22:44], 
            player_ids=list(range(11, 22)))
        team_ellipse = PlayerEllipse(mean_x=mean_x, mean_y=mean_y, 
                                       angle=angle, ellipse_width=ellipse_width, ellipse_height=ellipse_height, 
                                       player_team=1)
        self.add(team_ellipse)
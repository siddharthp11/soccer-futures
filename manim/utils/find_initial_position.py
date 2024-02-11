import pandas as pd

from .transform_coor import transform_coor

def find_initial_position(position_data):
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

  return initial_player_positions, ball_initial_position

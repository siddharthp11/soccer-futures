import pandas as pd

# Assuming `df` is your DataFrame with columns 'player0_x', 'player0_y', ..., 'ball_x', 'ball_y'
# Let's say `last_actual_row` is the last row of actual data and `first_predicted_row` is the first row of predicted data

# Concatenate the last actual row with the first predicted row
processed_data = pd.read_csv("test_data/processed_data.csv")
predictions = pd.read_csv("test_data/predictions.csv")
last_actual_row = processed_data.iloc[-1:]
first_predicted_row = predictions.iloc[:1]
transition_df = pd.concat([last_actual_row, first_predicted_row]).reset_index(drop=True)

# Use linear interpolation to fill in a specified number of intermediate frames
num_intermediate_frames = 1  # Number of frames you want to interpolate between the actual and predicted frames
interpolated_df = transition_df.reindex(range(num_intermediate_frames + 2)).interpolate()

# Now, `interpolated_df` contains the original rows and interpolated rows to smooth the transition
#prepend interpolated_df to predictions
predictions = pd.concat([interpolated_df, predictions]).reset_index(drop=True)
#save to csv in test_data
predictions.to_csv("test_data/new_predictions.csv", index=False)
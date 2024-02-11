import pandas as pd 
import torch 

def process_csv(path_to_csv):
    temp = pd.read_csv(path_to_csv, header=None)
    #drop bs stuff 
    temp = temp.drop([0, 1, 2, 3])
    temp = temp.iloc[:,1:]  # Drop the first column if it's not needed

    # Reset the index without adding the old index as a column
    temp = temp.reset_index(drop=True)

    # Converting data type into floats
    temp = temp.astype(float)
    temp = temp.iloc[:900,:]
    df = preprocess_df(temp, 15, normalize=True)
    input_tensor = get_tensor_from_df(df)

    output_names = df.columns 
    return input_tensor, output_names 

def normalize_positions(positions_data, max_width=3840, max_height=2160):
    print(positions_data)
    for i in range(22):
        x_result_column_name = f'player_{i}_x'
        y_result_column_name = f'player_{i}_y'

        # Calculate new columns and add them to the new DataFrame
        positions_data[x_result_column_name] /= (max_width)
        positions_data[y_result_column_name] /= (max_height)
    
    positions_data['ball_x'] /= max_width
    positions_data['ball_y'] /= max_height
    return positions_data


def clean_dataframe(new_data): 
    new_data = new_data.interpolate(method='index')
    if new_data.isnull().sum().sum()> 0: 
        print("! null values found")
    return new_data

def sample_rows(df, n): return df.iloc[::n]

def preprocess_df(data, n=1, normalize=True):
    num_columns = len(data.columns)
    group_size = 4
    num_players = num_columns // group_size

    # Create a new DataFrame
    new_data = pd.DataFrame()

    for i in range(num_players):
        group_columns = data.iloc[:, i*group_size:(i+1)*group_size]
        x_result_column_name = f'player_{i}_x'
        y_result_column_name = f'player_{i}_y'

        # Calculate new columns and add them to the new DataFrame
        new_data[x_result_column_name] = group_columns.iloc[:,1] + group_columns.iloc[:,3] / 2
        new_data[y_result_column_name] = group_columns.iloc[:,2] + group_columns.iloc[:,0] / 2

    # Handle the special case for ball coordinates
    if 'player_22_x' in new_data.columns and 'player_22_y' in new_data.columns:
        new_data = new_data.rename({'player_22_x': 'ball_x', 'player_22_y': 'ball_y'}, axis=1)
    
    new_data = clean_dataframe(new_data)
    if normalize: 
        new_data = normalize_positions(new_data)
    return sample_rows(new_data, n)


def get_tensor_from_df(df): 
    sequence_tensor = torch.tensor(df.values.reshape(len(df), -1)).float()
    return sequence_tensor 


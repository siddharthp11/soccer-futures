import numpy as np
import pandas as pd
from .transform_coor import transform_coor

def plot_std_dev_ellipses(player_data, player_ids):
    # Apply the custom function to each row of the DataFrame
    player_data = apply_transform_coor(player_data, player_ids)

    # Calculate mean
    mean_x, mean_y = np.mean(player_data, axis=0)

    # Calculate the covariance matrix
    cov_matrix = np.cov(player_data.T)

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # Sort the eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Use the first eigenvector to calculate the angle in degrees
    angle = np.degrees(np.arctan2(eigenvectors[1, 0], eigenvectors[0, 0]))
    ellipse_width = 2*np.sqrt(eigenvalues[0])
    ellipse_height = 2*np.sqrt(eigenvalues[1])

    # We want to return all the data that we need to connstruct the ellipse. 
    return mean_x, mean_y, angle, ellipse_width, ellipse_height

def apply_transform_coor(player_data, player_ids):
    if isinstance(player_data, pd.Series):                                                    #    0       1
        players = [transform_coor(player_data[i], player_data[i+1]) for i in range(0, 22, 2)] # [(x,y)], (x,y)]
        player_data = pd.DataFrame(players, columns=['x', 'y'])

        return player_data
    else:
        for id in player_ids:
            x_col = f"player_{id}_x"
            y_col = f"player_{id}_y"

            # for index in player_data.index:
            #     new_coords = transform_coor(player_data.loc[index, x_col], player_data.loc[index, y_col])
            #     player_data.at[index, x_col] = new_coords[0]
            #     player_data.at[index, y_col] = new_coords[1]

            player_data[[x_col, y_col]] = player_data.apply(
                lambda row: transform_coor(row[x_col], row[y_col]),
                axis=1,
                result_type="expand"
            )

        player_data = pd.DataFrame(player_data.values.reshape(-1, 2), columns=['x', 'y'])

        return player_data
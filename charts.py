import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
import pandas as pd
import seaborn as sns

colors = sns.color_palette()

def characteristic_area_by_frame(df, frame_number):
    # A demo of characteristic area
    # Specify the frame number to visualize

    # Plotting all player locations at a frame

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    _draw_soccer_field(ax)
    df_frame = df.iloc[frame_number]
    reshaped_df = pd.DataFrame(df_frame.values.reshape(-1, 2), columns=['x', 'y'])

    # Team 1
    ax.scatter(reshaped_df.iloc[:11, 0], reshaped_df.iloc[:11, 1], color = colors[0], marker='o', s=500)
    plot_std_dev_ellipses(reshaped_df.iloc[:11], ax, color = colors[0])

    # Team 2
    ax.scatter(reshaped_df.iloc[11:22, 0], reshaped_df.iloc[11:22, 1], color = colors[1], marker='o', s=500)
    plot_std_dev_ellipses(reshaped_df.iloc[11:22], ax, color = colors[1])

    # Ball
    ax.scatter(reshaped_df.iloc[22, 0], reshaped_df.iloc[22, 1], color = 'black', marker='o', s=500)

    plt.xlim(0, 3840)
    plt.ylim(0, 2160)
    plt.gca().invert_yaxis()
    plt.title(f'Characteristic Area of both teams at the frame number of {frame_number}', fontsize = 24)
    ax.axis('off')
    return fig 

def plot_std_dev_ellipses(player_data, ax, color):
    """
    Plot standard deviation ellipses and mean markers for players in a DataFrame.

    Parameters:
    player_data (DataFrame): DataFrame containing player coordinates.
    ax (Axes): Matplotlib Axes object to plot on.
    color (str): Color for the ellipse and marker.
    player_number (int): Player number to annotate.
    """

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

    # Drawing the standard deviation ellipse with orientation for each player
    ellipse = Ellipse((mean_x, mean_y), width=2*np.sqrt(eigenvalues[0]), height=2*np.sqrt(eigenvalues[1]),
                      angle=angle, facecolor=color, alpha=0.5)
    ax.add_patch(ellipse)

    # Marking the mean
    ax.scatter([mean_x], [mean_y], color=color, marker='X', s = 250)

def plot_activity_areas(df, ax, activity_obj= "team1"):
    """
    df: of game 
    activity_obj: team1, team2, or ball 
    outputs: plot of activity on field over time 
    """
    
    # Plotting activity patterns for Team 1
    _draw_soccer_field(ax)
    
    if activity_obj=="ball":
        plot_std_dev_ellipses(df.iloc[:, -2:], ax, color = colors[0])
    
    else: 
        player_range = range(0, 22, 2) if activity_obj == "team1" else range(22, 44, 2)
        for i in player_range:
            color = colors[i // 2 % len(colors)]
            plot_std_dev_ellipses(df.iloc[:, i:i+2], ax, color)

def _draw_soccer_field(ax):
    # Standard soccer field dimensions in meters
    field_length_m = 105
    field_width_m = 68

    # Scale factors
    field_length_px = 3840 * 0.75
    field_width_px = field_length_px / (field_length_m / field_width_m)  # Maintain aspect ratio

    # Field position
    field_left = (3840 - field_length_px) / 2
    field_top = (2160 - field_width_px) / 2

    # Drawing the field
    rect = plt.Rectangle((field_left, field_top), field_length_px, field_width_px, edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(rect)

    # Scale for meters to pixels
    scale_x = field_length_px / field_length_m
    scale_y = field_width_px / field_width_m

    # Center Circle
    center_circle_radius_m = 9.15  # Standard center circle radius
    center_circle = plt.Circle((3840 / 2, 2160 / 2), center_circle_radius_m * scale_x, color='black', fill=False, lw=2)
    ax.add_patch(center_circle)

    # Goal Areas (6-yard box)
    goal_area_length_m = 5.5
    goal_area_width_m = 18.32
    goal_area_left = plt.Rectangle((field_left, 2160 / 2 - (goal_area_width_m * scale_y / 2)), 
                                   goal_area_length_m * scale_x, goal_area_width_m * scale_y, 
                                   edgecolor='black', facecolor='none', lw=2)
    goal_area_right = plt.Rectangle((3840 - field_left - goal_area_length_m * scale_x, 2160 / 2 - (goal_area_width_m * scale_y / 2)), 
                                    goal_area_length_m * scale_x, goal_area_width_m * scale_y, 
                                    edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(goal_area_left)
    ax.add_patch(goal_area_right)

    # Vertical Center Line
    plt.plot([3840 / 2, 3840 / 2], [field_top, field_top + field_width_px], color='black', lw=2)

    
def plot_player_posn(df, ax, player_idx):
    """
    df: dataframe of game 
    ax: ax on which to draw player posn 
    """
    # Draw the soccer field
    _draw_soccer_field(ax)

    adjusted_idx = player_idx * 2

    # Plotting player positions
    ax.scatter(df.iloc[:,adjusted_idx],df.iloc[:,adjusted_idx+1], color = colors[0])

def player_path(df, player_idx):
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    plot_player_posn(df, ax, player_idx=player_idx)
    plt.xlim(0, 3840)
    plt.ylim(0, 2160)
    plt.gca().invert_yaxis()
    plt.title(f'Path Traced by Player {player_idx}', fontsize = 24)
    ax.axis('off')
    return fig 
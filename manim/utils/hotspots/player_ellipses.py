import numpy as np

def plot_std_dev_ellipses(player_data):

    mean_x, mean_y = np.mean(player_data, axis=0)
    cov_matrix = np.cov(player_data).T
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

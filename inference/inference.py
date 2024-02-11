from torch.utils.data import Dataset, DataLoader
import torch
import pandas as pd
from process_csv import process_csv, get_tensor_from_df
import torch
import torch.nn as nn


class LSTMWithLinear(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=1):
        super(LSTMWithLinear, self).__init__()

        # LSTM layer
        self.lstm = nn.LSTM(input_size=input_size,
                            hidden_size=hidden_size,
                            num_layers=num_layers,
                            batch_first=True)

        # Linear layer
        self.linear = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        # x: input tensor of shape (batch_size, sequence_length, input_size)

        # Passing the input through the LSTM layer
        # lstm_out: tensor of shape (batch_size, sequence_length, hidden_size)
        lstm_out, _ = self.lstm(x)

        # Passing the output of the LSTM layer through the linear layer
        # This operation is applied to each time step, so we use lstm_out
        # linear_out: tensor of shape (batch_size, sequence_length, output_size)
        linear_out = self.linear(lstm_out)

        return linear_out


model = torch.load('inference/model.pt', map_location=torch.device('cpu'))
model.eval()


def denormalize_positions(output_names, norm_tensor, max_width=3840, max_height=2160):
    """
    norm_tensor(Torch.tensor[OutputLength, 46]): tensor with 46 positions for OutputLength frames. 
    Denormalize x and y positions from a [0, 1] range to their original scale.
    """

    for idx in range(norm_tensor.shape[1]):
        if idx % 2 == 0:
            norm_tensor[:, idx] *= max_width
        else:
            norm_tensor[:, idx] *= max_height

    df = pd.DataFrame(norm_tensor.cpu().numpy(), columns=output_names)

    return df


def next_k_inference(csv_file, num_available_frames, num_frames_to_predict):
    """
    input: test_dataset <torch dataset>. 
    output: list of dataframes, one for each element of the test dataset.
    """
    input_tensor, output_names = process_csv(csv_file)
    batch = input_tensor.unsqueeze(0)
    current_input = batch[:, :num_available_frames, :]

    predictions = current_input.clone()

    # Predict the next 'k' frames iteratively
    for _ in range(num_frames_to_predict):
        # Predict the next frame using the most recent frames
        with torch.no_grad():
            # Shape: [batch_size, 1, num_features]
            next_frame_pred = model(current_input)[:, -1:, :]
        predictions = torch.cat((predictions, next_frame_pred), dim=1)
        current_input = torch.cat(
            (current_input[:, 1:, :], next_frame_pred), dim=1)

    # Access the predicted frames
    predicted_frames = predictions[:, num_available_frames:, :]
    # convert the data into dataframe:
    predicted_frames = predicted_frames.squeeze(0)
    predictions_as_df = denormalize_positions(output_names, predicted_frames)

    return predictions_as_df

if __name__ == '__main__':
    csv_file = 'inference/data/corner.csv'
    predictions = next_k_inference(csv_file, num_available_frames=30, num_frames_to_predict=20)   
    print(predictions)
    print(predictions.shape)
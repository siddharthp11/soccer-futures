import time
import torch 
import torch.nn as nn

import run_inference
import streamlit as st

from streamlit_extras.row import row
from run_inference import next_k_inference


if "model" in st.session_state:
    pass
else: 
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
        
    model = torch.load('model.pt', map_location=torch.device('cpu'))
    st.session_state['model'] = model 


# Define the submit action
def submit_action(uploaded_files):
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            st.write(f"File submitted: {uploaded_file.name}")

title = st.markdown(body="<h1 style='text-align: center; color: white;'>PitchPerfect</h1>", unsafe_allow_html=True)
desc = st.markdown(body="<h4 style='text-align: center; color: white;'>Your platform to upload and analyze soccer training videos</h4><br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    with st.expander("Why use PitchPerfect?"):
        st.write("Do you want to predict how a given soccer play unfurls in the future from a given position? Pitch Perfect is a data driven solution that would allow you to predict the future of soccer plays unfold from a given position as well as visualize this data in a generated animated video clip form.")
    with st.expander("How does it work"):
        st.write("Our interface takes in an annotated csv file along with an mp4 video of the play and feeds it into a custom LSTM model we have developed to predict the future coordinates of all players and the ball for a short period of time in the future. We then use these coordinates to generate an animated clip of how the play could evolve, along with additional visualizations relating to player hotspots and team dynamic control areas.")
    with st.expander("Future Improvements"):
        st.write("In the future, we hope to develop an image segmentation model that would essentially allow us to generate the annotations csv file. We could also expand this approach to other sports like basketball or american football to predict plays.")

with col2:
    uploaded_files = st.file_uploader("Choose Files", accept_multiple_files=True, type=['csv', 'mp4'])
    submit_button = st.button("Submit", use_container_width=True)

    if submit_button:
        submit_action(uploaded_files)

# Embedded Training Videos
st.markdown(body="<h2 style='text-align: center; color: white;'>Embedded Training Videos</h2>", unsafe_allow_html=True)

st.markdown("""
  <style>
  div.stSpinner > div {
    text-align:center;
    align-items: center;
    justify-content: center;
  }
  </style>""", unsafe_allow_html=True)
with st.spinner('Computing...'):
    # time.sleep(5)
    # video_row = row(2, vertical_align="center")
    # video_row.video("data/top_view/viz_results/D_20220220_1_0000_0030.mp4")
    # video_row.video("data/top_view/viz_results/D_20220220_1_0000_0030.mp4")
    video1, video2 = st.columns(2)
    video1 = st.video("data/top_view/viz_results/D_20220220_1_0000_0030.mp4")
    video2 = st.video("data/top_view/viz_results/D_20220220_1_0000_0030.mp4")


def run_model():
    csv_file = 'inference/data/corner.csv'
    predictions = run_inference.next_k_inference(csv_file, num_available_frames=30, num_frames_to_predict=20)  
    print(predictions)

st.button(label='run model', on_click=run_model)
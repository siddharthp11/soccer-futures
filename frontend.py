import time
import torch 
import torch.nn as nn

import run_inference
import streamlit as st

from streamlit_extras.row import row
from run_inference import custom_forward_pass, format_processed_csv
import charts 


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


if "df" not in st.session_state: 
    df = format_processed_csv("test_data/processed_data.csv")
    st.session_state['df'] = df
        
    


# Define the submit action
def submit_action(uploaded_files):
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            st.session_state['uploaded_files'] = [uploaded_file]
            st.write(f"File submitted: {uploaded_file.name}")

def run_model():
    csv_file = "test_data/processed_data.csv"
    predictions = custom_forward_pass(st.session_state['model'], csv_file) 
    predictions.to_csv('test_data/predictions.csv', index=False)

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

st.markdown("""
  <style>
  div.stSpinner > div {
    text-align:center;
    align-items: center;
    justify-content: center;
    
  }
  </style>""", unsafe_allow_html=True)

if 'uploaded_files' in st.session_state:
    st.markdown(body="<h2 style='text-align: center; color: white;'> Visual Analytics </h2>", unsafe_allow_html=True)


    frame = st.slider("Select a frame", 0, len(st.session_state["df"]))
    fig = charts.characteristic_area_by_frame(st.session_state["df"], frame)
    st.pyplot(fig)

    player_position = st.slider("Select a player", 0, 21)
    fig = charts.player_path(st.session_state["df"], player_position)
    st.pyplot(fig)

    


if 'uploaded_files' in  st.session_state or submit_button:
    # with st.spinner('Computing...'):
    #     time.sleep(2)
        

    st.markdown(body="<h2 style='text-align: center; color: white;'> Visualization of Uploaded Game </h2>", unsafe_allow_html=True)

    st.video("SoccerFieldScene.mp4")
    st.markdown(body="<h2 style='text-align: center; color: white;'> Prediction by LSTM Neural Network </h2>", unsafe_allow_html=True)

    st.video("NewPredictionsScene.mp4")
    
    st.markdown(body="<h2 style='text-align: center; color: white;'> Covariance Matrix based Player Activity Areas </h2>", unsafe_allow_html=True)

    st.video("ActivityAreasScene.mp4")
        

       
#st.button(label='run model', on_click=run_model)
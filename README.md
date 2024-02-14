# Pitch Perfect: Predicting Soccer Game Positioning

## Demo Video (click on image): 
[![Pitch Perfect Demo](http://img.youtube.com/vi/wSdZr7G1JDo/0.jpg)](https://www.youtube.com/watch?v=wSdZr7G1JDo "Pitch Perfect Demo (Hackylytics 2024)")


## Instructions:
1. Create `venv` and install necsessary libraries using the `requirements.txt` file.
2. Run `streamlit run frontend.py` to begin the frontend service.

## What Is Pitch Perfect?
Do you want to predict how a given soccer play unfurls in the future from a given position? Pitch Perfect is a data driven solution that would allow you to predict the future of soccer plays unfold from a given position as well as visualize this data in a generated animated video clip form.

We wanted to create some sort of powerful analytics tool in the realm of sports that, if fully fleshed out, could provide valuable information that will transform the sports landscape. Being fans of soccer/futbol, we sought out to predict player movements within a soccer game given a set amount of their previous positions. 

## Why Does It Matter?
We see this project having a plethora of implications in professional sports analytics, sports betting, and sports training. If there was a tool that could provide in-depth analytics about the movement relationships amongst a team and even predict how certain positions dictate the future state of the game, the possibilities of application are endless. Notably, we see this tool providing social good to younger generations for the purposes of sports training as teams could utilize such a powerful tool to learn game patterns and develop their game theory skills. Furthermore, this concept could be expanded to many other team-based sports such as basketball, NFL football, hockey, etc.

## What Was Our Journey?
We found this helpful [dataset](https://www.kaggle.com/datasets/atomscott/soccertrack/data) that contains position data about the soccer players and the ball in several 30-second clips from multiple games. We preprocessed the dataset to allow for training and then built a custom generative LSTM model from the ground up to predict soccer positions, training on the dataset. We utilized Streamlit as the Python frontend framework and the `manim` Python library, popularly known from 3Blue1Brown YouTube videos, to generate our visualizations.

## What Were Our Challenges?
Building a generative model without simply making a ChatGPT wrapper is a very technically challenging task that is not doable within the time frame of a hackathon. However, we were able to extract key insights from the model and the model was even able to predict the outcome of an edge case like a corner kick in soccer. We also faced challenges using the `manim` library as it was our first time using the library and it can be rather complicated to create visualizations with it.

## What Accomplishments Are We Proud Of?
We were able to build an initial model that is capable of making decent predictions of player/ball positions. Additionally, we created `manim` animations and have ideated many future ideas that could continue to build on this seemingly limitless project.

## What Did We Learn?
We gained a plethora of technical skills including building an LSTM model, creating appealing data visualizations, exploring the field of sports analytics, and how to consider the usage of data in building useful applications.

## What Is Next for Pitch Perfect?
We have plenty of ideas that we formulated during the hackathon some of which being, polishing the model and visualizations, developing clustering algorithms to identify team formations and strategies, and implementing user-interactive visualizations, 


## Model -> Sid, Viren 
- [Dataset](https://www.kaggle.com/datasets/atomscott/soccertrack/data)
  Steps:
  1. pip install kaggle
  2. Generate API key in Kaggle account
  3. Add API key as such: ~/.kaggle/kaggle.json
  4. Use this command in project directory: kaggle datasets download -d atomscott/soccertrack --unzip
  5. Add all data files to a data folder in the project directory
- [Read](https://arno.uvt.nl/show.cgi?fid=148968) 
- Find Models on HF 
- Deploying the model to Intel Dev Cloud.


## UI -> Rishi, Harshith 
- [Manim](https://github.com/3b1b/manim) Integration
- Video Uploads. 
- Taipy Setup.

## Top level Dependencies 
- [Manim](https://docs.manim.community/en/stable/installation/macos.html#required-dependencies) 
- Huggingface / Pytorch 
- Intel Cloud 
- Pandas 

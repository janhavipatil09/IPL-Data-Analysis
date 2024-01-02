import math
import numpy as np
import pickle
import streamlit as st

# Load ML model
model_filename = 'ml_model.pkl'
model = pickle.load(open(model_filename, 'rb'))

# Set page configuration
st.set_page_config(page_title='IPL_Score_Predictor', layout="centered")

# HTML styling for title background
st.markdown("<h1 style='text-align: center; color: white;'> IPL Score Predictor 2022 </h1>", unsafe_allow_html=True)

# Background image styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://4.bp.blogspot.com/-F6aZF5PMwBQ/Wrj5h204qxI/AAAAAAAABao/4QLn48RP3x0P8Ry0CcktxilJqRfv1IfcACLcBGAs/s1600/GURU%2BEDITZ%2Bbackground.jpg");
        background-attachment: fixed;
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Description section
with st.expander("Description"):
    st.info("""A Simple ML Model to predict IPL Scores between teams in an ongoing match. To ensure accuracy and reliability, the model considers a minimum of 5 overs in the current match.
    """)

# Team Selection
batting_team = st.selectbox('Select the Batting Team', ('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
                                                       'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
                                                       'Royal Challengers Bangalore', 'Sunrisers Hyderabad'))

prediction_array = [1 if batting_team == team else 0 for team in
                     ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders',
                      'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']]

# Bowling Team
bowling_team = st.selectbox('Select the Bowling Team', ('Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab',
                                                       'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
                                                       'Royal Challengers Bangalore', 'Sunrisers Hyderabad'))

if bowling_team == batting_team:
    st.error('Bowling and Batting teams should be different')

prediction_array += [1 if bowling_team == team else 0 for team in
                      ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 'Kolkata Knight Riders',
                       'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore', 'Sunrisers Hyderabad']]

# Enter the Current Ongoing Over
overs = st.number_input('Enter the Current Over', min_value=5.1, max_value=19.5, value=5.1, step=0.1)
if overs - math.floor(overs) > 0.5:
    st.error('Please enter a valid over input as one over only contains 6 balls')

# Enter Current Run
runs = st.number_input('Enter Current runs', min_value=0, max_value=354, step=1, format='%i')

# Wickets Taken till now
wickets = st.slider('Enter Wickets fallen till now', 0, 9)
wickets = int(wickets)

# Runs in the last 5 over
runs_in_prev_5 = st.number_input('Runs scored in the last 5 overs', min_value=0, max_value=runs, step=1, format='%i')

# Wickets in the last 5 over
wickets_in_prev_5 = st.number_input('Wickets taken in the last 5 overs', min_value=0, max_value=wickets, step=1, format='%i')

# Get all the data for predicting
prediction_array += [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]
prediction_array = np.array([prediction_array])

# Display Predicted Score
if st.button('Predict Score'):
    my_prediction = int(round(model.predict(prediction_array)[0]))
    st.success(f'PREDICTED MATCH SCORE: {my_prediction - 5} to {my_prediction + 5}')

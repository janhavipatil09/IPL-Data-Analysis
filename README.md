# IPL Score Predictor
The objective of this project is to perform an in-depth analysis of IPL data to gain insights and predict outcomes. The project involves collecting and cleaning the data. The project covers various aspects like team and player performance, batting and bowling trends, venue analysis. Exploratory data analysis will be carried out using Pandas, NumPy, Matplotlib, Seaborn to identify patterns and correlations in the data, which will help in developing models for predicting match outcomes.

**Algorithms used:**

* Linear Regression
* RandomForest Regressor
* Decision Tree Regressor

**Hyperparamter Optimization:**

Used optuna for paramter optimization.

**Dataset:**

The dataset comprises of over by over details of matches and runs from 2008 to 2020.

Dataset Used: ipl_data.csv

* mid - match id
* date - when matches are played
* venue - place where matches aew played
* bat_team - batting team
* bowl_team - bowling team
* batsman - batsman
* bowler - bowler
* runs - runs scored
* wickets - wickets
* overs - overs - next 3 are based on this
* run_last_5 - runs scored in last 5 overs
* wicket_last_5 - wickets in last 5 overs
* stricker - batsman playing as main 1
* non-striker - batsman playing as runner up - not main 0
* total - total score (target variable)


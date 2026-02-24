# Pmpml-wait-time-prediction
End-to-end Machine Learning project predicting PMPML bus wait time, deployed using Streamlit.  

🚌 PMPML Bus Wait Time Prediction Using Machine Learning


📌 Project Overview
This project aims to predict the waiting time of buses operated by Pune Mahanagar Parivahan Mahamandal Limited (PMPML) using Machine Learning techniques.
The objective is to help commuters in Pune estimate bus arrival time more accurately based on historical and real-time data such as route, traffic conditions, time of day, and distance.


🎯 Problem Statement
Public transport users often face uncertainty in bus arrival times due to:
Traffic congestion

Weather conditions

Peak hour demand

Route-specific delays

This project builds a predictive ML model that estimates bus wait time to improve commuter planning and reduce uncertainty.


🧠 Machine Learning Approach
The project follows a complete ML lifecycle:

Data Collection

Historical bus timing data

Route information

Timestamp and traffic-related features

Data Preprocessing

Handling missing values

Feature engineering (hour, day, peak time)

Encoding categorical variables

Normalization / Scaling

Model Training Algorithms used:

Linear Regression

Random Forest Regressor

Decision Tree Regressor

Model Evaluation

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

Best Model Selection The model with lowest error and highest accuracy was selected for final prediction.


🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-learn

Matplotlib / Seaborn

Jupyter Notebook


📊 Features Used for Prediction

Bus Route Number

Stop ID

Distance to Stop

Time of Day

Day of Week

Historical Average Delay

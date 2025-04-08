# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_kjd9UOz6B43WoGMUawx9Rygho8Y6xDK
"""

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Column names for the dataset
column_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']

# Correct URL from UCI ML repo
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"

# Load the dataset
df = pd.read_csv(url, names=column_names)

# Encode categorical features
le = LabelEncoder()
df_encoded = df.apply(le.fit_transform)

# Split features and target
X = df_encoded.drop('class', axis=1)
y = df_encoded['class']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Streamlit UI
st.title("Car Evaluation Prediction App")

buying = st.selectbox('Buying', ['low', 'med', 'high', 'vhigh'])
maint = st.selectbox('Maintenance', ['low', 'med', 'high', 'vhigh'])
doors = st.selectbox('Doors', ['2', '3', '4', '5more'])
persons = st.selectbox('Persons', ['2', '4', 'more'])
lug_boot = st.selectbox('Lug Boot', ['small', 'med', 'big'])
safety = st.selectbox('Safety', ['low', 'med', 'high'])

user_input = pd.DataFrame({
    'buying': [buying],
    'maint': [maint],
    'doors': [doors],
    'persons': [persons],
    'lug_boot': [lug_boot],
    'safety': [safety]
})

# Encode user input
user_input_encoded = user_input.apply(le.transform)

# Make prediction
prediction = model.predict(user_input_encoded)
predicted_class = le.inverse_transform(prediction)

st.success(f"Predicted Car Class: {predicted_class[0]}")

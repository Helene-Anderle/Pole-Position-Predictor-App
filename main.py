import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Simple Silverstone example data
data = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "PoleTime": [92.937, 89.287, 86.600, 85.892, 85.093, 85.000, 86.760, 100.983, 86.720, 85.819]
})

st.title("F1 Pole Position Predictor")

st.subheader("Silverstone Circuit")

st.write("Historical Pole Position Times (seconds)")
st.dataframe(data)

# Simple prediction model
X = data[["Year"]]
y = data["PoleTime"]

model = LinearRegression()
model.fit(X, y)

next_year = np.array([[2025]])
prediction = model.predict(next_year)

st.subheader("Predicted 2025 Pole Time")
st.write(f"{prediction[0]:.3f} seconds")
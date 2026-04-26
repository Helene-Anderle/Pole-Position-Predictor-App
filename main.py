import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------------------
# Page setup
# ---------------------------
st.set_page_config(page_title="F1 Pole Predictor", layout="centered")

st.title("🏁 F1 Qualifying Performance Predictor")
st.markdown("""
Predict Formula 1 pole position lap times using historical qualifying data and simple trend modelling.
Select a circuit to view historical trends and predictions.
""")

st.divider()

# ---------------------------
# CIRCUIT BUTTONS
# ---------------------------
st.subheader("Select a Circuit")

col1, col2, col3 = st.columns(3)

silverstone_clicked = False

with col1:
    if st.button("Silverstone"):
        silverstone_clicked = True

with col2:
    st.button("Monaco (coming soon)", disabled=True)

with col3:
    st.button("Spa (coming soon)", disabled=True)

# ---------------------------
# SILVERSTONE DATA
# ---------------------------
if silverstone_clicked:

    st.subheader("Silverstone Circuit")

    data = pd.DataFrame({
        "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        "PoleTime": [92.937, 89.287, 86.600, 85.892, 85.093, 85.000, 86.760, 100.983, 86.720, 85.819]
    })

    st.write("Historical Pole Position Times (seconds)")
    st.dataframe(data)

    # Model
    X = data[["Year"]]
    y = data["PoleTime"]

    model = LinearRegression()
    model.fit(X, y)

    next_year = np.array([[2025]])
    prediction = model.predict(next_year)

    st.subheader("2025 Pole Position Prediction")
    st.metric(label="Predicted Time", value=f"{prediction[0]:.3f} seconds")

    st.caption("Simple linear regression based on historical qualifying trends.")
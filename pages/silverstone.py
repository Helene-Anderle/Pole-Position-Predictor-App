import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Silverstone Circuit")

st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Silverstone_Circuit_map.png")

data = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "PoleTime": [92.937, 89.287, 86.600, 85.892, 85.093, 85.000, 86.760, 100.983, 86.720, 85.819]
})

st.dataframe(data)

model = LinearRegression()
model.fit(data[["Year"]], data["PoleTime"])

prediction = model.predict(np.array([[2025]]))

st.metric("2025 Prediction", f"{prediction[0]:.3f} s")
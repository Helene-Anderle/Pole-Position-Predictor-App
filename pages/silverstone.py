import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Silverstone Analysis")

# ---------------- IMAGE ----------------
st.image("pages/silverstone.jpg", use_container_width=True)

st.divider()

# ---------------- DATA ----------------
data = pd.DataFrame({
    "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "PoleTime": [92.937, 89.287, 86.600, 85.892, 85.093, 85.000, 86.760, 100.983, 86.720, 85.819]
})

st.subheader("Pole Position Trend")

# ---------------- GRAPH ----------------
fig, ax = plt.subplots()
ax.plot(data["Year"], data["PoleTime"], marker="o")

ax.set_xlabel("Year")
ax.set_ylabel("Pole Time (s)")
ax.set_title("Silverstone Pole Position Trend")

st.pyplot(fig)
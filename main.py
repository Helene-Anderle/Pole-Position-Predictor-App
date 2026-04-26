import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="F1 Predictor", layout="wide")

# ---------------- HEADER ----------------
st.title("🏁 F1 Pole Position Predictor")
st.markdown("Select a circuit to view historical trends and predictions.")
st.divider()

# ---------------- CIRCUIT SELECTOR ----------------
circuit = st.selectbox(
    "Choose Circuit",
    ["Silverstone", "Monaco", "Spa"]
)

st.divider()

# ---------------- SILVERSTONE ----------------
if circuit == "Silverstone":

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3c/Silverstone_Circuit_map.png",
        use_container_width=True
    )

    st.subheader("Silverstone Analysis")

    data = pd.DataFrame({
        "Year": [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        "PoleTime": [92.937, 89.287, 86.600, 85.892, 85.093, 85.000, 86.760, 100.983, 86.720, 85.819]
    })

    fig, ax = plt.subplots()
    ax.plot(data["Year"], data["PoleTime"], marker="o")

    ax.set_xlabel("Year")
    ax.set_ylabel("Pole Time (s)")
    ax.set_title("Silverstone Pole Trend")

    st.pyplot(fig)

    st.metric("Predicted Pole (2025)", "85.7s")

# ---------------- MONACO ----------------
elif circuit == "Monaco":

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/9e/Monaco_circuit.png",
        use_container_width=True
    )

    st.subheader("Monaco Analysis")
    st.metric("Predicted Pole (2025)", "72.1s")

# ---------------- SPA ----------------
elif circuit == "Spa":

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/1/1e/Spa-Francorchamps.png",
        use_container_width=True
    )

    st.subheader("Spa Analysis")
    st.metric("Predicted Pole (2025)", "103.4s")
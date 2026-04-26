import streamlit as st

st.set_page_config(page_title="F1 Predictor", layout="wide")

# SIDEBAR
st.sidebar.title("🏎️ Circuits")

circuit = st.sidebar.selectbox(
    "Select Circuit",
    ["Silverstone", "Monaco", "Spa"]
)

# MAIN TITLE
st.title("F1 Pole Position Predictor")
st.divider()

# CONTENT SWITCH

if circuit == "Silverstone":
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Silverstone_Circuit_map.png")
    st.subheader("Silverstone")
    st.write("High-speed circuit with long corners and strong aero sensitivity.")
    st.metric("Predicted Pole Time (2025)", "85.7s")

elif circuit == "Monaco":
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9e/Monaco_circuit.png")
    st.subheader("Monaco")
    st.metric("Predicted Pole Time (2025)", "72.1s")

elif circuit == "Spa":
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1e/Spa-Francorchamps.png")
    st.subheader("Spa")
    st.metric("Predicted Pole Time (2025)", "103.4s")
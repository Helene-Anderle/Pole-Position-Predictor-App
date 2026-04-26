import streamlit as st

st.set_page_config(page_title="F1 Predictor", layout="wide")

# HEADER
st.title("🏁 F1 Pole Position Predictor")
st.markdown(
    "Select a circuit to view historical performance and predictions.\n\n"
    "Each circuit contains model-based qualifying analysis."
)

st.divider()

# CIRCUIT GRID

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3c/Silverstone_Circuit_map.png"
    )
    st.markdown("### Silverstone")
    st.write("High-speed, low downforce circuit analysis.")
    st.page_link("pages/Silverstone.py", label="Open Silverstone →")

with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/9/9e/Monaco_circuit.png"
    )
    st.markdown("### Monaco")
    st.button("Coming soon", disabled=True)

with col3:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/1/1e/Spa-Francorchamps.png"
    )
    st.markdown("### Spa")
    st.button("Coming soon", disabled=True)
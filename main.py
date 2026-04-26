import streamlit as st

st.set_page_config(page_title="F1 Predictor", layout="wide")

# HEADER
st.title("🏁 F1 Pole Position Predictor")
st.markdown("Select a circuit to view historical performance and predictions.")

st.divider()

# CIRCUIT BUTTONS (tiles style)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Silverstone_Circuit_map.png")
    if st.button("Silverstone"):
        st.switch_page("pages/Silverstone.py")

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9e/Monaco_circuit.png")
    st.button("Monaco (coming soon)", disabled=True)

with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1e/Spa-Francorchamps.png")
    st.button("Spa (coming soon)", disabled=True)
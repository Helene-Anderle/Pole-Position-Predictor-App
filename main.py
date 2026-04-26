import streamlit as st

st.set_page_config(page_title="F1 Predictor", layout="wide")

st.title("🏁 F1 Pole Position Predictor")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3c/Silverstone_Circuit_map.png")
    st.markdown("### Silverstone")

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9e/Monaco_circuit.png")
    st.markdown("### Monaco")

with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1e/Spa-Francorchamps.png")
    st.markdown("### Spa")
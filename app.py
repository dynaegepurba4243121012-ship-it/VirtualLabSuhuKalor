import streamlit as st

st.set_page_config(
    page_title="Virtual Lab Suhu dan Kalor",
    page_icon="🌡️",
    layout="wide"
)

st.title("🌡️ VIRTUAL LAB SUHU DAN KALOR")

st.write("Website Virtual Lab berhasil dijalankan!")

st.markdown("---")

st.header("Simulasi Suhu")

suhu = st.slider(
    "Atur suhu:",
    min_value=0,
    max_value=100,
    value=25
)

st.metric("Suhu", f"{suhu} °C")

st.success("Jika tulisan ini muncul, berarti Streamlit sudah berhasil.")

import streamlit as st

def show():
    st.markdown("<h1 class='title'>Bienvenido a Hitalyzer</h1>", unsafe_allow_html=True)
    st.markdown("Sube tu canción para analizar:")

    uploaded_file = st.file_uploader("Selecciona un archivo", type=["wav", "mp3", "flac"])

    if uploaded_file:
        st.success(f"Archivo cargado: {uploaded_file.name}")

import streamlit as st

def show_home():
    st.markdown(
        "<h1 style='color:#ff4b9e;'>Bienvenido a Hitalyzer</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "Sube una canción para analizar sus características acústicas y conocer su potencial de éxito.",
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader("📁 Sube un archivo de audio (.wav, .mp3)", type=["wav", "mp3"])

    if uploaded_file:
        st.success(f"Archivo cargado: {uploaded_file.name}")
        # Aquí puedes insertar el análisis posterior

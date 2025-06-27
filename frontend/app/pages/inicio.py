import streamlit as st
import requests
import json
import tempfile

API_URL = "http://127.0.0.1:8000/extract-audio-features"

def show_home():
    # Estilo del botón y fondo
    st.markdown("""
    <style>
    div.stButton > button {
        background-color: black !important;
        color: white !important;
        border-radius: 8px !important;
        border: 1px solid white !important;
        font-weight: bold;
        padding: 0.5rem 1.5rem;
    }
    div.stButton > button:hover {
        background-color: #222 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Título
    st.markdown("<h1 style='color:#ff4b9e;'>🎧 Bienvenido a Hitalyzer</h1>", unsafe_allow_html=True)
    st.markdown(
        "Sube una canción para analizar sus características acústicas.",
        unsafe_allow_html=True
    )

    # Uploader
    uploaded_file = st.file_uploader("📁 Sube un archivo de audio (.wav, .mp3)", type=["wav", "mp3"])

    if uploaded_file:
        st.success(f"Archivo cargado: {uploaded_file.name}")
        if st.button("🎵 Analizar canción"):
            with st.spinner("🔍 Estamos analizando tu canción..."):
                # Guardar archivo temporalmente
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                    tmp_file.write(uploaded_file.read())
                    tmp_file_path = tmp_file.name

                # Enviar a la API
                with open(tmp_file_path, "rb") as f:
                    files = {"file": (uploaded_file.name, f, uploaded_file.type)}
                    response = requests.post(API_URL, files=files)

                if response.status_code == 200:
                    st.success("✅ Análisis completado.")
                    response_data = response.json()
                    st.code(json.dumps(response_data, indent=2, ensure_ascii=False), language="json")
                else:
                    st.error(f"❌ Error en la API: {response.status_code}")

import streamlit as st
import requests
import json
import uuid
from google.cloud import storage
import os
import time
from streamlit_lottie import st_lottie

BUCKET_NAME = "hitalyzer-audio-files"
API_FEATURE_EXTRACTION = "https://hitalyzer-feature-extraction-417641910060.us-central1.run.app/extract-audio-features"
genres = ["rock", "pop", "electronic", "hip hop", "classical"]

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path_svg = os.path.join(parent_dir, "..", "assets", "HITSPELL.svg")
gif_path = os.path.join(parent_dir, "..", "assets", "HIT.gif")

def show_home():
    # Estilo del botón y fondo

    # Título y subtítulo
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(logo_path_svg, width=800)

    st.markdown("<hr style='margin-top: 10px; margin-bottom: 5px;'>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='text-align: center; margin-top: 5px; margin-bottom: 5px;'>HitSpell es un hechizo tecnológico diseñado</h3>",
        unsafe_allow_html=True
    )

    st.markdown("<hr style='margin-top: 5px; margin-bottom: 10px;'>", unsafe_allow_html=True)


    st.markdown("Sube tu canción y deja que la magia ocurra: nuestra herramienta analiza sus elementos sonoros -tempo, ritmo, energía, texturas y emociones- y los compara con miles de éxitos músicales del mismo género. A través de un modelo entrenados con cientos de miles de canciones, HitSpell predice la probabilidad de que tu canción se convierta en hit a partir de sus características de audio.")
    st.markdown("Pero no sólo se queda ahí. Cómo un oráculo musical, también te entrega recomendaciones concretas y personalizadas para afinar el hechizo: ajustes en tempo, mezcla, estructura o atmosfera emocional.")

    st.markdown(
        "<h2 style='text-align: center; margin-top: 5px; margin-bottom: 5px;'>¡CONJURA TU PRÓXIMO HIT!</h3>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    # --- Diseño con columnas ---
    st.markdown("""
    <style>
    /* El circulito seleccionado del radio */
    input[type="radio"]:checked + div:before {
        border-color: white !important;
        background-color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # 🧱 Layout horizontal limpio
    col1, col2 = st.columns([1, 3])

    with col1:
        st.markdown("🎵 <span style='color:white;font-weight:600;'>Género musical</span>", unsafe_allow_html=True)
        selected_genre = st.radio(
            "🎵 Género musical",
            genres,
            label_visibility="collapsed",
            horizontal=True
        )

    with col2:
        st.markdown("📁 <span style='color:white;font-weight:600;'>Sube un archivo de audio (.wav, .mp3)</span>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Uploader de audio (oculto)",
            type=["wav", "mp3"],
            label_visibility="collapsed",
            key="audio_file"
        )

    if uploaded_file:
        if st.button("🎵 Analizar canción"):

            try:
                # Subida a GCS
                client = storage.Client()
                bucket = client.bucket(BUCKET_NAME)
                unique_filename = f"{uuid.uuid4()}_{uploaded_file.name}"
                blob = bucket.blob(unique_filename)
                blob.upload_from_file(uploaded_file, content_type=uploaded_file.type)

                # Llamada API
                col1, col2 = st.columns([1, 4])

                gif_slot = col1.empty()
                status_slot = col2.empty()

                # Mostrar el GIF animado mientras carga
                gif_slot.image(gif_path, use_container_width=True)

                # Mensaje informativo mientras analiza
                status_slot.markdown("⏳ <b>Analizando tu canción... esto puede tardar hasta 2 minutos</b>", unsafe_allow_html=True)

                # Llamada a la API o procesamiento largo
                with st.spinner("Analizando características acústicas..."):
                    response = requests.post(API_FEATURE_EXTRACTION, json={"filename": unique_filename})


                # ✅ Mostrar resultados si todo sale bien
                if response.status_code == 200:
                    response_data = response.json()
                    response_data = {"genre": selected_genre, **response_data}

                    st.success("✅ Análisis completado con éxito")
                    st.code(json.dumps(response_data, indent=2, ensure_ascii=False), language="json")

                    # Bloque 1: Índice popularidad
                    st.markdown(f"""<div style='
                        text-align: center;
                        background: linear-gradient(135deg, #ff0080, #7928ca);
                        padding: 30px;
                        border-radius: 20px;
                        margin-top: 30px;
                        margin-bottom: 20px;
                        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
                    '>
                        <h1 style='color: white; font-size: 60px; margin: 0;'>🎯 87.35</h1>
                        <h3 style='color: white; margin: 0;'>Índice de popularidad estimado</h3>
                    </div>""", unsafe_allow_html=True)

                    # Bloque 2: Reporte animado
                    reporte_chatgpt = """Esta canción muestra un perfil acústico alineado con las tendencias actuales..."""
                    bloque = st.empty()
                    texto_mostrado = ""
                    for letra in reporte_chatgpt:
                        texto_mostrado += letra
                        bloque.markdown(f"""<div style='
                            background-color: #1e1e1e;
                            color: white;
                            padding: 25px;
                            border-radius: 12px;
                            font-size: 16px;
                            line-height: 1.6;
                            margin-top: 20px;
                            box-shadow: 0 2px 10px rgba(0,0,0,0.3);
                        '>
                            <h4 style='color: #f72585;'>📝 Análisis de potencial generado por inteligencia artificial</h4>
                            <p>{texto_mostrado}</p>
                        </div>""", unsafe_allow_html=True)
                        time.sleep(0.005)

                else:
                    st.error(f"❌ Error en la API: {response.status_code}")
                    st.code(response.text)

            except Exception as e:
                st.error(f"❌ Error durante el análisis: {e}")

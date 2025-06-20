import streamlit as st
import os
from PIL import Image
from pages import inicio  # importar más páginas aquí si las agregas

# Configuración de la app
st.set_page_config(page_title="Hitalyzer", layout="wide")

# Estilos personalizados
style_path = os.path.join(os.path.dirname(__file__), "styles.css")
with open(style_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Encabezado con logo y navbar
col1, col2 = st.columns([1, 8])
with col1:
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(Image.open(logo_path), width=80)
with col2:
    st.markdown(
        """
        <div class='navbar'>
            <a class='active'>Inicio</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Mostrar la página actual (en este caso solo Inicio)
inicio.show()

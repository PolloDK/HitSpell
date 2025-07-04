import streamlit as st

from pages import inicio
import os

# --- Rutas y configuración ---
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path_svg = os.path.join(parent_dir, "assets", "HITSPELL.svg")
favicon_path_svg = os.path.join(parent_dir, "assets", "logo.svg")

st.set_page_config(
    page_title="Hitalyzer",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon=favicon_path_svg
)

# --- Páginas internas ---
pages = {
    "Home": inicio.show_home,
}

st.markdown(f"""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}
#MainMenu, header, footer {{ visibility: hidden; }}

html, body, .stApp {{
    background: linear-gradient(to bottom, #000000, #ff4b9e);
    background-attachment: fixed;
}}

body, .stApp, .stMarkdown, p, span, div {{ color: white !important; }}
[data-testid="stMarkdownContainer"] svg {{ color: #ff4b9e !important; }}

section[data-testid="stFileUploader"] > div {{
    background-color: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid white !important;
    border-radius: 12px !important;
    padding: 1.25rem !important;
    box-shadow: 0 0 6px #ffffff44;
}}

/* Oculta el botón blanco nativo */
section[data-testid="stFileUploader"] input[type="file"] {{
    color: white !important;
    background-color: transparent !important;
    border: 1px solid white !important;
    border-radius: 6px;
    padding: 0.4rem 0.8rem;
    font-weight: bold;
    cursor: pointer;
}}

/* Ocultar completamente si prefieres zona full drop */
section[data-testid="stFileUploader"] > div div div div:nth-child(2) {{
    display: none !important;
}}

section[data-testid="stFileUploader"] div div {{
    background-color: transparent !important;
}}
section[data-testid="stFileUploader"] p {{
    color: white !important;
}}

hr {{
    border-top: 1px solid white !important;
    opacity: 1 !important;
}}

section[data-testid="stFileUploaderDropzone"] {{
    background-color: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid white !important;
    color: white !important;
}}
section[data-testid="stFileUploaderDropzone"] * {{
    color: white !important;
}}

div[data-testid="stHeader"] {{
    z-index: 0 !important;
}}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>
button[kind="primary"] {
    background-color: black !important;
    color: white !important;
    border-radius: 8px !important;
    border: 1px solid white !important;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
button[kind="primary"]:hover {
    background-color: #222 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Fondo oscuro para bloques de JSON */
pre {
    background-color: #111 !important;
    color: white !important;
    padding: 1rem !important;
    border-radius: 10px !important;
    font-size: 0.85rem !important;
    overflow-x: auto !important;
}
</style>
""", unsafe_allow_html=True)

# --- CSS personalizado ---
st.markdown("""
<style>
/* Aplica solo al primer selectbox visible */
div[data-testid="column"] > div:nth-of-type(1) > div {
    background-color: transparent !important;
    border: 1px solid white !important;
    border-radius: 8px !important;
    padding: 5px !important;
    height: 60px !important;
    color: white !important;
}

/* Texto dentro del select */
div[data-testid="column"] > div:nth-of-type(1) > div * {
    color: white !important;
}

/* Forzamos a aplicar estilo al dropdown */
div[role="listbox"] {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border-radius: 8px !important;
}

div[role="option"] {
    background-color: transparent !important;
    color: white !important;
}
div[role="option"]:hover {
    background-color: rgba(255, 255, 255, 0.1) !important;
}
</style>
""", unsafe_allow_html=True)

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

# --- Solución previa para conflictos de z-index (navbar desactivado ahora) ---
# st.markdown("""
# <style>
# nav[data-testid="stNavbar"] {
#     z-index: 999 !important;
#     position: relative !important;
# }
# section.main > div {
#     position: relative;
#     z-index: 1;
# }
# </style>
# """, unsafe_allow_html=True)

# --- Navbar desactivado ---
# from streamlit_navigation_bar import st_navbar
# styles = {...}
# options = {...}
# selected_page = st_navbar(...)
# pages[selected_page]()

# --- Mostrar página directamente ---
pages["Home"]()

# --- Footer ---
st.markdown("---")
col_logo, col_footer = st.columns([1, 4])

with col_logo:
    if os.path.exists(logo_path_svg):
        st.image(logo_path_svg, width=200)

with col_footer:
    st.markdown("""
    <div style="font-size: 0.9rem; color: white; text-align: left; padding-top: 0.5rem;">
        <p style="margin: 4px 0;">Hitspell © 2025</p>
        <p style="margin: 4px 0;">Desarrollado por Tremendo equipo</p>
    </div>
    """, unsafe_allow_html=True)

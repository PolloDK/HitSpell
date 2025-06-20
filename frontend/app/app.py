import streamlit as st
from streamlit_navigation_bar import st_navbar
from pages import inicio
import os

# --- Rutas y configuración ---
parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path_svg = os.path.join(parent_dir, "assets", "logo.svg")

st.set_page_config(
    page_title="Hitalyzer",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon=logo_path_svg
)

# --- Páginas internas ---
pages = {
    "Home": inicio.show_home,
}

# --- Estilos del navbar ---
styles = {
    "nav": {
        "background-color": "#111111",
        "justify-content": "flex-start",
        "align-items": "center",
        "gap": "1rem",
        "height": "60px",
        "padding": "0 2rem",
        "z-index": "10000"
    },
    "img": {
        "padding-right": "12px",
        "height": "38px",
    },
    "span": {
        "color": "#ff4b9e",
        "font-size": "16px",
        "padding": "14px",
        "font-weight": "bold",
        "transition": "background-color 0.3s ease, color 0.3s ease",
    },
    "active": {
        "background-color": "#ff4b9e",
        "color": "white",
        "font-weight": "bold",
        "height": "60px",
        "box-sizing": "border-box",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": False,
}

# --- Estilos globales ---
st.markdown(f"""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {{ display: none !important; }}
#MainMenu, header, footer {{ visibility: hidden; }}

html, body, .stApp {{
    background: linear-gradient(to bottom, #000000, #ff4b9e);
    background-attachment: fixed;
}}

.block-container {{
    margin-top: 2.75rem !important;
    color: white !important;
}}

nav {{
    position: fixed !important;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 10000 !important;
}}

nav span:hover {{
    background-color: #ff4b9e33 !important;
    color: white !important;
    cursor: pointer;
}}

body, .stApp, .stMarkdown, p, span, div {{ color: white !important; }}
[data-testid="stMarkdownContainer"] svg {{ color: #ff4b9e !important; }}

section[data-testid="stFileUploader"] > div {{
    background-color: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid #ff4b9e88 !important;
    border-radius: 12px !important;
    padding: 1.25rem !important;
    box-shadow: 0 0 6px #ff4b9e55;
}}
section[data-testid="stFileUploader"] div div {{
    background-color: transparent !important;
}}
section[data-testid="stFileUploader"] p {{
    color: #f0f0f0 !important;
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

# --- Navbar ---
selected_page = st_navbar(
    pages=list(pages.keys()),
    styles=styles,
    options=options,
    logo_path=logo_path_svg,
)

# --- Mostrar contenido de la página seleccionada ---
pages[selected_page]()

# --- Footer ---
st.markdown("---")
col_logo, col_footer = st.columns([1, 4])

with col_logo:
    if os.path.exists(logo_path_svg):
        st.image(logo_path_svg, width=80)

with col_footer:
    st.markdown("""
    <div style="font-size: 0.9rem; color: white; text-align: left; padding-top: 0.5rem;">
        <p style="margin: 4px 0;">Hitalyzer © 2025</p>
        <p style="margin: 4px 0;">
            Conecta con nosotros:
            <a href="https://www.linkedin.com/company/fkeconomics" target="_blank" style="color: #ff4b9e;">LinkedIn FK</a>
        </p>
        <p style="margin: 4px 0;">Desarrollado por Tremendo equipo</p>
    </div>
    """, unsafe_allow_html=True)

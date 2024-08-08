import streamlit as st
from Inicio import main as inicio_main
from main import main as main_main

st.set_page_config(

    page_title="Inicio",
    page_icon=":guardsman:",
    layout="wide",
    initial_sidebar_state="expanded"

)

# Agrega tus rutas aquí
pages = {
    "Inicio": inicio_main,
    "Recomendador de Alimentos": main_main,
}

# Selecciona la página en el menú desplegable
page = st.sidebar.selectbox("Selecciona una página", list(pages.keys()))

# Carga la página seleccionada
pages[page]()
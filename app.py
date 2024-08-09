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

# Inicializa la sesión
if "page" not in st.session_state:
    st.session_state.page = "Inicio"

# Crea botones en el sidebar
inicio_button = st.sidebar.button("Inicio")
recomendador_button = st.sidebar.button("Recomendador de Alimentos")

# Actualiza la página actual
if inicio_button:
    st.session_state.page = "Inicio"
elif recomendador_button:
    st.session_state.page = "Recomendador de Alimentos"

# Renderiza la página correspondiente
if st.session_state.page == "Inicio":
    inicio_main()
elif st.session_state.page == "Recomendador de Alimentos":
    main_main()
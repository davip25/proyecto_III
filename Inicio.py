import streamlit as st

st.set_page_config(
    page_title="Inicio",
)

st.write("# Sistema de Recomendación de Alimentos")

st.markdown(
    """
    Tienes dificultades para conocer que alimentos te pueden ayudar a alcanzar tus objetivos de un cuerpo
    sano? Esta aplicacion desarrollada con Inteligencia artifical te muestra recomendaciones segun
    tus caracteristicas fisicas especificas.
     
    Ha sido elaborado con Tecnologias de:
    Scikit-learn: Machine learning(NearestNeighbour y K-NearestNeighbour)
    Streamlit: Elaboracion de aplicación Web

    Puedes Enconytrar mas detalles en el repositorio [GitHub](https://github.com/davip25/proyecto_III).
    """
)
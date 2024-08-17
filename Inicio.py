import streamlit as st
from load import load_images


def main():
    images = load_images()

    st.markdown("<div style='text-align: center'><h1>👋 Bienvenido a  Sistema de Recomendación de Alimentos</h1></div>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center'>"

            "🤔 Tienes dificultades para conocer que alimentos te pueden ayudar a alcanzar tus objetivos de un cuerpo sano? <br>"

           "😆 Esta aplicacion desarrollada con Inteligencia artifical te muestra recomendaciones segun tus caracteristicas fisicas especificas."

           "</div>", unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image(images[0])

    st.markdown(" ")
    st.markdown(" ") # Agrega una linea vacia para separar

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(images[1])
        st.write("🤓 Ha sido elaborado con Tecnologias de: Scikit-learn: Machine learning(NearestNeighbour y K-NearestNeighbour) Streamlit: Elaboracion de aplicación Web.")
        
    with col2:
        st.write("🧐 Aqui puedes encontrar la fuente de datos en [Kaggle](https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset).")
        st.image(images[2]) 

    with col3:
        st.image(images[3])
        st.write("👨‍💻 Puedes encontrar más detalles en el repositorio de [Github](https://github.com/davip25/proyecto_III)")
        
        

if __name__ == "__main__":

    main()

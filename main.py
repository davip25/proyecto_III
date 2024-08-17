import pandas as pd
import streamlit as st
import streamlit_echarts
import random
from random import uniform as rnd
from streamlit_echarts import st_echarts
from load import load
from Persona import Persona
from recomendador_alimento import Recomendacion
from display import display_header, display_form, display_user_data, display_calculated_data, display_recommendations

def main():
    display_header("Recomendador de Alimentos")

    # Crear el formulario
    edad, altura, peso, genero, actividad, objetivo_comidas, cant_comidas, submit_button = display_form()

    persona = Persona(edad, altura, peso, genero, actividad, objetivo_comidas, cant_comidas)

    # Mostrar los datos ingresados
    if submit_button:
        datos_usuario = {
            "edad": edad,
            "altura": altura,
            "peso": peso,
            "genero": genero,
            "actividad": actividad,
            "objetivo_comidas": objetivo_comidas,
            "cant_comidas": cant_comidas
        }

        # Cargar datos de alimentos
        scaler, nneigh, food_names, caloric_values, fats, carbohydrates, proteins, sugars = load()

        # Crear recomendador
        recomendador = Recomendacion(scaler, nneigh, food_names, caloric_values, fats, carbohydrates, proteins, sugars)

        # Mostrar datos del usuario
        display_user_data(persona)

        # Mostrar datos calculados
        display_calculated_data(persona)

        # Generar recomendaciones
        with st.spinner("Generando recomendaciones..."):

            valores_aleatorios = persona.generar_valores_aleatorios()
            recomendaciones = recomendador.generar_recomendaciones(*valores_aleatorios)

        # Mostrar recomendaciones
        st.success("✅ Recomendaciones generadas correctamente! ")
        display_recommendations(recomendaciones)

        # Almacena el estado de la sesión
        st.session_state.recomendaciones = recomendaciones

if __name__ == "__main__":
    main()

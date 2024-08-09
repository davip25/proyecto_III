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

        persona = Persona(datos_usuario['edad'],
                          datos_usuario['altura'],
                          datos_usuario['peso'],
                          datos_usuario['genero'],
                          datos_usuario['actividad'],
                          datos_usuario['objetivo_comidas'],
                          datos_usuario['cant_comidas']
                          )

        scaler, nneigh,  food_names, caloric_values, fats, carbohydrates, proteins, sugars = load()

        recomendador = Recomendacion(scaler, nneigh,  food_names, caloric_values, fats, carbohydrates, proteins, sugars)

        valores_aleatorios = persona.generar_valores_aleatorios()
        recomendaciones = recomendador.generar_recomendaciones(*valores_aleatorios)
        
        display_user_data(persona)
        display_calculated_data(persona)
        display_recommendations(recomendaciones)

if __name__ == "__main__":
    main()

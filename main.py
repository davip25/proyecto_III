import pandas as pd
import streamlit as st
import streamlit_echarts
import random
from random import uniform as rnd
from streamlit_echarts import st_echarts
import joblib
import numpy as np
from load import load
from Persona import Persona
from recomendador_alimento import Recomendacion

def main():
    st.title("Recomendador de Alimentos")

    # Crear el formulario
    with st.form(key='user_form'):
        edad = st.number_input("Edad", min_value=0, max_value=120, step=1, value=10)
        altura = st.number_input("Altura (cm)", min_value=1.0, max_value=300.0, step=1.0, value=150.0)
        peso = st.number_input("Peso (kg)", min_value=1.0, max_value=500.0, step=1.0, value=50.0)

        genero = st.selectbox("Género", options=["Masculino", "Femenino"])

        actividad = st.selectbox("Nivel de Actividad", options=[
            'Sedentario',
            'Ligeramente activo (1-3 días/semana)',
            'Moderadamente activo (3-5 días/semana)',
            'Muy activo (6-7 días/semana)',
            'Extra activo'
        ])

        objetivo_comidas = st.selectbox("Objetivo de Comidas", options=[
            "Pérdida de peso",
            "Mantenimiento",
            "Ganancia de Masa Muscular"
        ])

        cant_comidas = st.number_input("Cantidad de Alimentos por día", min_value=1, max_value=10, step=1)

        submit_button = st.form_submit_button(label='Calcular')

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

        scaler, nneigh,  food_names = load()

        recomendador = Recomendacion(scaler, nneigh,  food_names)

        valores_aleatorios = persona.generar_valores_aleatorios()
        recomendaciones = recomendador.generar_recomendaciones(*valores_aleatorios)
        
        st.write("### Datos Ingresados")
        st.write(f"**Edad:** {persona.edad} años")
        st.write(f"**Altura:** {persona.altura} cm")
        st.write(f"**Peso:** {persona.peso} kg")
        st.write(f"**Género:** {persona.genero}")
        st.write(f"**Nivel de Actividad:** {persona.actividad}")
        st.write(f"**Objetivo de Comidas:** {persona.objetivo_comidas}")
        st.write(f"**Cantidad de Comidas por Día:** {persona.cant_comidas}")

        st.write("### Datos Calculados")
        st.write(f"**Índice de Masa Corporal:** {persona.calculo_imc()}")
        st.write(f"**Tasa Metabólica Basal:** {persona.calcular_tmb()}")
        st.write(f"**Ingesta de Calorias diarias recomendadas:** {persona.calculador_calorias()}")
        st.write(f"**Distribución de Macronutrientes:** {persona.distribuir_macronutrientes()}")

        
        st.write("### Recomendaciones")
        st.write(recomendaciones)


if __name__ == "__main__":
    main()

import pandas as pd
import streamlit as st
import streamlit_echarts
import random
from modules.ml_func import *
from random import uniform as rnd
from streamlit_echarts import st_echarts
import joblib

st.set_page_config(page_title="Recomendador de Alimentos", page_icon="🍎", layout="wide")

# Función para generar valores aleatorios que sumen un total específico
def random_values(total, n):
    values = []
    for _ in range(n - 1):
        value = random.uniform(0, total)
        values.append(value)
        total -= value
    values.append(total)
    random.shuffle(values)
    return values


class Persona:

    def __init__(self, edad, altura, peso, genero, actividad, objetivo_comidas, cant_comidas):
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.actividad = actividad
        self.objetivo_comidas = objetivo_comidas
        self.cant_comidas = cant_comidas

    def calculo_imc(self):
        imc = round(self.peso / ((self.altura / 100) ** 2), 2)
        return imc

    def mostrar_resultados(self):
        imc = self.calculo_imc()
        imc_texto = f'{imc} kg/m²'
        if imc < 18.5:
            categoria = 'Bajo Peso'
            color = 'Red'
        elif 18.5 <= imc < 24.9:
            categoria = 'Normal'
            color = 'Green'
        elif 24.9 <= imc < 29.9:
            categoria = 'Sobre Peso'
            color = 'Yellow'
        else:
            categoria = 'Obesidad'
            color = 'Red'
        return imc_texto, categoria, color

    def calcular_tmb(self):
        if self.genero == 'Masculino':
            tmb = 10 * self.peso + 6.25 * self.altura - 5 * self.edad + 5
        else:
            tmb = 10 * self.peso + 6.25 * self.altura - 5 * self.edad - 161
        return tmb

    def calculador_calorias(self):
        actividad = ['Sedentario',
                     'Ligeramente activo (1-3 días/semana)',
                     'Moderadamente activo (3-5 días/semana)',
                     'Muy activo (6-7 días/semana)',
                     'Extra activo']
        valores_actividad = [1.2, 1.375, 1.55, 1.725, 1.9]
        valor_actividad = valores_actividad[actividad.index(self.actividad)]
        calorias_diarias = self.calcular_tmb() * valor_actividad

        # Ajuste según objetivo
        if self.objetivo_comidas == 1:
            # Ganar Masa Muscular
            calorias_diarias += 500
        elif self.objetivo_comidas == 2:
            # Perder Peso
            calorias_diarias -= 500

        return calorias_diarias

    def distribuir_macronutrientes(self):
        calorias_diarias = self.calculador_calorias()

        if self.objetivo_comidas == 1 or self.objetivo_comidas == 2:
            # Ganar Masa Muscular o Perder Peso
            proteinas_diarias = self.peso * 2
            calo_proteinas_diarias = proteinas_diarias * 4

            grasas_diarias = self.peso * 0.8
            calo_grasas_diarias = grasas_diarias * 9

            calo_carbohidratos_diarias = calorias_diarias - (calo_grasas_diarias + calo_proteinas_diarias)
            carbohidratos_diarios = calo_carbohidratos_diarias / 4

        else:
            # Mantener tu peso
            proteinas_diarias = self.peso * 1.8
            calo_proteinas_diarias = proteinas_diarias * 4

            grasas_diarias = self.peso * 0.8
            calo_grasas_diarias = grasas_diarias * 9

            calo_carbohidratos_diarias = calorias_diarias - (calo_grasas_diarias + calo_proteinas_diarias)
            carbohidratos_diarios = calo_carbohidratos_diarias / 4

        azucares = calorias_diarias * 0.05
        return azucares, proteinas_diarias, calo_proteinas_diarias, grasas_diarias, calo_grasas_diarias, calo_carbohidratos_diarias, carbohidratos_diarios

    

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
        
        """
        #Falta hacer esta Parte terminar de organizarlo para sacar los valores aleatorios
        
        azucares, proteinas_diarias, calo_proteinas_diarias, grasas_diarias, calo_grasas_diarias, calo_carbohidratos_diarias, carbohidratos_diarios = persona.distribuir_macronutrientes()
        # Cargar el modelo y el scaler
        nneigh = joblib.load('nearest_neighbors_model.pkl')
        scaler = joblib.load('scaler.pkl')


        # Generar valores aleatorios para cada variable
        caloric_values = random_values(persona.total_calories, persona.cant_alimentos)
        fats = random_values(grasas_diarias, persona.cant_alimentos)  
        carbohydrates = random_values(carbohidratos_diarios, persona.cant_alimentos)  # Ejemplo: 300 gramos de carbohidratos totales
        proteins = random_values(proteinas_diarias, persona.cant_alimentos)  # Ejemplo: 150 gramos de proteínas totales
        sugars = random_values(azucares, persona.cant_alimentos) 

        """
        
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
        st.write(f"**Distribucion de Macronutrientes:** {persona.distribuir_macronutrientes()}")
        st.write(f"**Recomendaciones:** {persona.generar_recommendaciones()}")

        

if __name__ == "__main__":
    main()

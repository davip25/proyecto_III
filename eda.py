import subprocess
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
from math import sqrt
from unidecode import unidecode
import os
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
...

def eda_app():

    # Configuracion Especial de Pandas
    # Elimina los limites para mostrar columnas en Pandas
    pd.set_option('display.max_columns', None)

    # Lectura de archivos.csv
    data_1 = pd.read_csv("C:\\Users\\Sora\\Desktop\\Clove\\proyecto_III\\sources\\FOOD-BEBIDAS.csv")
    data_2 = pd.read_csv("C:\\Users\\Sora\\Desktop\\Clove\\proyecto_III\\sources\\FOOD-COMUNES.csv")
    data_3 = pd.read_csv("C:\\Users\\Sora\\Desktop\\Clove\\proyecto_III\\sources\\FOOD-FRUTAS.csv")
    data_4 = pd.read_csv("C:\\Users\\Sora\\Desktop\\Clove\\proyecto_III\\sources\\FOOD-PESCADOS.csv")
    data_5 = pd.read_csv("C:\\Users\\Sora\\Desktop\\Clove\\proyecto_III\\sources\\FOOD-POSTRES.csv")

    #Compilacion de dataframes
    data_compilada = pd.concat([data_1, data_2, data_3, data_4, data_5], ignore_index=True)
    data_compilada


    # ## EDA
    # ### (Exploratory Data Analysis)

    # Exploración Inicial de los Datos
    ## Verificacion de los nombres de las columnas y sus tipos de datos
    print(data_compilada.dtypes)

    # Se eliminan las primeras dos filas ya que no aportan informacion mas que el previo indice
    data_compilada = data_compilada.drop(data_compilada.columns[[0, 1]], axis=1)
    data_compilada

    data_compilada.info()

    # ### Limpieza de nombres de Columnas
    # - Limpieza de los nombres de las columnas, se creo una funcion que elimana los espacios en blanco al principio y al final, cambia el texto de mayusculas a minusculas, sustituye espacios en blanco por '_', elimina todos los acentos del

    def limpiar_columnas(nombre):
        nombre = nombre.strip() #Elimina espacios en blanco al principio y al final
        nombre = nombre.replace(' ','_') #Reemplaza espacios en blanco con guiones bajos
        nombre = unidecode(nombre) #Elimina todos los acentos
        nombre = nombre.lower() #Transforma en minuscula todos los nombres de series
        return nombre

    data_compilada.columns = data_compilada.columns.map(limpiar_columnas)
    data_compilada = data_compilada.copy()
    df_test = data_compilada.copy()
    data_compilada


    # ### Traduccion de Columna food
    # La aplicación es en español y los resultados deben ser traducidos

    # Crear el objeto traductor
    traductor = GoogleTranslator(source='en', target='es')

    # Función para traducir con manejo de errores
    def traducir_texto(text):
            translated_text = traductor.translate(text)
            return translated_text


    # Traducir la columna 'food'
    data_compilada['food'] = data_compilada['food'].apply(traducir_texto)

    print(data_compilada)

    # In[12]:


    # Exploración Inicial de los Datos
    ## Primeras 40 columnas
    data_compilada.head(40)


    # In[13]:


    ## Ultimas 40 filas
    data_compilada.tail(40)


    # In[14]:


    ## Registros Random
    data_compilada.iloc[40:-40].sample(40)


    # In[ ]:


    ### Faltan Graficas


    # In[ ]:





    # In[18]:


    # Obtener el directorio actual de trabajo
    directorio_actual = os.getcwd()

    # Ruta del archivo en el directorio actual
    ruta_archivo = os.path.join(directorio_actual, "data_compilada.csv")

    # Guardar el dataframe en un archivo CSV, sustituyendo si ya existe
    data_compilada.to_csv(ruta_archivo, index=False)

    print(f"Archivo guardado en {ruta_archivo}")


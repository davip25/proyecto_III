import pandas as pd
import joblib
import os
import streamlit as st

def load():
    sources = 'sources'
    
    # Cargar scaler
    scaler_path = os.path.join(sources, 'scaler.pkl')
    scaler = joblib.load(scaler_path)

        # Cargar modelo de nearest neighbors
    nneigh_path = os.path.join(sources, 'nearest_neighbors_model.pkl')
    nneigh = joblib.load(nneigh_path)

    # Cargar nombres de alimentos
    data_compilada_path = os.path.join(sources, 'data_compilada.csv')
    data_compilada = pd.read_csv(data_compilada_path)
    food_names = data_compilada['food'].values
    caloric_values = data_compilada['caloric_value'].values
    fats = data_compilada['fat'].values
    carbohydrates = data_compilada['carbohydrates'].values
    proteins = data_compilada['protein'].values
    sugars = data_compilada['sugars'].values

    return scaler, nneigh, food_names, caloric_values, fats, carbohydrates, proteins, sugars

def load_images():

    images = []
    images.append(os.path.join("sources", "alimentos.jpeg"))
    images.append(os.path.join("sources", "scikit_learn_logo.png"))
    images.append(os.path.join("sources", "kaggle_logo.png"))
    images.append(os.path.join("sources", "github_logo.png"))

    return images
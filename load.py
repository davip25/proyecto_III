import pandas as pd
import joblib
import os

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

    return scaler, nneigh,  food_names
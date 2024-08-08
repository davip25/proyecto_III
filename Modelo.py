import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import pandas as pd

class Modelo:
    def __init__(self, data_compilada):
        self.data_compilada = data_compilada
        self.X = self.data_compilada.drop(['food', 'saturated_fats',
                                          'monounsaturated_fats', 'polyunsaturated_fats',
                                          'dietary_fiber', 'cholesterol', 'sodium', 'water',
                                          'vitamin_a', 'vitamin_b1', 'vitamin_b11', 'vitamin_b12', 'vitamin_b2',
                                          'vitamin_b3', 'vitamin_b5', 'vitamin_b6', 'vitamin_c', 'vitamin_d',
                                          'vitamin_e', 'vitamin_k', 'calcium', 'copper', 'iron', 'magnesium',
                                          'manganese', 'phosphorus', 'potassium', 'selenium', 'zinc',
                                          'nutrition_density'], axis=1).values
        self.food_names = self.data_compilada['food'].values
        self.scaler = StandardScaler()
        self.X_scaled = self.scaler.fit_transform(self.X)
        self.nneigh = NearestNeighbors(metric='cosine', algorithm='brute')
        self.nneigh.fit(self.X_scaled)
        joblib.dump(self.nneigh, 'nearest_neighbors_model.pkl')
        joblib.dump(self.scaler, 'scaler.pkl')
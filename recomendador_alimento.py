import numpy as np

class Recomendacion:
    def __init__(self, scaler, nneigh, food_names):
        self.scaler = scaler
        self.nneigh = nneigh
        self.food_names = food_names

    def generar_recomendaciones(self, caloric_values, fats, carbohydrates, proteins, sugars):
        input_values = np.array([caloric_values, fats, carbohydrates, proteins, sugars]).T
        input_scaled = self.scaler.transform(input_values)
        distances, indices = self.nneigh.kneighbors(input_scaled, n_neighbors=5)
        recommended_foods = self.food_names[indices]
        return recommended_foods
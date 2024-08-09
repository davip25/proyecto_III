import numpy as np

class Recomendacion:
    def __init__(self, scaler, nneigh, food_names, caloric_values, fats, carbohydrates, proteins, sugars):
        self.scaler = scaler
        self.nneigh = nneigh
        self.food_names = food_names
        self.caloric_values = caloric_values
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.proteins = proteins
        self.sugars = sugars

    def generar_recomendaciones(self, caloric_values, fats, carbohydrates, proteins, sugars):
        input_values = np.array([caloric_values, fats, carbohydrates, proteins, sugars]).T
        input_scaled = self.scaler.transform(input_values)
        distances, indices = self.nneigh.kneighbors(input_scaled, n_neighbors=10)
        recommended_foods = self.food_names[indices]
        Calorias = self.caloric_values[indices]
        Grasas = self.fats[indices]
        Carbohidratos = self.carbohydrates[indices] 
        Proteinas = self.proteins[indices] 
        Azucares = self.sugars[indices]
        return recommended_foods, Calorias, Grasas, Carbohidratos, Proteinas, Azucares
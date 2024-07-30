import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

pd.set_option('display.max_columns', None)
data=pd.read_csv('../proyecto_III/sources/FOOD-PESCADOS.csv')
print(data)

features = ['Caloric Value', 'Fat', 'Saturated Fats', 'Monounsaturated Fats', 'Polyunsaturated Fats',
            'Carbohydrates', 'Sugars', 'Protein', 'Dietary Fiber', 'Cholesterol', 'Sodium', 'Water',
            'Vitamin A', 'Vitamin B1', 'Vitamin B11', 'Vitamin B12', 'Vitamin B2', 'Vitamin B3',
            'Vitamin B5', 'Vitamin B6', 'Vitamin C', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Calcium',
            'Copper', 'Iron', 'Magnesium', 'Manganese', 'Phosphorus', 'Potassium', 'Selenium', 'Zinc']

X = data[features].values
food_names = data['food'].values

# Normalizar datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar modelo
neigh = NearestNeighbors(metric='cosine', algorithm='brute')
neigh.fit(X_scaled)

# Hacer recomendaciones
food_index = 0  # Índice del alimento para el cual quieres recomendaciones
distances, indices = neigh.kneighbors([X_scaled[food_index]], n_neighbors=5)

# Mostrar recomendaciones
recommended_foods = [food_names[i] for i in indices[0]]
print("Recomendaciones para", food_names[food_index], ":", recommended_foods)


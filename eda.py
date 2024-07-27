import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Downloads\dataset.csv", nrows=1)  # Read first 100 rows
print(df.head())

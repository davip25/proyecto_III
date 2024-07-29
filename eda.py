import pandas as pd

data=pd.read_parquet(r"C:\Users\HP\Downloads\archive (3)\recipes.parquet")
print(data.head())

print(data.info())

print('hola')

data.tail(10)

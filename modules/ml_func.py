import os
import pandas as pd
import pickle
import sklearn
import base64


def read_data():
    os.chdir(r"C:\Users\HP\Desktop\FORMACION\HackaBoss Data Scienct AI\proyecto_III\sources")
    csv_file = pd.read_csv("../data_compilada.csv", encoding="latin1", header = 1)
    
    return csv_file


def load_pkls():
    os.chdir(r"C:\Users\HP\Desktop\FORMACION\HackaBoss Data Scienct AI\proyecto_III\sources")

    with open(file = "nearest_neighbors_model.pkl", mode="rb") as file:
        nneigh = pickle.load(file)

    with open(file = "scaler.pkl", mode="rb") as file:
        scaler = pickle.load(file)

    return nneigh, scaler  


def download_file(df):

    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f"<a href='data:file/csv;base64,{b64}' download='data_compilada.csv'>Download CSV File</a>"

    return href

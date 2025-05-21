import pandas as pd

# Dataframes es la información básica con el nombre de las piezas y centímetros para poder

data = {
    "Piezas": ["Pata", "Tablerao", "Puerta", "Estante", "Panel Lateral"],
    "Centímetros": [40, 120, 30, 30, 180],   
}

df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Excel

df.to_excel("Muebles_medidas.xlsx", index=False)
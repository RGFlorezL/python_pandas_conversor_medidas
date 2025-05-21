import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo Excel:
df = pd.read_excel("Muebles_medidas.xlsx")

# Añadir una columna al Dataframe que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Pulgadas"] = df["Centímetros"].apply(cm_a_pulgadas)

df.to_excel("Muebles_medidas_convertidas.xlsx", index=False)

print("Conversión completada y guardada en un archivo llamado 'Muebles_medidas_convertidas.xlsx'")
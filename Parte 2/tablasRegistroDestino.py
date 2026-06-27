import pandas as pd

df = pd.read_csv("../muestra2000.csv")

frecuencia_abs = df["Destino"].value_counts().sort_index()

# Frecuencia relativa
frecuencia_rel = df["Destino"].value_counts(normalize=True).sort_index()

# Crear la tabla
tabla_frecuencias = pd.DataFrame({
    "Frecuencia absoluta": frecuencia_abs,
    "Frecuencia relativa": frecuencia_rel
})

print(tabla_frecuencias)
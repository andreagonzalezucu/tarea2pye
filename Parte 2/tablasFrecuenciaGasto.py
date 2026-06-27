import pandas as pd

muestra = pd.read_csv("../muestra2000.csv")

# Crear los intervalos
intervalos = pd.cut(muestra["GastoTotal"], bins=10)

# Tabla de frecuencias
fa = intervalos.value_counts().sort_index()

tabla = pd.DataFrame()
tabla["Intervalo"] = fa.index.astype(str)
tabla["Frecuencia absoluta"] = fa.values
tabla["Frecuencia relativa"] = (fa.values / len(muestra)).round(4)
tabla["Frecuencia relativa acumulada"] = tabla["Frecuencia relativa"].cumsum().round(4)

# Marca de clase
tabla["Marca de clase"] = [
    round((i.left + i.right) / 2, 2)
    for i in fa.index
]

print(tabla)
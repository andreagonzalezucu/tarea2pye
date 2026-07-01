import pandas as pd 
from scipy.stats import chi2_contingency 

# leemos la muestra
muestra = pd.read_csv("muestra2000.csv")

tabla_contingencia = pd.crosstab(
    muestra["Estadia"],
    muestra["Lugar Salida"]
)

chi2, p_valor, grados_libertad, frecuencias_esperadas = chi2_contingency(tabla_contingencia)

print("Resultados test Chi-Cuadrado")
print("Estadístico Chi-Cuadrado:", chi2)
print("p-valor:", p_valor)
print("Grados de libertad:", grados_libertad)

# guardamos la tabla de contingencia
tabla_contingencia.to_csv("tabla_contingencia_estadia_lugarsalida.csv")
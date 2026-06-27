import pandas as pd
import matplotlib.pyplot as plt

# Leer la muestra
muestra = pd.read_csv("../muestra2000.csv")

# Boxplot
plt.figure(figsize=(8,6))

plt.boxplot(muestra["GastoTotal"], vert=True)

plt.title("Diagrama de cajas de Gasto Total")
plt.ylabel("Gasto Total")

plt.tight_layout()

plt.savefig("boxplotGastoTotal.png", dpi=300, bbox_inches="tight")
plt.close()

# Cuartiles
q1 = muestra["GastoTotal"].quantile(0.25)
mediana = muestra["GastoTotal"].median()
q3 = muestra["GastoTotal"].quantile(0.75)

# Rango intercuartílico
ric = q3 - q1

print("Primer cuartil (Q1):", round(q1, 2))
print("Mediana:", round(mediana, 2))
print("Tercer cuartil (Q3):", round(q3, 2))
print("Rango intercuartílico (RIC):", round(ric, 2))

limite_inferior = q1 - 1.5 * ric
limite_superior = q3 + 1.5 * ric

atipicos = muestra[
    (muestra["GastoTotal"] < limite_inferior) |
    (muestra["GastoTotal"] > limite_superior)
]

print("Cantidad de datos atípicos:", len(atipicos))
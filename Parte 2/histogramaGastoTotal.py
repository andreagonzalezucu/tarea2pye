import pandas as pd
import matplotlib.pyplot as plt

# Leer la muestra
muestra = pd.read_csv("../muestra2000.csv")

# Histograma
plt.figure(figsize=(10,6))

plt.hist(
    muestra["GastoTotal"],
    bins=10,
    edgecolor="black"
)

plt.title("Histograma de Gasto Total")
plt.xlabel("Gasto Total")
plt.ylabel("Frecuencia")

plt.tight_layout()

plt.savefig("histogramaGastoTotal.png", dpi=300, bbox_inches="tight")
plt.close()
import pandas as pd
import matplotlib.pyplot as plt

# Leer la muestra
muestra = pd.read_csv("../muestra2000.csv")

# Diagrama de dispersión
plt.figure(figsize=(8,6))

plt.scatter(
    muestra["Gente"],
    muestra["GastoTotal"]
)

plt.title("Diagrama de dispersión: Gente vs Gasto Total")
plt.xlabel("Cantidad de personas (Gente)")
plt.ylabel("Gasto Total")

plt.tight_layout()

plt.savefig("dispersionGenteGastos.png", dpi=300, bbox_inches="tight")
plt.close()
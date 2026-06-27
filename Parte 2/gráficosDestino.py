import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../muestra2000.csv")

# Frecuencias de la variable Destino
frecuencia = df["Destino"].value_counts()

# Gráfico de barras
plt.figure(figsize=(10,6))
frecuencia.plot(kind="bar")
plt.title("Frecuencia de destinos")
plt.xlabel("Destino")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=300, bbox_inches="tight")
plt.close()

plt.figure(figsize=(8,8))
frecuencia.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Distribución de destinos")
plt.ylabel("")  # Oculta la etiqueta del eje Y
plt.tight_layout()
plt.savefig("grafico_circular.png", dpi=300, bbox_inches="tight")
plt.close()
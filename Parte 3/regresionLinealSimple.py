import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# leemos la muestra
muestra = pd.read_csv("muestra2000.csv")

x = muestra["Gente"]
y = muestra["GastoTotal"]

resultado = linregress(x, y)

pendiente = resultado.slope
intercepto = resultado.intercept
r = resultado.rvalue
r2 = r ** 2
p_valor_regresion = resultado.pvalue

print("\nResultados Regresión Lineal Simple")
print("Intercepto:", intercepto)
print("Pendiente:", pendiente)
print("Coeficiente de correlación r:", r)
print("Coeficiente de determinación R²:", r2)
print("p-valor:", p_valor_regresion)


# grafico de dispersion con recta de regresion
plt.figure(figsize=(8, 6))
plt.scatter(x, y)

plt.plot(
    x,
    intercepto + pendiente * x
)

plt.title("Regresion lineal simple: Gente vs GastoTotal")
plt.xlabel("Cantidad de personas (Gente)")
plt.ylabel("GastoTotal")
plt.tight_layout()
plt.savefig("regresion_gente_gastototal.png", dpi=300, bbox_inches="tight")
plt.close()




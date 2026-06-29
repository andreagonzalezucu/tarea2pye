import pandas as pd
from scipy.stats import ttest_rel

muestra = pd.read_csv("muestra2000.csv")

alimentacion = muestra["GastoAlimentacion"]
compras = muestra["GastoCompras"]

estadistico, p_bilateral = ttest_rel(
    alimentacion,
    compras
)

if estadistico > 0:
    p_valor = p_bilateral / 2
else:
    p_valor = 1 - p_bilateral / 2

print("Estadistico t:", estadistico)
print("p-valor:", p_valor)

alpha = 0.05

if p_valor < alpha:
    print("Se rechaza H0")
else:
    print("No se rechaza H0")
import pandas as pd
from scipy.stats import ttest_1samp

muestra = pd.read_csv("muestra2000.csv")

datos = muestra["GastoAlojamiento"]

estadistico, p_bilateral = ttest_1samp(
    datos,
    popmean=350
)

if estadistico < 0:
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
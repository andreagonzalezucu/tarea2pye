import pandas as pd
import numpy as np
from scipy.stats import t

muestra = pd.read_csv("muestra2000.csv")

variables = [
    "GastoAlojamiento",
    "GastoAlimentacion",
    "GastoTransporteInternac",
    "GatoTransporteLocal",
    "GastoCultural",
    "GastoTours",
    "GastoCompras",
    "GastoResto"
]

nivel_confianza = 0.95

resultados = []

for variable in variables:

    datos = muestra[variable]

    n = len(datos)
    media = datos.mean()
    desviacion = datos.std(ddof=1)

    valor_t = t.ppf(
        1 - (1 - nivel_confianza) / 2,
        df=n - 1
    )

    margen_error = valor_t * desviacion / np.sqrt(n)

    limite_inferior = media - margen_error
    limite_superior = media + margen_error

    resultados.append({
        "Variable": variable,
        "Media": round(media, 2),
        "Desv. Est.": round(desviacion, 2),
        "IC Inferior": round(limite_inferior, 2),
        "IC Superior": round(limite_superior, 2)
    })

tabla_ic = pd.DataFrame(resultados)

print(tabla_ic)
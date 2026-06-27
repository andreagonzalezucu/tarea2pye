import pandas as pd

df = pd.read_csv("emisivo.csv")

muestra = df.sample(n=2000, random_state=42)

muestra.to_csv("muestra2000.csv", index=False)

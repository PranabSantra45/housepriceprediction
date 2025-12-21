import pandas as pd

df = pd.read_csv("data/housingdata.csv")
print("Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 rows:")
df.head
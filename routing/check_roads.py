import pandas as pd

roads = pd.read_csv("datasets/roads.csv")

print(roads.head())
print("\nTotal rows:", len(roads))
print("\nColumns:")
print(roads.columns)
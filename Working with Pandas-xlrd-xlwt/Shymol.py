import pandas as pd
import csv

df = pd.read_csv('shymolThesis.csv')
#df = df.fillna("uuuu")
flights = df.dropna()
print(df)
print(flights)

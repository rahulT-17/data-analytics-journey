# These all syntax are used to understand the DataSet
import pandas as pd 
df = pd.read_csv("expense.csv")

print("\nHEAD")
print(df.head())

print("\nTAIL")
print(df.tail())

print("\nINFO")
df.info()

print("\nDESCRIBE")
print(df.describe())

print("\nDTYPES")
print(df.dtypes)

# In this lesson we are gonna learn : 1. How to rename columns.
# 2. Create derived columns.

import pandas as pd 

df = pd.read_csv("employee_expense.csv")
print(df)
# SYNTAX : for renaming columns 
df = df.rename(columns={
    "employee_id" : "emp_id" , 
    "department" : "dept"
})
print(df.columns)

# Getting derived columns :
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df["year"] = df["date"].dt.year

print(df["month"],df["year"])
import pandas as pd 

# creating a dataframe and reading the csv file 
df = pd.read_csv("employee_expense.csv")
#print(df)

# Filling Numeric data that is missing with zero
#print(df.isna())

df["amount"] = df["amount"].fillna(0)

#print(df["amount"])

# cleaning text data ie category and department 
df["category"] = df["category"].str.strip().str.title()
df["department"] = df["department"].str.strip().str.title()

# printing the cleaned txt data 
#print(df["category"])
#print(df["department"])

# Filtering data :
# here we are filtering by food 
food_expense = df[df["category"]== "Food"]

#print(food_expense)

# Also we are checking expense > 500 :
high_expense = df[df["amount"]>500] 
#print(high_expense)

# Here we are gonna GROUPBY : categorie wise total

category_summary = df.groupby("category")["amount"].sum()
#print(category_summary)

# Here we are gonna GROUPBY : department-wise 

dept_wise = df.groupby("department")["amount"].sum().sort_values(ascending=False)
#print(dept_wise)

# NOW we are gonna do TIME-BASED ANALYSIS : by month
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

monthly_summary = df.groupby("month")["amount"].sum()
#print(monthly_summary)

monthly_dept_summ = df.groupby("department")["month"]
print(monthly_dept_summ)
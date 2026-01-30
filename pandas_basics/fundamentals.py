import pandas as pd
df = pd.read_csv("expense.csv")
#print(df)

#for selecting coloumns syntax:
#print(df["amount"])

#syntaxx for accessing columns saare columns:
# print(df.columns)

#syntax for counting total rows ad=nd columns:
#print(df.shape)

#using this syntax below we can list the columns headers:
#print(list(df.columns))

#below shows the method of how to strip the empty or blank spaces in the columns:
#df.columns = df.columns.str.strip()
#print(df.columns)

#Here we are starting with the GROUPBY func in pandas : in eng -: group the data by category where only take from each group amount and sum 
#category_summary = df.groupby("category")["amount"].sum()
#print(category_summary)

#here we are gonna filter columns by time ex : since our date is in type[str] well first convert it into datetime format
df["date"] = pd.to_datetime(df["date"])

#after conversion to datetime
#current_month_data = df[
    #(df["date"].dt.year == pd.Timestamp.now().year) &
    #(df["date"].dt.month == pd.Timestamp.now().month)]

#print(current_month_data)
#monthly_total = current_month_data["amount"].sum()
#print("monthly total : " , monthly_total )
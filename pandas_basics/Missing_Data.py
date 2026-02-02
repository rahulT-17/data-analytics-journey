# Here we are gonna see how we can identify missing datas in our dataset and effectively fix it.

# To LOAD AND INSPECT our Missng Values (Na)
df = pd.read_csv("Xyzfilename.csv") 
print(df) 

# To find the Mjssing data in our data frame we would use this syntax : 
print(df.isna())       # Gives value in boolean [True or False]
                       # True : data is missing | False : data exists

# To COUNT missing values in the columns : Gives us which column is broken and how many rows are affected
print(df.isna().sum())

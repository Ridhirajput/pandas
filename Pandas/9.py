#we can replcae values empty values of a specified columns
import pandas as pd
df=pd.read_csv('data.csv')
df["Calories"].fillna(130,inplace=True)
#print(df.to_string())
print(df.to_string())
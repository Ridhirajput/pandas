#Replace empty values using mean,median,mode
import pandas as pd
df=pd.read_csv('data.csv')
print(df.to_string())
x=df["Calories"].mean()
df["Calories"].fillna(x,inplace=True)
print(df.to_string())
#mean=sum of all values divided by no of values.
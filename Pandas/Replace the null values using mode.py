#Replace the null values using mode
import pandas as pd
df=pd.read_csv('data.csv')
x=df["Calories"].mode()[0]
df["Calories"].fillna(x,inplace=True)
print(df.to_string())
#mode=the values appear most frequently

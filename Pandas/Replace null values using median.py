#Replacing the null/empty values of column using median 
import pandas as pd 
df=pd.read_csv('data.csv')
x=df['Calories'].median()
df["Calories"].fillna(x,inplace=True)
print(df.to_string())
#median=the middle value after sorting in ascending order.

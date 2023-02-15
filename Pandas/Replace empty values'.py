#Replace empty values 
#Another way of dealing with null values row is to insert the new values to these empty cells
import pandas as pd
df=pd.read_csv('data.csv')
df.fillna(130,inplace=True)
print(df.to_string())
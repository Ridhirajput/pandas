#Cleaning Data
#Data cleaning means fixing bad data in your dataset.which could be - empty cells,data in wrong format,wrong data,
# duplicates
import pandas as pd
df=pd.read_csv('data.csv')
new_df=df.dropna() # dropna method returns new dataframe and will not change the original but if we want to replace
# the original one with the new one we can use "df.dropna(inplace=True)"-it will not return new data frame it will
#  remove the empty rows from the original dataframe
print(new_df.to_string())
#to remove the duplicated rows we can use duplicated(). duplicated() method returns boolean values
import pandas as pd 
df=pd.read_csv('data.csv')
#it will return true for duplicated rows
#print(df.duplicated().to_string())
#Remove duplicated rows
df.drop_duplicates(inplace=True)
print(df.duplicated().to_string())
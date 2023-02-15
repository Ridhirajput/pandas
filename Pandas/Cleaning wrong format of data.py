#Cleaning wrong format of data
#To clean the data frame we can either remove the wrong formatted data or convert them into the same format
#converting into correct format
import pandas as pd
df=pd.read_csv('data2.csv')
df['Date']=pd.to_datetime(df['Date'])
print(df.to_string())
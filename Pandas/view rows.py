#viewing the data
#the head() method returns the headers and the specified number of rows starting from the top.
import pandas as pd
df=pd.read_csv('data.csv')
print(df.head(10))  # it will print the 10 rows from the start
print(df.head()) # it will print the 5 rows from the start


print(df.tail(10)) # it will print the 10 rows from the last
print(df.tail())  # it will print the 5 rows from the last


print(df.info()) #info tells the no of rows and volumn and the name of columns,count of non-null values and their datatype.
 

#Load files into data frame 
# we use .to_string() to print the whole data frame
import pandas as pd
file_read=pd.read_csv('data.csv')
print(file_read.to_string())
print(file_read) 
print(pd.options.display.max_rows)
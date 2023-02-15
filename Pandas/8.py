#Load files into data frame 
#if we want to read the /display the whole data frame frame csv file without using to_string() we can increase the 
#number of display rows
import pandas as pd
pd.options.display.max_rows=9999
file_read=pd.read_csv('data.csv')
print(file_read)
# Data sets in pandas are multi dimensional ,are known as Data Frames
# Series is like a column and Data Frames are the whole  table 

import pandas as pd
my_data_set={
    'cars': ["BMW","Reanault","Ferrari"],
    'locations': ["Mumbai","Kolkata","Pune"],
    'sites': [56,7678,23]
}

myvar=pd.DataFrame(my_data_set)
print(myvar)
print(pd.__version__)

#Pandas Dataframe is a 2 dimensional data structure like a 2 dimensional araay or a table.
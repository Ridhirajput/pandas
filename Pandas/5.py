# to return the row we use loc in pandas 
import pandas as pd
my_data_set={
    'cars': ["BMW","Reanault","Ferrari"],
    'locations': ["Mumbai","Kolkata","Pune"],
    'sites': [56,7678,23]
}
df=pd.DataFrame(my_data_set)
print(df.loc[1]) # this will return the row no 1 
print(df.loc[[1,2]]) # this will return the row no 1 and 2 
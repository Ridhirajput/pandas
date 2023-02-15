# named indexes
import pandas as pd
my_data_set={
    'cars': ["BMW","Reanault","Ferrari"],
    'locations': ["Mumbai","Kolkata","Pune"],
    'sites': [56,7678,23]
}
df=pd.DataFrame(my_data_set,index=["First","Second","Third"])
print(df)
print(df.loc["Second"])

import pandas as pd 
df=pd.read_csv('data.csv')
#one way to fix values is to replace them with something 
#1st way
df.loc[7,'Duration']=45
print(df.to_string())
#2nd way
#for the small sets we might be able to replace the wrong data one by one but for the large sets of wrong data we can
#some boundaries/rules like loops with conditional statements
for x in df.index:
    if df.loc[x,'Duration'] > 45:
        df.loc[x,'Duration'] = 00
print(df.to_string())
#3rd way 
#another way is to remove the wrong  data
for x in df.index:
    if df.loc[x,'Duration'] > 45:
        df.drop(x,inplace=True)
print(df.to_string())




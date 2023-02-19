import pandas as pd 
df=pd.read_csv('data.csv')
print(df.corr())

#perfect relationship=duration and  duration(1)
#good relationship=duration and calories(0.9)
#bad relationship=duration and maxpulse (0.009)
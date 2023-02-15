import pandas as pd 
cal = {"day1":778,"day2":234,"day3":896}
myvar=pd.Series(cal)
print(myvar)
myvar1=pd.Series(cal,index=["day1","day2"])
print(myvar1)
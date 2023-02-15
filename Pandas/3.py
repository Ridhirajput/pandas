# creating your own labels 
import pandas as pd
a=[2,3,4]
myvar=pd.Series(a,index=["x","y","z"]) # here we are creating our own labels 
print(myvar)
print(myvar["y"]) # here we are accessing elements of series using our own ctreated labels
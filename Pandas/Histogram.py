#we use kind keyword to specify that we want histogram
import pandas as pd 
import sys
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df['Duration'].plot(kind='hist')
plt.show()
#plt.savefig(sys.stdout.buffer)
#sys.stdout.flush()

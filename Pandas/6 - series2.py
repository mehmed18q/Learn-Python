import numpy as np
import pandas as pd
data=np.array(['t','o','p','l'])
myseries=pd.Series(data,index=['first','second','third','fourth'])
#loc , iloc
#print(myseries.iloc[3:6])
print(myseries.loc['second': 'fourth'])
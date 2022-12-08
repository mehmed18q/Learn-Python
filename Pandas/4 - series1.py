#series , Data frame
import numpy as np
import pandas as pd
data= np.array(['t','o','p','l','e','a','r','n'])
myseries = pd.Series(data)
# print(myseries.index)
# data={'first':'ali','sec':'majid','third':'hosein'}
# ser=pd.Series(data,index=['sec','first','5th','third'])
print(myseries[3:5])
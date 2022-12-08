import pandas as pd
import numpy as np
data = {'name':['ali','hamid',np.nan,'reza'],'age':[18,40,23,25],
        'city':['tehran','shiraz','tehran',np.nan],'teaching':[np.nan,np.nan,np.nan,np.nan]}
df = pd.DataFrame(data)
#isnull notnull
#print(df.fillna('undefind'))
#dropna
print(df.dropna(axis=1))








#
#
# print(df[df['age']>=25])


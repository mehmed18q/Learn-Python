import pandas as pd 
import numpy as np
df=pd.read_csv('file.csv')
#print(df)
mygp=df.groupby('Name')
#print(mygp.groups)
# def myfunc(self):
#     return df.loc[self].Test1 > df.loc[self].Test2

# print(df.groupby(myfunc).groups)
#print(mygp['Test3'].agg(np.mean))
# for name, group in mygp:
#     print('Name')
#     print(group)
# getgp=mygp.get_group('Ali')
# print(getgp)

df1=pd.DataFrame({'name':['Ali','Hamid','Sadeq'],
    'grade':[80,75,63],'qualification':['High','Mid','Low']})
    
df2=pd.DataFrame({'eddited':['Ali','Hamid','Sadeq'],
    'grade':[56,82,73],'qualification':['Low','High','Mid']})

print(pd.concat([df1,df2]))

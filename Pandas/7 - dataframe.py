import pandas as pd
# mylist=['toplearn','pandas','tutorial']
# df=pd.DataFrame(mylist,index=['first','second','third'],columns=['text'])
# print(df)
data={'name':['ali','reza','hosein'],'age':[25,36,18],'city':['tehran','esfahan','shiraz'],'email':['test1','test2',
                                                                                                   'test3']}
df=pd.DataFrame(data,index=['person1','person2','person3'])
print(df.loc['person1':'person3','age':'email'])
#print(df.iloc[0:2,1:2])


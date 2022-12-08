import pandas as pd 
# import matplotlib.pyplot as plt
# df= pd.read_csv('file.csv')
# df['Grade'].plot()
# plt.show()






# df_1=pd.DataFrame({'name':['Ali','Hamid','Sadeq'],
#     'grade':[80,75,63],'qualification':['High','Mid','Low']})
    
# df_2=pd.DataFrame({'name':['Ali','Hamid','Sadeq'],
#     'grade':[56,82,73],'qualification':['Low','High','Mid']})

    
# df_3=pd.DataFrame({'name':['Ali','Hamid','Sadeq'],
#     'grade':[49,72,84],'email':['test1','test2','test3']})

# #print(pd.merge(df_1,df_2,on= 'name'))    

# df_1.set_index('name',inplace=True)
# df_2.set_index('name',inplace=True)

# myjoin=df_1.join(df_3,lsuffix='_left')
# print(myjoin)





df_1=pd.DataFrame({'name':['Ali','Sara','Sadeq','Hamed'],
    'grade':[80,75,63,45],'qualification':['High','Mid','Low','low']})

    
df_2=pd.DataFrame({'name':['Omid','Hamid','Sadeq','Hamed'],
    'grade':[56,82,73,89],'qualification':['Low','High','Mid','High']})

    
df_3=pd.DataFrame({'name':['Ali','Hamid','Sadeq'],
    'grade':[49,72,84],'email':['test1','test2','test3']})

merged=pd.merge(df_1,df_2,on='name',how='outer')
merged.set_index('name',inplace=True)
print(merged)
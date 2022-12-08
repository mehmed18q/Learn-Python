import pandas as pd
data_1=pd.Series([16,3,87,14,2],index=['a','b','c','d','f'])
data_2=pd.Series([29,45,6,44,78],index=['a','b','c','d','f'])
#print(data_1.add(data_2))
#print(data_1.sub(data_2))
#print(data_1.mul(data_2))
#print(data_1.div(data_2))
print(data_1.pow(data_2))
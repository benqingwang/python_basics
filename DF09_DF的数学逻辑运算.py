import pandas as pd
import os
import numpy as np

# ====================================================================
# 比较2个DF是否相同：(df1==df2)
# ====================================================================
#1 Compare two DF - boolean DF
data1=[[1,2,3],[4,5,6],[7,8,9]];df1=pd.DataFrame(data1,columns=['a','b','c'])
data2=[[11,12,13],[4,5,6],[17,18,19]];df2=pd.DataFrame(data2,columns=['a','b','c'])
bolean_df=(df1==df2)

#2 Compare across types - want to consider '1' and 1 are the same
data=[[1,'1'],[2,'2'],[8,9]];df=pd.DataFrame(data,columns=['a','b'])
df['a']==df['b']
df['a'].astype(str)==df['b']
df['a']==df['b'].astype(float)

# ====================================================================
# 算术计算
# ====================================================================
df1*0.5+1

# ====================================================================
# 逻辑运算
# ====================================================================
# 1a. 如果column a大于3， 则给column d赋值为'High'
df.loc[df['a']>3,'d']='High'

# 1b. 如果column a大于3， 则给column d赋值为'High'，否则赋值为'Low'
df['d']=np.where(df['a']>3,'High','Low')

# 2a. 如果column a大于3， 则给column d赋值为column c乘以2减一
df.loc[df['a']>3,'d']=df['c']*2-1

# 2b. 如果column a大于3， 则给column d赋值为column c乘以2减一；否则就是column c的值
df['d']=np.where(df['a']>3,df['c']*2-1,df['c'])

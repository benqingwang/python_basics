import pandas as pd
import os
import numpy as np

#---------------------------------------------------------------------
# Sample Dataset
#---------------------------------------------------------------------
data=[[1,2,3],[4,5,6],[7,8,9]]
df=pd.DataFrame(data,columns=['a','b','c'])
print(tabulate(df, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
|  2 |   7 |   8 |   9 |
+----+-----+-----+-----+
#---------------------------------------------------------------------
# Select per location or name
#---------------------------------------------------------------------
# 1 根据location选择
df.iloc[1:3]        # select rows per location (continuous row)
df.iloc[[0,2]]      # select rows per location (discrete row)

df.iloc[:,0]        # select cols per col location (1 col)
df.iloc[:,[0,2]]    # select cols per col location (discrete cols)

df.iloc[1,2]        # select per cell's index
df.iloc[[0,2],[1,2]]        # select per location index (discrete)
df.iloc[range(2),[1,2]]     # select per location index (continuous)
df.iloc[0:2,[1,2]]          # select per location index (continuous)


# 2 根据name选择
df.loc[1:3]         # select rows per row name

df[['a','c']]       # select cols per col name

df.loc[1,'c']       # select per cell's column or row name
df.loc[[0,2],['a','c']]     # select per cell's column or row name
df.loc[range(3),['a','c']]  # select per cell's column or row name
df.loc[0:2,['a','c']]  # select per cell's column or row name

#---------------------------------------------------------------------
# Select sub-DF per conditions
#---------------------------------------------------------------------
data=[['Nemo',2,3],['Bob',np.nan,6],['Lulu',8,9]]
df=pd.DataFrame(data,columns=['cat','age','weight'])
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 | Nemo  |     2 |        3 |
|  1 | Bob   |   nan |        6 |
|  2 | Lulu  |     8 |        9 |
+----+-------+-------+----------+

#1 Simple comparison: 
df[df['age']<5]
df[df['weight']!=6]

#2 Multiple conditions
df[(df['age']<5) & (df['weight']!=6)]  # multiple condition "()" is a must
df[(df['age']<5) | (df['weight']!=6)]  # | means or

#3 value ISIN (a universee)
condition1=df['age'].isin({2,5})
condition2=df['weight'].isin({3,9})  
df[condition1&condition2]

#4 isnull and notnull
df[df['age'].isnull()]
df[df['age'].notnull()]

#5 value string test
df[df['cat'].str.contains('o')]        # contain letter 'o'
df[df['cat'].str.endswith('mo')]       # ends with 'mo‘
df[df['cat'].str.startswith('Bo')]     # starts with 'Bo'
df[df['cat'].apply(lambda x: (x.lower()).startswith('bo'))] # start with 'Bo' or 'bo'

#---------------------------------------------------------------------
# Select sub-DF per location + conditions
#---------------------------------------------------------------------
2种方法: 
    Syntax: df[location][conditions]
    Syntax: df.loc[condition,location]

#1 df[location][conditions]
condition1=df['age'].isin({2,5})
condition2=df['weight'].isin({3,9})  
df['cat'][condition1&condition2]
df[['cat','age']][condition1&condition2]
+----+-------+-------+
|    | cat   |   age |
|----+-------+-------|
|  0 | Nemo  |     2 |
+----+-------+-------+

#2 df.loc[condition,location]
condition1=df['age'].isin({2,5})
condition2=df['weight'].isin({3,9}) 
df.loc[condition1&condition2,['cat','age']]
+----+-------+-------+
|    | cat   |   age |
|----+-------+-------|
|  0 | Nemo  |     2 |
+----+-------+-------+



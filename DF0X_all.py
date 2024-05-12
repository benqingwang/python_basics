import pandas as pd
import os
from tabulate import tabulate

# 我们用下面的例子
data=[[1,2,3],[4,5,6]]
df=pd.DataFrame(data,columns=['a','b','c'])
print(tabulate(df, headers='keys', tablefmt='psql'))
"""
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
+----+-----+-----+-----+
"""
# ==========================================================================
# 1. Insert Replace a column
# ==========================================================================
#1 插入或者replace一个column（值都只有一个)
df['new col1']='a' # can be a scalar 
"""
+----+-----+-----+-----+------------+
|    |   a |   b |   c | new col1   |
|----+-----+-----+-----+------------|
|  0 |   1 |   2 |   3 | a          |
|  1 |   4 |   5 |   6 | a          |
+----+-----+-----+-----+------------+
"""

#2 插入或者replace一个column（值不一样，用list代表所有数值)
df['new col2']=[10,20]
+----+-----+-----+-----+------------+
|    |   a |   b |   c |   new col2 |
|----+-----+-----+-----+------------|
|  0 |   1 |   2 |   3 |         10 |
|  1 |   4 |   5 |   6 |         20 |
+----+-----+-----+-----+------------+

#3 插入或者replace一个column（根据另一个column)
data=[[1,2,3],[4,5,6]]
df=pd.DataFrame(data,columns=['a','b','c'])
df['new col1']='a'
df['new col3']=df['new col1']*2
+----+-----+-----+-----+------------+------------+
|    |   a |   b |   c | new col1   | new col3   |
|----+-----+-----+-----+------------+------------|
|  0 |   1 |   2 |   3 | a          | aa         |
|  1 |   4 |   5 |   6 | a          | aa         |
+----+-----+-----+-----+------------+------------+   
df['new col3']=df['new col1']*2 # can be calculated based on other col

#4 指定location的插入
data=[[1,2,3],[4,5,6]]
df=pd.DataFrame(data,columns=['a','b','c'])
df.insert(1,'new col2',99) # 在位置1的后面插入，新column的名字，值
+----+-----+------------+-----+-----+
|    |   a |   new col2 |   b |   c |
|----+-----+------------+-----+-----|
|  0 |   1 |         99 |   2 |   3 |
|  1 |   4 |         99 |   5 |   6 |
+----+-----+------------+-----+-----+

# ==========================================================================
# 2. Insert Replace a Row
# ==========================================================================
# 1. 在最后一行后面加一行
data=[[1,2,3],[4,5,6]]
df=pd.DataFrame(data,columns=['a','b','c'])
df.loc['new row']=[1,2,3]
+---------+-----+-----+-----+
|         |   a |   b |   c |
|---------+-----+-----+-----|
| 0       |   1 |   2 |   3 |
| 1       |   4 |   5 |   6 |
| new row |   1 |   2 |   3 |
+---------+-----+-----+-----+

df.iloc[-1]=[4,5,6]
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
| -1 |   4 |   5 |   6 |
+----+-----+-----+-----+

# ==========================================================================
# 3. Delete Rows/Columns
# ==========================================================================
# Delete Columns
df.drop(['a','b'], axis=1) 
df.drop(columns=['a','b'])
del df['a'];del df['b']    

# Delete rows
df.drop([1])        # delete a row using drop its name
df[:-1]             # delete last row
df.iloc[:-1]        # delete last row

# ==========================================================================
# 4. Rename Columns
# ==========================================================================
df.columns = ['x','y','z'] # rename all the cols 
df=df.rename(columns = {'x':'xxx','y':'yyy'}) # rename certain cols

# ==========================================================================
# 5. Filter DF's label (column name and row name)
# ==========================================================================
data=[['Nemo',2,3],['Bob',5,6],['Lulu',8,9]]
df=pd.DataFrame(data,columns=['cat','age','weight']) 
df=df.set_index('cat')
print(tabulate(df, headers='keys', tablefmt='psql'))
+-------+-------+----------+
| cat   |   age |   weight |
|-------+-------+----------|
| Nemo  |     2 |        3 |
| Bob   |     5 |        6 |
| Lulu  |     8 |        9 |
+-------+-------+----------+

#1. 用like对一个DF的column name进行fileter (as axis=1), like means including letter'a' 
df = df.filter(like='a', axis=1)
+-------+-------+
| cat   |   age |
|-------+-------|
| Nemo  |     2 |
| Bob   |     5 |
| Lulu  |     8 |
+-------+-------+

#2 用Regex也可以filter。下面的例子是对index进行filter(as axis=0), regex is similar to module re 
df.filter(regex=r'\w+o\w+',axis=0)
+-------+-------+
| cat   |   age |
|-------+-------|
| Bob   |     5 |
+-------+-------+


"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
A04_Select Sub-DF.py
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

import pandas as pd
import os
import numpy as np
myPath=r'C:\Users\Danish\Desktop\python sample'
os.chdir(myPath)

"""********************************************************************
Sample DF
********************************************************************"""
data=[[1,2,3],[4,5,6],[7,8,9]];df=pd.DataFrame(data,columns=['a','b','c'])
"""
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9"""

"""********************************************************************
Select a cell in DF
********************************************************************"""
df.iloc[1,2]        # select per cell's index
df.loc[1,'c']       # select per cell's column or row name

'''Out[95]: 6'''

"""********************************************************************
Select rows/columns per location
********************************************************************"""
df.iloc[1:3]        # select rows per location (continuous row)
df.iloc[[0,2]]      # select rows per location (discrete row)
df.loc[1:3]         # select rows per row name

df.iloc[:,0]        # select cols per col location (1 col)
df.iloc[:,[0,2]]    # select cols per col location (discrete cols)
df[['a','c']]       # select cols per col name

"""********************************************************************
Select sub-DF per location
********************************************************************"""
df.iloc[[0,2],[1,2]]        # select per location index (discrete)
df.iloc[range(2),[1,2]]     # select per location index (continuous)
df.iloc[0:2,[1,2]]          # select per location index (continuous)

df.loc[[0,2],['a','c']]     # select per cell's column or row name
df.loc[range(3),['a','c']]  # select per cell's column or row name
df.loc[0:2,['a','c']]  # select per cell's column or row name

"""********************************************************************
Select sub-DF per conditions

    Syntax: df[conditions]
********************************************************************"""
data=[['Nemo',2,3],['Bob',np.nan,6],['Lulu',8,9]]
df=pd.DataFrame(data,columns=['cat','age','weight'])
"""
    cat  age  weight
0  Nemo  2.0       3
1   Bob  NaN       6
2  Lulu  8.0       9"""

#1 Simple comparison
df[df['age']<5]                        # variable compared with constant
"""
    cat  age  weight
0  Nemo  2.0       3"""                 # nan is excluded

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
"""
   cat  age  weight
1  Bob  NaN       6"""

df[df['age'].notnull()]
"""
    cat  age  weight
0  Nemo  2.0       3
2  Lulu  8.0       9"""

#5 value string test
df[df['cat'].str.contains('o')]        # contain letter 'o'
df[df['cat'].str.endswith('mo')]       # ends with 'mo‘
df[df['cat'].str.startswith('Bo')]     # starts with 'Bo'
df[df['cat'].apply(lambda x: (x.lower()).startswith('bo'))] # start with 'Bo' or 'bo'

"""********************************************************************
Select sub-DF per conditions + Select per location/name

    Syntax: df[location][conditions]
    Syntax: df.loc[condition,location]
********************************************************************"""
data=[['Nemo',2,3],['Bob',5,6],['Lulu',8,9]]
df=pd.DataFrame(data,columns=['cat','age','weight'])
"""
    cat  age  weight
0  Nemo    2       3
1   Bob    5       6
2  Lulu    8       9"""

#1 df[location][conditions]
condition1=df['age'].isin({2,5})
condition2=df['weight'].isin({3,9})  
df['cat'][condition1&condition2]
df[['cat','age']][condition1&condition2]
"""
    cat  age
0  Nemo    2"""

#2 df.loc[condition,location]
condition1=df['age'].isin({2,5})
condition2=df['weight'].isin({3,9}) 
df.loc[condition1&condition2,['cat','age']]
"""
    cat  age
0  Nemo    2"""

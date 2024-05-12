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


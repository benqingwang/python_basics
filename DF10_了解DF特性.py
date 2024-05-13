import os
import pandas as pd
from tabulate import tabulate

我们用下面的例子说明
data=[[1,2,3],[1,2,3],[7,8,9],[10,11,12]]
df=pd.DataFrame(data,columns=['a','b','c'])
print(tabulate(df, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   1 |   2 |   3 |
|  2 |   7 |   8 |   9 |
|  3 |  10 |  11 |  12 |
+----+-----+-----+-----+

# ====================================================================
# DF的shape
# ====================================================================
len(df.index)       # Number of observations (rows)
len(df)             # Number of observations (rows)
len(df.columns)     # Number of variables (columns)
df.shape            # Num of obs X Num of variables

# ====================================================================
# DF的基本统计
# ====================================================================
df.describe()       # Common stat for variables
+-------+-------+-------+-------+
|       |     a |     b |     c |
|-------+-------+-------+-------|
| count |  4    |  4    |  4    |
| mean  |  4.75 |  5.75 |  6.75 |
| std   |  4.5  |  4.5  |  4.5  |
| min   |  1    |  2    |  3    |
| 25%   |  1    |  2    |  3    |
| 50%   |  4    |  5    |  6    |
| 75%   |  7.75 |  8.75 |  9.75 |
| max   | 10    | 11    | 12    |
+-------+-------+-------+-------+

#1 stat by variables (columns)
df.mean()
df.std()
df['c'].std() # only check for column c
df.pct_change() 
df.quantile(0.75)

#2 stat at DF level - just repeat
df.mean().mean()
df.sum().sum()

#3 conditional statistics
df[df.a>3].sum()
# ====================================================================
# DF的snapshot and sampling
# ====================================================================
df.head(2)          # show first n rows
df.tail(2)          # show last n rows
df.sample(frac=0.5) # randomly select 50% of the rows
df.sample(2)        # randomly select n rows
df.nlargest(2,'a')  # select 2 largest rows in terms of col a
df.nsmallest(2,'a') # select 2 smallest rows in terms of col a

# ====================================================================
# DF的value和unique values
# ====================================================================
df.index.values             # return an array
df.index.values.tolist()    # return a list
df.columns.values

df['a'].unique()        # return unique value of a column
df.iloc[1].unique()     # return unique value of a row
df['a'].value_counts()  # value count for a column (variable)

# ====================================================================
# 检查DF的data type
# ====================================================================
# 1 用.dtypes
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   1 |   2 |   3 |
|  2 |   7 |   8 |   9 |
|  3 |  10 |  11 |  12 |
+----+-----+-----+-----+
df.dtypes
a    int64
b    int64
c    int64

2. str variable的类型是object
+----+-----+-----+-----+
|    |   a | b   |   c |
|----+-----+-----+-----|
|  0 |   1 | a   |   3 |
|  1 |   1 | b   |   3 |
|  2 |   7 | c   |   9 |
|  3 |  10 | d   |  12 |
+----+-----+-----+-----+
a     int64
b    object
c     int64
dtype: object

# 3. 一颗老鼠屎坏一个variable
+----+-----+-----+-----+
|    | a   | b   | c   |
|----+-----+-----+-----|
|  0 | 1   | 2   | 3   |
|  1 | 1   | 2   | 3   |
|  2 | 7   | 8   | 9   |
|  3 | x   | y   | z   |
+----+-----+-----+-----+
df.dtypes
"""
a    object
b    object
c    object
dtype: object"""

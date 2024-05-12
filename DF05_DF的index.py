import pandas as pd
from tabulate import tabulate

# ==========================================================================
# Sample Data
# ==========================================================================
data=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]] 
df=pd.DataFrame(data,columns=['a','b','c'])
print(tabulate(df, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
|  2 |   7 |   8 |   9 |
|  3 |  10 |  11 |  12 |
+----+-----+-----+-----+

# ==========================================================================
# Rename Index
# ==========================================================================
# 改变所有的index
df.index=['a1','a2','a3','a4']
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
| a1 |   1 |   2 |   3 |
| a2 |   4 |   5 |   6 |
| a3 |   7 |   8 |   9 |
| a4 |  10 |  11 |  12 |
+----+-----+-----+-----+

# 只改变个别index
df=df.rename(index = {2:'a2'})
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
| 0  |   1 |   2 |   3 |
| 1  |   4 |   5 |   6 |
| a2 |   7 |   8 |   9 |
| 3  |  10 |  11 |  12 |
+----+-----+-----+-----+

# ==========================================================================
# Set/Reset/Drop Index
# ==========================================================================
比如我们的DF df是这样
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
|  2 |   7 |   8 |   9 |
|  3 |  10 |  11 |  12 |
+----+-----+-----+-----+

# 给一个DF添加index based on a column
df = df.set_index('a')
+-----+-----+-----+
|   a |   b |   c |
|-----+-----+-----|
|   1 |   2 |   3 |
|   4 |   5 |   6 |
|   7 |   8 |   9 |
|  10 |  11 |  12 |
+-----+-----+-----+

# 把index的变为一个column，还保留这个column，并且这个column的名字就是原来它的名字 
# 如果这个column本身就没有名字，本来就是index，那这个column的名字就是lower case 'index'
df=df.reset_index(drop=False)
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
|  2 |   7 |   8 |   9 |
|  3 |  10 |  11 |  12 |
+----+-----+-----+-----+


# 把index彻底去掉，reset为default的0, 1, 2...的index
df=df.reset_index(drop=True)
+----+-----+-----+
|    |   b |   c |
|----+-----+-----|
|  0 |   2 |   3 |
|  1 |   5 |   6 |
|  2 |   8 |   9 |
|  3 |  11 |  12 |
+----+-----+-----+

# ==========================================================================
# 创建多层次index
# ==========================================================================
df.index=pd.MultiIndex.from_tuples([('d',1),('d',2),('e',3),('f',4)])
+----------+-----+-----+-----+
|          |   a |   b |   c |
|----------+-----+-----+-----|
| ('d', 1) |   1 |   2 |   3 |
| ('d', 2) |   4 |   5 |   6 |
| ('e', 3) |   7 |   8 |   9 |
| ('f', 4) |  10 |  11 |  12 |
+----------+-----+-----+-----+


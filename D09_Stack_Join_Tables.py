# 这里我们介绍如何stack或者join 2个DF
# 1. stack DF
# 2. Approximate lookup
# 3. Exact lookup

import pandas as pd
import os

data1=[[1,2,3],[4,5,6],[7,8,9]]
df1=pd.DataFrame(data1,columns=['a','b','c'], index=['x1','x2','x3'])
print(tabulate(df1, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
| x1 |   1 |   2 |   3 |
| x2 |   4 |   5 |   6 |
| x3 |   7 |   8 |   9 |
+----+-----+-----+-----+

data2=[[11,12,13],[14,15,16],[17,18,19]] 
df2=pd.DataFrame(data2,columns=['d','e','f'], index=['y1','y2','y3'])
print(tabulate(df2, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+
|    |   d |   e |   f |
|----+-----+-----+-----|
| y1 |  11 |  12 |  13 |
| y2 |  14 |  15 |  16 |
| y3 |  17 |  18 |  19 |
+----+-----+-----+-----+

#----------------------------------------------------------------------
# 1. Stack DF vertically or horizontally
#----------------------------------------------------------------------
#1 竖着叠加: 这里default是axis=0，所以不说也可以
pd.concat([df1,df2])        # stack vertically with concat
pd.concat([df1,df2],axis=0) # stack vertically with concat

#2 横着并列
pd.concat([df1,df2],axis=1) # stack horizontally with concat
# 如果你想要ignore index

#3 使用ignore_index
ignore_index = True就是把所有index (axis=0) 或者column name (axis=1)转换为0,1,2,3....
df3= pd.concat([df1,df2],axis=0,ignore_index=True)
print(tabulate(df3, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+-----+-----+-----+
|    |   a |   b |   c |   d |   e |   f |
|----+-----+-----+-----+-----+-----+-----|
|  0 |   1 |   2 |   3 | nan | nan | nan |
|  1 |   4 |   5 |   6 | nan | nan | nan |
|  2 |   7 |   8 |   9 | nan | nan | nan |
|  3 | nan | nan | nan |  11 |  12 |  13 |
|  4 | nan | nan | nan |  14 |  15 |  16 |
|  5 | nan | nan | nan |  17 |  18 |  19 |
+----+-----+-----+-----+-----+-----+-----+

df3= pd.concat([df1,df2],axis=1,ignore_index=True)
print(tabulate(df3, headers='keys', tablefmt='psql'))
+----+-----+-----+-----+-----+-----+-----+
|    |   0 |   1 |   2 |   3 |   4 |   5 |
|----+-----+-----+-----+-----+-----+-----|
| x1 |   1 |   2 |   3 | nan | nan | nan |
| x2 |   4 |   5 |   6 | nan | nan | nan |
| x3 |   7 |   8 |   9 | nan | nan | nan |
| y1 | nan | nan | nan |  11 |  12 |  13 |
| y2 | nan | nan | nan |  14 |  15 |  16 |
| y3 | nan | nan | nan |  17 |  18 |  19 |
+----+-----+-----+-----+-----+-----+-----+

#4 如果我想要的是下面的结果，则不应该用ignore_index
+----+-----+-----+-----+-----+-----+-----+
|    |   a |   b |   c |   d |   e |   f |
|----+-----+-----+-----+-----+-----+-----|
|  0 |   1 |   2 |   3 |  11 |  12 |  13 |
|  1 |   4 |   5 |   6 |  14 |  15 |  16 |
|  2 |   7 |   8 |   9 |  17 |  18 |  19 |
+----+-----+-----+-----+-----+-----+-----+
正确的语法是
df3= pd.concat([df1.reset_index(drop=True),
                df2.reset_index(drop=True)],axis=1)

#----------------------------------------------------------------------
# 2. Approximate vlookup using bisect
#----------------------------------------------------------------------
# 我们用这个例子
data=[['Nemo',2,3],['Bob',5,6],['Lulu',8,9]]
df=pd.DataFrame(data,columns=['cat','age','weight']) 
print(tabulate(df, headers='keys', tablefmt='psql'))
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 | Nemo  |     2 |        3 |
|  1 | Bob   |     5 |        6 |
|  2 | Lulu  |     8 |        9 |
+----+-------+-------+----------+

#1 我们先定义一个Mapping的方法:
# age<3, class L
# 3<=age<5, class M
# 5<=age<7, class H
# age>=7, class E

age_list=[3,5,7]                    # vlookup keys
age_group_list=['L','M','H','E']    # vlookup values

#2 use bisect to construct an approximate vlookup
from bisect import bisect
def myvlookup(age):
    mypos=bisect(age_list,age)
    mygrp=age_group_list[mypos]
    return mygrp

#3 使用我们的函数
df['age group']=df['age'].apply(myvlookup)
+----+-------+-------+----------+-------------+
|    | cat   |   age |   weight | age group   |
|----+-------+-------+----------+-------------|
|  0 | Nemo  |     2 |        3 | L           |
|  1 | Bob   |     5 |        6 | H           |
|  2 | Lulu  |     8 |        9 | E           |
+----+-------+-------+----------+-------------+

#----------------------------------------------------------------------
# 3. 用.map()实现Exact Vlookup
#----------------------------------------------------------------------
#1 首先我们有一个dataframe (nation_map) 相当于mapping table
+----+-------+---------------+
|    | cat   | nationality   |
|----+-------+---------------|
|  0 | Nemo  | Mexico        |
|  1 | Bob   | US            |
+----+-------+---------------+

#2 用这个mapping DF创建一个mapping series
mapping=nation_map.set_index('cat')['nationality'] 

#3 用这个series得到exact match
df['nationality']=df['cat'].map(mapping)
+----+-------+-------+----------+---------------+
|    | cat   |   age |   weight | nationality   |
|----+-------+-------+----------+---------------|
|  0 | Nemo  |     2 |        3 | Mexico        |
|  1 | Bob   |   nan |        6 | US            |
|  2 | Lulu  |     8 |        9 | nan           |
+----+-------+-------+----------+---------------+

#----------------------------------------------------------------------
# 3. 用.merge()实现Exact Vlookup
#----------------------------------------------------------------------
df.merge(nation_color_map,on='cat')                 # 不说明就是inner join
df.merge(nation_color_map,on='cat',how='outer')     # outer join
df.merge(nation_color_map,on='cat',how='left')     # left join
df.merge(nation_color_map,on='cat',how='right')     # right join

# 另一个style
pd.merge(df,nation_color_map,on='cat',how='outer')  

# 左右可以是不同名字的key
pd.merge(df,nation_color_map,left_on='cat', right_on='cat', how='outer')  

#----------------------------------------------------------------------
# 4. 用dict.get(,)实现exact match
#----------------------------------------------------------------------
#1 首先我们有一个dataframe (nation_color_map) 相当于mapping table
+----+-------+---------------+---------+
|    | cat   | nationality   | color   |
|----+-------+---------------+---------|
|  0 | Nemo  | Mexico        | mixed   |
|  1 | Bob   | US            | white   |
+----+-------+---------------+---------+

#2 把2个column各自变成一个dictionary
nation_dict=nation_color_map.set_index('cat').T.to_dict('records')[0]
结果是: {'Nemo': 'Mexico', 'Bob': 'US'}
color_dict=nation_color_map.set_index('cat').T.to_dict('records')[1]
结果是: {'Nemo': 'mixed', 'Bob': 'white'}

# 3用dictionary.get()得到merge结果，可以定义not found的情况下如何输出
df['nationality']=df['cat'].apply(lambda x: nation_dict.get(x,'not found'))
df['color']=df['cat'].apply(lambda x: color_dict.get(x,'not found'))
+----+-------+-------+----------+---------------+-----------+
|    | cat   |   age |   weight | nationality   | color     |
|----+-------+-------+----------+---------------+-----------|
|  0 | Nemo  |     2 |        3 | Mexico        | mixed     |
|  1 | Bob   |   nan |        6 | US            | white     |
|  2 | Lulu  |     8 |        9 | not found     | not found |
+----+-------+-------+----------+---------------+-----------+



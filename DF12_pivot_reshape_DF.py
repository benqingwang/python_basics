import pandas as pd
import os

""" Month                Product       State     Sales $
0  January          Volcano Blend  California  488.757790
1  January  Turkish Delight Roast  California    8.403761
2  January  Turkish Delight Roast      Oregon  736.851654
3  January     Breakfast Blastoff      Oregon  330.257964
4  January   Best Blend of Arabia  California  992.611480"""

# ====================================================================
# pivot table - using groupby
# ====================================================================
# 1简单的pivot: 一个column
df.groupby(['Month'])['Sales $'].sum()
"""
Month
April         6858.580996
August        8666.111602
February     10608.775847
January       4327.125696
July          9234.052790
June          8670.847320
March        40684.879014
May           8373.798496
September     8425.431158"""

#2 多个column groupby
df1=df.groupby(['Month','State'])['Sales $'].mean()
"""
Month      State     
April      California    506.065570
           Oregon        384.496431
           Washington    252.534832
August     California    492.307681
           Oregon        528.785255
           Washington    423.258998
February   California    579.075458
           Oregon        398.967952
           Washington    737.333288"""

# ====================================================================
# pivot table - using pd.pivot_table()
# ====================================================================
#1 Pivot Table can get the same results with group by
pd.pivot_table(df,
               values='Sales $',
               index=['Month','State'],
               aggfunc='mean',
               fill_value=None,
               margins=False,
               dropna=True,
               margins_name='All')

"""                        Sales $
Month     State                   
April     California  506.065570
          Oregon      384.496431
          Washington  252.534832
August    California  492.307681
          Oregon      528.785255
          Washington  423.258998
February  California  579.075458
          Oregon      398.967952
          Washington  737.333288"""

# ====================================================================
# pivot table - multiple columns
# ====================================================================
pd.pivot_table(df,values='Sales $',index=['Month'],columns='State',
               aggfunc='mean',fill_value=None,margins=False,dropna=True,
               margins_name='All')
"""
State      California      Oregon  Washington
Month                                        
April      506.065570  384.496431  252.534832
August     492.307681  528.785255  423.258998
February   579.075458  398.967952  737.333288
January    566.317188  515.464237         NaN
July       386.485900  543.062566  609.460332
June       414.526927  466.117784  564.496509
March      509.260906  447.991687  398.910041
May        185.373289  628.305302  581.954492
September  521.582820  502.287851  380.367855"""


# ====================================================================
# 用melt()来Normalize crosstabs
# ====================================================================
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 | Nemo  |     2 |        3 |
|  1 | Bob   |     5 |        6 |
|  2 | Lulu  |     8 |        9 |
+----+-------+-------+----------+

#1 melt without parameters
df.melt()
+----+------------+---------+
|    | variable   | value   |
|----+------------+---------|
|  0 | cat        | Nemo    |
|  1 | cat        | Bob     |
|  2 | cat        | Lulu    |
|  3 | age        | 2       |
|  4 | age        | 5       |
|  5 | age        | 8       |
|  6 | weight     | 3       |
|  7 | weight     | 6       |
|  8 | weight     | 9       |
+----+------------+---------+

#2 assign a key value
pd.melt(df,id_vars='cat')
+----+-------+------------+---------+
|    | cat   | variable   |   value |
|----+-------+------------+---------|
|  0 | Nemo  | age        |       2 |
|  1 | Bob   | age        |       5 |
|  2 | Lulu  | age        |       8 |
|  3 | Nemo  | weight     |       3 |
|  4 | Bob   | weight     |       6 |
|  5 | Lulu  | weight     |       9 |
+----+-------+------------+---------+

# ====================================================================
# Normalize crosstabs - melt()
# ====================================================================
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 | Nemo  |     2 |        3 |
|  1 | Bob   |     5 |        6 |
|  2 | Lulu  |     8 |        9 |
+----+-------+-------+----------+

# ====================================================================
# 用shift插入空行，并且挤掉原有的行
# ====================================================================
#shift down by 2 rows and insert 'NaN' for the new rows
df.shift(2)            
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 |       |   nan |      nan |
|  1 |       |   nan |      nan |
|  2 | Nemo  |     2 |        3 |
+----+-------+-------+----------+

df.shift(-1)
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 | Bob   |     5 |        6 |
|  1 | Lulu  |     8 |        9 |
|  2 |       |   nan |      nan |
+----+-------+-------+----------+


# ====================================================================
# Transpose
# ====================================================================
+----+-------+-------+----------+
|    | cat   |   age |   weight |
|----+-------+-------+----------|
|  0 | Nemo  |     2 |        3 |
|  1 | Bob   |     5 |        6 |
|  2 | Lulu  |     8 |        9 |
+----+-------+-------+----------+

# 1 基本的transpose
df.T
+--------+------+-----+------+
|        | 0    | 1   | 2    |
|--------+------+-----+------|
| cat    | Nemo | Bob | Lulu |
| age    | 2    | 5   | 8    |
| weight | 3    | 6   | 9    |
+--------+------+-----+------+

# 2 把value transpose
df.values.T
+------+-----+------+
| 0    | 1   | 2    |
|------+-----+------|
| Nemo | Bob | Lulu |
| 2    | 5   | 8    |
| 3    | 6   | 9    |
+------+-----+------+



# ====================================================================
# 将 9*1 series 转换为 a 3*3 DF
# ====================================================================
ser=pd.Series(range(9))
"""
0    0
1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8"""

pd.DataFrame(ser.values.reshape(3,3))
"""
   0  1  2
0  0  1  2
1  3  4  5
2  6  7  8"""

# ====================================================================
# 将  a 3*3 DF 转换为 9*1 series
# ====================================================================
df_3_3=pd.DataFrame(pd.Series(range(9)).values.reshape(3,3))
+----+-----+-----+-----+
|    |   0 |   1 |   2 |
|----+-----+-----+-----|
|  0 |   0 |   1 |   2 |
|  1 |   3 |   4 |   5 |
|  2 |   6 |   7 |   8 |
+----+-----+-----+-----+

df_3_3.stack()
0  0    0
   1    1
   2    2
1  0    3
   1    4
   2    5
2  0    6
   1    7
   2    8

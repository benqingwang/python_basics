# DF.iterrows() 是一个 a generator

import pandas as pd

使用的例子
+----+-----+-----+-----+
|    |   a |   b |   c |
|----+-----+-----+-----|
|  0 |   1 |   2 |   3 |
|  1 |   4 |   5 |   6 |
|  2 |   7 |   8 |   9 |
+----+-----+-----+-----+

for index,row in DF.iterrows():
    print (sum(row))

The result is
6
15

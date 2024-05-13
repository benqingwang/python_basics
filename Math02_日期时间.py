import datetime

# =======================================================================
# 手动输入时间日期
# =======================================================================
import datetime
print(datetime.date(2018,9,20))               #-->2018-9-20
print(datetime.datetime(2018,9,20,14,2,30,5)) #--> 2018-09-20 14:02:30.000005
print(datetime.datetime.now())                #-->2018-09-17 21:38:10.771824'
print(datetime.date.today())                  # --> 2018-09-22

# =======================================================================
# 用performance counter: 计算run time
# =======================================================================
import time
t0=time.perf_counter()                        # record start
for i in range(1000000):
    i**2
t1=time.perf_counter()                        # record end
t=t1-t0
print (f'running time is {t}.')

# =======================================================================
# slow down by using time.sleep(#) - 延时器
# =======================================================================
import time
import datetime
print(datetime.datetime.now())
time.sleep(0)
print(datetime.datetime.now())
"""
2018-09-17 21:39:19.112741
2018-09-17 21:39:39.115767"""

# =======================================================================
# 把date time string变成date time object
# =======================================================================
+----+-----+-----------+
|    | 0   | 1         |
|----+-----+-----------|
|  0 | mao | 9-28-2018 |
|  1 | du  | 9-18-2018 |
+----+-----+-----------+

# 1 我们看到所有column都是obj
DF.dtypes
"""
0            object
1            object 类型是object
dtype: object"""

# 2 用pd.to_datetime来转换为时间
DF[1]=pd.to_datetime(DF[1])
DF.dtypes
"""
0            object
1    datetime64[ns] 现在类型变成了datetime
dtype: object"""

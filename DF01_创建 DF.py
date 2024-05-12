import pandas as pd
import os

# ------------------------------------------------------------------------------
# 1. 创建dataframe
# ------------------------------------------------------------------------------
# 1 用nested list创建 
data=[[1,2,3],[4,5,6]]
pd.DataFrame(data,columns=['a','b','c']) 
"""
   a  b  c
0  1  2  3
1  4  5  6"""

# 2 用dictionary of list 创建
data={'a':[1,2,3],'b':[4,5,6]}
pd.DataFrame(data)
"""
   a  b
0  1  4
1  2  5
2  3  6"""

# 3创建同时赋予index
data={'a':[1,2,3],'b':[4,5,6]}
pd.DataFrame(data,index=['a1','a2','a3'])
"""
    a  b
a1  1  4
a2  2  5
a3  3  6"""

# 4用a single variable DICT创建
#直接放入DataFrame是不行的。
# This won't work, because single component is series, not df. you will
# see error message: If using all scalar values, you must pass an index"""
data={'a':1,'b':2,'c':3}
pd.DataFrame(data)

#正确方式是放入Series再to_frame()
pd.Series(data).to_frame()
"""
   0
a  1
b  2
c  3"""

# ------------------------------------------------------------------------------
# 2. 创建empty or single-value DF
# ------------------------------------------------------------------------------
#1 creat single valued DF
df3=pd.DataFrame(0,index=range(3),columns=range(5))

#2 create a completely blank DF
df_blank=pd.DataFrame()

#3 creat empty DF with columns name only
df4=pd.DataFrame(columns=['a','b','c'])
df5=pd.DataFrame(columns=df4.columns)

# ------------------------------------------------------------------------------
# 3. 从其他文件创建DF
# ------------------------------------------------------------------------------
#1 import df from Excel File
# default header length is 1; header=None means no header at all
df=pd.read_excel('python sample.xlsx') # default to import the first tab
df=pd.read_excel('python sample.xlsx','SimpleTable') # certain tab only
df=pd.read_excel('python sample.xlsx','SimpleTable',usecols=[1,3])# certain cols
df=pd.read_excel('python sample.xlsx','EndRow',usecols=[1,3]).dropna() # end early
df=pd.read_excel('python sample.xlsx','Header',header=2) #不是从第一行开始

#2 import multiple tabs from one file
myfile=pd.ExcelFile('python sample.xlsx')
df1=pd.read_excel(myfile,'SimpleTable')
df2=pd.read_excel(myfile,'Header',header=2)
#存所有tab在一个dictionary 
df=pd.read_excel('python sample.xlsx',sheet_name = None) 

#3 import df from csv/test file
df = pd.read_csv('ex1data1.txt', sep=",", header=None)

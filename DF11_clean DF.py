import pandas as pd
import os
import numpy as np

# ====================================================================
# 应付Missing data/bad data - Replace,fill N/A
# ====================================================================
#1 Replace with Regex
df.replace(np.nan, r'no value',regex=True) # replace nan with string
df.replace(1, 'one',regex=True) # replace nan with string

#2 Fill N/A
df.fillna(r'no value')

#3 Drop N/A
df.dropna(axis=0,how= 'any') # drop the row if any value in the row is N/A
df.dropna(axis=0,how= 'all') # drop the row if all the values in the row are N/A
df.dropna(axis=1,how= 'any') # drop the col if any value in the col is N/A

# ====================================================================
# 改变data type or 使用 as type
# ====================================================================
#1 Change Value Type
df.applymap(float)
df.applymap(str)

#2 View as Type
df['a']==df['b'] # directly compare [False, False, True]
df['a'].astype(str)==df['b'].astype(str) # astype compare [True,True,True]

# ====================================================================
# 应对 duplicates
# ====================================================================
df.drop_duplicates(keep='first')    # keep first observation with duplicates (default)
df.drop_duplicates(keep='last')     # keep last observation with duplicates
df.drop_duplicates(keep= False)     # drop all observations with duplicates

df.drop_duplicates(inplace=False)   # return a copy - df does not change
df.drop_duplicates(inplace=True)    # df is permenantly changed.

df.drop_duplicates(subset=['a','c']) # only look at 'a' and 'c' for duplication

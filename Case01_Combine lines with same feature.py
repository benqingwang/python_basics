Combine lines with same feature(s)

"""********************************************************************
Combine lines with same feature(s)
这里的想法就是把要归结的项目组成一个新的DF
然后把符合条件的行做出一个sub-DF，然后把sub-DF的值存入一个list
最后把list输出到新的DF
********************************************************************"""
# Use the same database sample, I want to combine all the lines for a
# particular month into one line


#1 create the first column for my DF, which is the month
# There are alternative ways to do this:
# method 1: use drop_duplicates(). Use double [] to create DF not series
output=df[['Month']].drop_duplicates() 
# method 2: use unique(). The resulte will be a np array - need to convert
output=pd.DataFrame(df['Month'].unique(),columns=['Month'])

"""
0        January
8       February
26         March
116        April
134          May
152         June
170         July
188       August
206    September
"""
#2 Select the columns I want to appear in my DF. Here I choose all of them
select_cols={'Product','State'}

#3 Method 1 Loop through each col and each month to combine data

for col in select_cols:           # e.g. the first one is 'Product'
    output[col]=''                # set initial value as space for one col
    for i in range(len(output)):  # loop through each month
        # form a df only with one month
        month_df=df[df['Month']==output['Month'].iloc[i]]
        # put the values in a list and join them with '\n'
        output[col].iloc[i]='\n'.join(list(month_df[col].values)) 

#3 Method 2: Set month as index
df=df.set_index('Month')
output=output.set_index('Month')
for col in select_cols:           # e.g. the first one is 'Product'
    output[col]=''                # set initial value as space for one col
    for row in output.index.values:
        subDF=df.loc[row]
        output.loc[row,col]='\n'.join(list(subDF[col].values)) 

# Method 3: Use self-defined function





"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
Combine lines with the same feature
example: combine risk node lines with the same AE ID
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

import pandas as pd

"""********************************************************************
1.Simple Case
********************************************************************"""
data=[['A','apple'],['A','avocado'],['B','banana'],['B','blueberry']]
df=pd.DataFrame(data,columns=['Initial','Fruit'])
"""
  Initial      Fruit
0       A      apple
1       A    avocado
2       B     banana
3       B  blueberry"""

output=df[['Initial']].drop_duplicates()
df=df.set_index('Initial')
def stack_lines(idx,df,col):
    return ('\n').join(list(df.loc[idx,col].values))
output['Fruit']=output['Initial'].apply(lambda x: stack_lines(x,df,'Fruit'))

"""********************************************************************
2. Multiple columns to combine
********************************************************************"""
data=[['A','apple','red'],
      ['A','avocado','green'],
      ['B','banana','yellow'],
      ['B','blueberry','blue']]
df=pd.DataFrame(data,columns=['Initial','Fruit','Color'])
"""
  Initial      Fruit   Color
0       A      apple     red
1       A    avocado   green
2       B     banana  yellow
3       B  blueberry    blue"""

output=df[['Initial']].drop_duplicates()
df=df.set_index('Initial')
def stack_lines(idx,df,col):
    return ('\n').join(list(df.loc[idx,col].values))

for col in {'Fruit','Color'}:
    output[col]=output['Initial'].apply(lambda x: stack_lines(x,df,col))
"""********************************************************************
3. Multiple columns to combine - different types
********************************************************************"""
data=[['A','apple','red',1],
      ['A','avocado','green',2],
      ['B','banana','yellow',3],
      ['B','blueberry','blue',4]]
df=pd.DataFrame(data,columns=['Initial','Fruit','Color','Qty'])
"""
  Initial      Fruit   Color  Qty
0       A      apple     red    1
1       A    avocado   green    2
2       B     banana  yellow    3
3       B  blueberry    blue    4"""


output=df[['Initial']].drop_duplicates()
df=df.set_index('Initial')
def stack_lines(idx,df,col):
    return ('\n').join(list(df.loc[idx,col].values.astype(str)))

for col in {'Fruit','Color','Qty'}:
    output[col]=output['Initial'].apply(lambda x: stack_lines(x,df,col))
    
"""********************************************************************
3. Final Generalized method
********************************************************************"""
data=[['A','apple','red',1],
      ['A','avocado','green',2],
      ['B','banana','yellow',3],
      ['B','blueberry','blue',4]]
df=pd.DataFrame(data,columns=['Initial','Fruit','Color','Qty'])
"""
  Initial      Fruit   Color  Qty
0       A      apple     red    1
1       A    avocado   green    2
2       B     banana  yellow    3
3       B  blueberry    blue    4"""


def combine_lines(df,key_col,combine_col_list):
    output=df[[key_col]].drop_duplicates()
    df=df.set_index(key_col)
    def stack_lines(idx,df,col):
        return ('\n').join(list(df.loc[idx,col].values.astype(str)))
    for col in combine_col_list:
        output[col]=output[key_col].apply(lambda x: stack_lines(x,df,col))
    return output

result=combine_lines(df,'Initial',['Fruit','Color','Qty'])

"""********************************************************************
4. Case study
********************************************************************"""
import os
myPath=r'C:\Users\Danish\Desktop\python sample'
os.chdir(myPath)
df=pd.read_excel('python sample.xlsx','Database') 

result=combine_lines(df,'Month',['Product','State','Sales $'])
result.to_excel('temp.xlsx')

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

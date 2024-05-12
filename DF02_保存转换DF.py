#=======================================================================
# 1. 保存DF到Excel
#=======================================================================
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    df1.to_excel(writer, sheet_name='People', index=False)
    df2.to_excel(writer, sheet_name='Products', index=False)
    df3.to_excel(writer, sheet_name='Countries', index=False)

#=======================================================================
# 2. 保存DF到nested List
#=======================================================================
"""
   a  b  c
0  1  2  3
1  4  5  6"""

如果是拿一行作为一个Unit, df.values.to_list(): [[1, 2, 3], [4, 5, 6]]
如果是拿一列作为一个Unit, df.values.T.tolist(): [[1, 4], [2, 5], [3, 6]]

#=======================================================================
# 3. 保存DF到nested Dictionary
#=======================================================================
理解:
    <1> ditionary的关键是有一个key,所以你必须要用set_index定key
    <2> 注意这里需要用T来transpose，因为df自然的状态是vector的形式，如果
    我们不transpose，出来的不是Observation(key):variable1, variable2..
    而会是 variable: observation1, observation2...的形式。这种形式不是
    说没有用，但是很少用。
举例: 
        cat  age  weight
    0  Nemo    2       3
    1   Bob    5       6
    2  Lulu    8       9
df.set_index('cat').T.to_dict('list'): {'Nemo': [2, 3], 'Bob': [5, 6], 'Lulu': [8, 9]}
df.set_index('cat').T.to_dict('records'): [{'Nemo': 2, 'Bob': 5, 'Lulu': 8}, {'Nemo': 3, 'Bob': 6, 'Lulu': 9}]
df.set_index('cat').to_dict('list'): {'age': [2, 5, 8], 'weight': [3, 6, 9]}

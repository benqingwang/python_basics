data=[[4,8,3],[1,2,3],[7,5,9]]
df=pd.DataFrame(data,columns=['a','b','c'])
"""
   a  b  c
0  4  8  3
1  1  2  3
2  7  5  9"""

# sort per one column
df.sort_values('c',ascending=False)              # single sort criteria
'''
   a  b  c
2  7  5  9
0  4  8  3
1  1  2  3'''

# sort per multiple columns
df.sort_values(['c','b'],ascending=[False,True]) # multiple sort
"""
   a  b  c
2  7  5  9
1  1  2  3
0  4  8  3
"""

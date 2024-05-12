import pandas as pd
from tabulate import tabulate

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Occupation': ['Engineer', 'Doctor', 'Artist']}
df = pd.DataFrame(data)

# Print the DataFrame with a border
print(tabulate(df, headers='keys', tablefmt='psql'))

"""
+----+---------+-------+--------------+
|    | Name    |   Age | Occupation   |
|----+---------+-------+--------------|
|  0 | Alice   |    25 | Engineer     |
|  1 | Bob     |    30 | Doctor       |
|  2 | Charlie |    35 | Artist       |
+----+---------+-------+--------------+
"""

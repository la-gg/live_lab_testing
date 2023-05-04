import pandas as pd
from numpy import NaN

data1 = {'name':['A', ' b ', 'c', 'd', 'e'],
         'date':['2007-1-1']*5,
         'value1':[10, 20, NaN, 40, 150],
         'value2':[2, 3, 4, NaN, 6]}

data2 = {'name':['a', 'b', 'C', '  d', 'E'],
         'date':['2008-1-1']*5,
         'value1':[20, 25, 100, 40, 130],
         'value2':[NaN, 6, 8, 10, 12]}

data3 = {'name':['a', 'b', 'c', 'd', 'e'],
         'date':['2009-1-1']*5,
         'value1':[30, 30, 120, 40, 110],
         'value2':[6, 9, 12, 15, 18],
         'value3':[0, 0, 0, 0, 0]}

data4 = {'name':['a', 'b', 'c', 'd', 'e']*2,
         'date':['2007-1-1']*5 + ['2008-1-1']*5,
         'value3':[2, 2, 2, 2, 2, 1, 1, 1, 1, 1]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

# 1) The strings in the "name" columns are messy.  Standardize them using
#    Series string methods.
df1['name'].str.upper()
df2['name'].str.upper()
df3['name'].str.upper()
df4['name'].str.upper()

# 2) Turn the date columns into actual datetime datatypes.
df1['date'] = pd.to_datetime(df1['date']).dt
df2['date'] = pd.to_datetime(df2['date']).dt
df3['date'] = pd.to_datetime(df3['date']).dt
df4['date'] = pd.to_datetime(df4['date']).dt

# 3) Figure out the appropriate way to join these four dataframes together.

# should first join df 4 & 2 
# 4) Work out two ways to fill in the missing values; one that is general and
#    one that lets you replace each NaN with the specific value you want there.

# 5) Write a function that calculates a value4, which is equal to the number in
#    value 3 times the position of the letter in "name" in the alphabet 
#    (e.g. a=1, b=2...)

# 6) Show only the subset of the data for the year 2007.  Show only the subset of
#    the data for name "b".  Show only the subset of the data for value2 >= 10.

# 7) Group the data appropriately and calculate the mean of the values for
#    each group.

# 8) Create a dataframe that includes only the row with the maximum value for
#    value4 for each "name", (i.e. one row for each unique name)

# 9) Take your code from steps 1-4 and move it into an appropriate function(s)
#    that keeps things organized

# 10) Starting with the dataframe created by step 8, reshape it so that each
#    unique name becomes a column, and each row is uniquely identified by a date




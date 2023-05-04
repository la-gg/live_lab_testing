import pandas as pd

# Combine these three dataframes so that the result is a single
# dataframe with the columns "date", "place", "value1", "value2",
# with the date columns being datetime objects that run from
# 1/2020 to 10/2021, without modifying any starter code.
# Note: df1 contains value1 values & df2 contains value2 values.

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

print(df1)
print(df2)
print(df3)

df1['date'] = pd.to_datetime(df1['date']).dt.normalize()

df2['date'] = pd.to_datetime(df2['date']).dt.normalize()

df1 = df1.melt(id_vars='date', value_name='value1', var_name='place')

# then concat 1 & 3
# reshape 2 like 1
# turn everything to datetime
# merge 1 and 3 with 2 with outer merge
# add an assert statement to make sure they're all both
df1['place'] = [['place1']*4, ['place2']*4]



# so I think we want to concat the dates column
# separate by place 




















# ok I'm a little lost, will definitely come back to look at the answers
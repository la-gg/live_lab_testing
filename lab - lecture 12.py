import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

diamonds = pd.read_csv(url_to_csv)

# 1) Create a GroupBy object using "clarity" and "color" as the keys
#    What is the object created?  Can you do anything with it?  Explore.
clar_col = diamonds.groupby(['clarity', 'color'])

clar_col.describe()
clar_col.mean()


# 2) Display the describe() output JUST for group color=E, clarity=SI2.
clar_col.get_group(('SI2', 'E')).describe()


# 3) Display the max value for price in each group.

clar_col.apply(lambda g: g['price'].max())


# 4) Show a dataframe where each row is the diamond from each group w/ the 
#    highest price, with the dataframe sorted by price from highest to lowest.


clar_col.apply(lambda g: g['price'].sort_values(ascending = True).head())



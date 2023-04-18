import pandas as pd

data = {'gdp_usa':[15542, 16197, 16785, 17527, 18238, 18745, 19543], 
        'gdp_canada':[1789, 1829, 1847, 1804, 1556, 1528, 1650], 
        'gdp_mexico':[1181, 1201, 1274, 1315, 1172, 1078, 1159], 
        'unemp_usa':[8.9, 8.1, 7.4, 16.2, 5.3, 4.9, 4.4], 
        'unemp_canada':[7.5, 7.4, 7.2, 7.1, 7, 7.2, 6.4], 
        'unemp_mexico':[7.3, 7, 6.9, 6.6, 6.6, 6.8, 6.1]}

years = [2011, 2012, 2013, 2014, 2015, 2016, 2017]

df = pd.DataFrame(data, index=years)
df

# 1. Write one line that selects only the GDP columns, for the years 
#    2013-2015. There are at least five ways to do this; how many can
#    you find?
#1 
df[[c for c in df.columns if c.startswith('gdp')]]
#2
df[['gdp_usa', 'gdp_canada', 'gdp_mexico']]
#3
gdps = ['gdp_usa', 'gdp_canada', 'gdp_mexico']
df[gdps]
#4
df.loc[:, ['gdp_usa', 'gdp_canada', 'gdp_mexico']]
#5
df.iloc[0:, [0, 1, 2]]


# 2. The unemployment rate in the USA in 2014 should be 6.2, not 16.2.
df.replace(to_replace = 16.2, value = 6.2)

df.replace(to_replace = df.loc[2014, 'unemp_usa'], value = 6.2)
# oh ok so double brackets basically makes a new dataframe
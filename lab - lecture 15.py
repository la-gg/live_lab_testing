import pandas as pd
import os
import datetime
import pandas_datareader.data as web
from pandas_datareader import wb
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# API Key: ULTJJAV9C26FOFJT
apikey = 'ULTJJAV9C26FOFJT'

# 1. Using Pandas DataReader, retrieve the average monthly closing stock
#    prices of Tesla (TSLA) from January 1st, 2019 to December 1st, 2021.

# Hint: https://www.alphavantage.co/support/#api-key

start = datetime.date(year=2019, month=1, day=1)
end = datetime.date(year=2021, month=12, day=1)

df = web.DataReader('TSLA', 'av-monthly', start=start, end=end,
                    api_key='ULTJJAV9C26FOFJT')
df.head()

# 2. Create a new column that holds the rolling 3 month average.

df['three_month_avg'] = df['close'].rolling(3).mean()

# https://stackoverflow.com/questions/45825993/how-to-get-moving-average-of-past-months-in-pandas

# 3. Create a figure showing the time series for the monthly level and
#    the monthly rolling average together.

sns.set()
sns.lineplot(data=df[['close', 'three_month_avg']])
plt.xticks(rotation='vertical')

# https://www.statology.org/seaborn-plot-multiple-lines/

# 4. Recreate your figure showing the time series through May 1st, 2023.
start = datetime.date(year=2019, month=1, day=1)
end_2 = datetime.date(year=2023, month=5, day=1)

df_2 = web.DataReader('TSLA', 'av-monthly', start=start, end=end_2,
                      api_key='ULTJJAV9C26FOFJT')

df_2['three_month_avg'] = df['close'].rolling(3).mean()

sns.set()
sns.lineplot(data=df[['close', 'three_month_avg']])
plt.xticks(rotation='vertical')

# 5. Create a new dataframe from the base data from part 1 that resamples
#    the data to quarterly, using the mean value.
df.index = pd.to_datetime(df.index)
# Q is quarter end indexes, QS is quarter start indexes
df_qtr = df.resample('Q').mean()

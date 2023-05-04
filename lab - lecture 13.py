import matplotlib.pyplot as plt
import pandas as pd
import datetime
import os

# Load the file UNRATE.csv, which shows the seasonally-adjusted US unemployment
# rate, monthly, from 2000 to present.  Create a line plot, with vertical lines
# to mark recessions:
#   March 2001 - November 2001
#   December 2007 - June 2009
#   March 2020 - January 2021 (technically not billed a recession but we'll
#   include it anyway!)

base_path = (r"/Users/alicelele/Desktop/UChicago/Masters/Spring '23 Classes"
             r"/Data and Programming for Public Policy I/Github"
             r"/live_lab_testing")

path = os.path.join(base_path, "UNRATE.csv")

df = pd.read_csv(path, parse_dates=['DATE'])


recessions = [(datetime.datetime(2001, 3, 1),  datetime.datetime(2001, 11, 1)),
              (datetime.datetime(2007, 12, 1), datetime.datetime(2009, 6, 1)),
              (datetime.datetime(2020, 3, 1),  datetime.datetime(2021, 4, 1))]
print(recessions[0])
df.head
df.dtypes

# Vanilla Pandas Plot because we have a pandas dataframe
fig, ax = plt.subplots()
ax = df.plot(x='DATE', y="UNRATE")

# Bigger plot: figsize=(width, height) is a **fig_kw passed to plyplot.figure
fig, ax = plt.subplots(figsize=(12, 6))
ax = df.plot(x='DATE', y="UNRATE", legend=False, ax=ax)


# adding the lines


for start, end in recessions:
    print(start, end)
    ax.axvline(start, color="k", linestyle=":")
    ax.axvline(end, color="k", linestyle=":")

plt.savefig(os.path.join(base_path, "figure.png"))

# can also do a loop for shading the areas
for start, end in recessions:
    ax.axvspan(start, end, alpha=.4, color='gray')

plt.show()

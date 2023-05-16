import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'
diamonds = pd.read_csv(url_to_csv)


# 1) Explore the data & produce some basic summary stats
diamonds.columns
diamonds.mean()
diamonds.head(10)

# 2) Run a simple (hedonic) regression of price (y) on carat (x), including an
#    intercept term.  Report the estimates of the intercept (beta_0) & slope
#    coefficient (beta_1) using each of the following methods:
#        a) NumPy
x = diamonds['price']
y = diamonds['carat']
m, b = np.polyfit(x, y, deg=1)
gen_lin1d = np.poly1d((m, b))
fig, ax = plt.subplots()
ax.plot(x, y, 'ro')
ax.plot(x, gen_lin1d(x), 'k--')
ax.set_ylabel('price')
ax.set_xlabel('carat')
ax.set_title('Diamonds: Carat on Price')

#        b) statsmodels (smf)
model = smf.ols('price ~ carat', data=diamonds)
result = model.fit()

#        c) statsmodels (sm)
diamonds['intercept'] = np.ones(len(diamonds))
model = sm.OLS(endog=diamonds['carat'], exog=diamonds[['intercept', 'price']])
result = model.fit()

#        d) scikit-learn (LinearRegression)
#           Hint:  scikit-learn only works with array-like objects.
carat = np.array(diamonds['carat'])
price = np.array(diamonds['price'])
model = LinearRegression(fit_intercept=False)
results = model.fit(carat, price)
#    Confirm that all four methods produce the same estimates.

# 3) Run a regression of price (y) on carat, the natual logarithm of depth
#    (log(depth)), and a quadratic polynomial of table (i.e., include table &
#    table**2 as regressors).  Estimate the model parameters using any Python
#    method you choose, and display the estimates.


# 4) Run a regression of price (y) on carat and cut.  Estimate the model
#    parameters using any Python method you choose, and display the estimates.

# 5) Run a regression of price (y) on whatever predictors (and functions of
#    those predictors you want).  Try to find the specification with the best
#    fit (as measured by the largest R-squared).  Note that this type of data
#    mining is econometric blasphemy, but is the foundation of machine
#    learning.  Fit the model using any Python method you choose, and display
#    only the R-squared from each model.  We'll see who can come up with the
#    best fit by the end of lab.

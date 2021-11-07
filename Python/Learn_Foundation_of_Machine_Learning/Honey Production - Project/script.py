import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")
print(df.head())

# honey production per year
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
print(prod_per_year)

# set the x_value for year in prod_per_year
X = prod_per_year[['year']]
X = X.values.reshape(-1, 1)
# y-value totalprod in prod_per_year
y = prod_per_year.totalprod

# Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, y)
print(f"Coeff value : {regr.coef_[0]}")
print(f"intercept of line: {regr.intercept_}")

y_predict = regr.predict(X) 

plt.scatter(X, y)
# plot the data
plt.plot(X, y_predict, color='red')

plt.title('Total production of honey per year')
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.show()
plt.clf()

# Honey Decline
X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)
future_predict = regr.predict(X_future)

plt.scatter(X, y, color='mediumblue')
plt.plot(X_future, future_predict, color='gold')
plt.title('Future Predict for Total Production of Honey Per Year')
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.show()

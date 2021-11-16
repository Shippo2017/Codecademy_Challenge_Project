import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3


## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
# One quantitative variable
sns.color_palette('Pastel1')
sns.set_style('whitegrid')
sns.set_context('talk', font_scale=0.8)

plt.figure(figsize=(10,5))
sns.boxplot(data=flight, x='coach_price')
plt.title('Coach Price')
plt.show()
plt.clf()

## Task 2
# two quantitative variable
sns.color_palette('Pastel2')
sns.set_style('darkgrid')
sns.set_context('poster', font_scale=0.8)

plt.figure(figsize=(10, 5))
sns.histplot(flight.coach_price[flight['hours'] >= 8])
plt.title('Price for 8 hours flight')
plt.show()
plt.clf()

print('The lowers price for 8 hours long flights $', (np.min(flight.coach_price[flight['hours'] >= 8])))
print('The highest price for 8 hours long flights $', (np.max(flight.coach_price[flight['hours'] >= 8])))
print('The average price for 8 hours long flights $', (np.mean(flight.coach_price[flight['hours'] >= 8])))

## Task 3
sns.color_palette('Dark2')
sns.set_style('white')
sns.set_context('talk', font_scale=0.6)

plt.figure(figsize=(10, 5))
sns.histplot(flight.delay[flight.delay <= 600]) # 600 mins
plt.title('Flight Delay')
plt.show()
plt.clf()

## Task 4
perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))

sns.color_palette('Set1')
sns.set_style('dark')
sns.set_context('poster', font_scale=0.6)

plt.figure(figsize=(10, 5))
sns.lmplot(data=flight_sub, x='coach_price', y='firstclass_price', line_kws={'color': 'black'},
               lowess=True)
plt.title('Visualization Relationship Between Coach Price and First Class Price')

plt.show()
plt.clf()

## Task 5

plt.figure(figsize=(20,8))

# inflight meal
ax1 = plt.subplot(1,3,1) # 1 line, 3 rows, index nr 1 (first position in the subplot)
ax1 = sns.histplot(data=flight, x='coach_price', hue='inflight_meal')
ax1.set(title='Inflight Meal', xlabel='Coach Price', ylabel='Count')

# inflight entertainment
ax1 = plt.subplot(1,3,2) # 1 line, 3 rows, index nr 1 (first position in the subplot)
ax1 = sns.histplot(data=flight, x='coach_price', hue='inflight_entertainment')
ax1.set(title='Inflight Entertainment', xlabel='Coach Price', ylabel='Count')

# inflight wifi
ax1 = plt.subplot(1,3,3) # 1 line, 3 rows, index nr 1 (first position in the subplot)
ax1 = sns.histplot(data=flight, x='coach_price', hue='inflight_wifi')
ax1.set(title='Inflight Wifi', xlabel='Coach Price', ylabel='Count')

plt.suptitle('Relation between Coach Price and Inflight Features')
plt.subplots_adjust(wspace=0.8, bottom=0.2)
plt.tight_layout()

plt.show()
plt.clf()

## Task 6
sns.lmplot(data=flight, y='passengers', x='hours', x_jitter=0.25, scatter_kws={'s':5, 'alpha':0.2}, fit_reg=False)
plt.title('Relation between Passengers and The Length of Flights', fontsize=10)
plt.show()
plt.clf()

## Task 7
sns.lmplot(data=flight, x='coach_price', y='firstclass_price', hue='weekend', fit_reg=False)
plt.title('Price coach and firstclas on weekends')
plt.show()
plt.clf()

## Task 8
plt.figure(figsize=(15,5))
sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.show()
plt.clf()

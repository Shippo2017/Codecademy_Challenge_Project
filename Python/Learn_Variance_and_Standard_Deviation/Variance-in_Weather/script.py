import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

# Explore Data
print(london_data.head())
print(london_data.iloc[100:200])

tot_data = len(london_data)
print(tot_data)


# Looking at Temp
temp = london_data['TemperatureC']
average_temp = np.mean(temp)
temperature_var = np.var(temp)
temperature_std = np.std(temp)
print(temp.head())
print(average_temp)
print(temperature_var)
print(temperature_std)


# Filtering By Month
june = london_data.loc[london_data['month'] == 6]['TemperatureC']
july = london_data.loc[london_data['month'] == 7]['TemperatureC']
print(june)
print(july)
print(np.mean(june))
print(np.mean(july))
print(np.std(june))
print(np.std(july))

for i in range(1, 13):
  month = london_data.loc[london_data['month'] == i]['TemperatureC']
  print('The mean temperature in month ' + str(i) + ' is ' + str(np.mean(month)))
  print('The standard deviation of temperature in month ' + str(i) + ' is ' + str(np.std(month)) + '\n')


# Explore
for i in range(0, 24):
  hour = london_data.loc[london_data['hour'] == i]['dailyrainMM']
  print('The mean rain in hour ' + str(i) + ' is ' + str(np.mean(hour)))
  print('The standard deviation of rain in hour ' + str(i) + ' is ' + str(np.std(hour)) + '\n')

for i in range(1, 13):
  humidity = london_data.loc[london_data['month'] == i]['Humidity']
  print('The mean humidity in month ' + str(i) + ' is ' + str(np.mean(humidity)))
  print('The standard deviation of humidity in month ' + str(i) + ' is ' + str(np.std(humidity)) + '\n')

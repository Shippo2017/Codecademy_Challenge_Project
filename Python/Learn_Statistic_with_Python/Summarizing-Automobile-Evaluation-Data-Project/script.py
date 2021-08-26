import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

# Summarizing Manufacturing Country
car_frequency = car_eval['manufacturer_country'].value_counts()
print(car_frequency)

print(car_frequency.index[3])

car_proportion = car_eval['manufacturer_country'].value_counts(normalize=True, dropna=False)
print(car_proportion)

# Summarizing Buying Costs
print(car_eval['buying_cost'].unique())

buying_cost_categories = ['low', 'med', 'high', 'vhigh']

car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)
print(car_eval['buying_cost'].unique())

median_index = np.median(car_eval['buying_cost'].cat.codes)
print(median_index)

median_car_status = buying_cost_categories[int(median_index)]
print(median_car_status)

# Summarizing Luggage Capacity
print(car_eval['luggage'].value_counts(normalize=True))

print(car_eval['luggage'].value_counts(dropna=False, normalize=True))

print(car_eval['luggage'].value_counts()/len(car_eval['luggage']))

# Summarizing Passenger Capacity
more_five_doors = np.sum(car_eval['doors'] >= '5more')
print(more_five_doors)

five_car_proportion = (car_eval['doors'] == '5more').mean()
print(five_car_proportion)

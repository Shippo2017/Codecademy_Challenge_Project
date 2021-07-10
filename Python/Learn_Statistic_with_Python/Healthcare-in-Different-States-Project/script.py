import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")
print(healthcare.head())
# print(len(healthcare))
# print(healthcare.columns)

# print(healthcare['DRG Definition'].unique())

chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
# print(chest_pain)


# Separating By State
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL']
# print(alabama_chest_pain) 

costs = alabama_chest_pain[' Average Covered Charges '].values
# print(costs)

# plt.figure(figsize=(8,5))
# plt.boxplot(costs)
# plt.title('Alabama Chest Pain Average Covered Charge', fontsize=18)
# plt.xlabel('State', fontsize=14)
# plt.ylabel('Cost ($)')
# plt.show()


# Makin a Boxplot for All States
states = healthcare['Provider State'].unique()
# print(states)

dataset = []
for state in states:
  dataset.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)
# print(dataset)

plt.figure(figsize=(20,6))
plt.boxplot(dataset, labels=states)
plt.title('All States Chest Pain Average Covered Charges', fontsize=18)
plt.xlabel('State', fontsize=14)
plt.ylabel('Cost ($)')
plt.show()


# Explore
# chest pain for Average Medicare Payments
dataset_tot_payment = []
for state in states:
    dataset_tot_payment.append(chest_pain[chest_pain['Provider State'] == state]['Average Medicare Payments'].values)    
# dataset_tot_payment

plt.figure(figsize=(20,6))
plt.boxplot(dataset_tot_payment, labels=states)
plt.title('Chest Pain Average Medicare Payment for All State in US', fontsize=20)
plt.xlabel('State', fontsize=14)
plt.ylabel('Cost ($)', fontsize=14)
plt.show()


# 194 - SIMPLE PNEUMONIA & PLEURISY W CC
simple_pneumonia = healthcare[healthcare['DRG Definition'] == '194 - SIMPLE PNEUMONIA & PLEURISY W CC']
len(simple_pneumonia)

states_simple_pneumonia = simple_pneumonia['Provider State'].unique()
states_simple_pneumonia

dataset_cost_pneumonia = []
for state in states_simple_pneumonia:
    dataset_cost_pneumonia.append(simple_pneumonia[simple_pneumonia['Provider State'] == state][' Average Total Payments '].values)
# dataset_cost_pneumonia

plt.figure(figsize=(20,6))
plt.boxplot(dataset_cost_pneumonia, labels=states_simple_pneumonia)
plt.title('Average Total Payment for 194-SIMPLE PNEUMONIA & PLEURISY W CC by States in US', fontsize=20)
plt.xlabel('State ($ cost)')
plt.show()

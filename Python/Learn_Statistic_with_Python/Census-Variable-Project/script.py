import codecademylib3

# Import pandas with alias
import pandas as pd
import numpy as np

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
print(census.head())

print(census.dtypes)

# Inspecting Datatypes
print(census['birth_year'].unique())

# Altering Data

census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census['birth_year'].unique())

# Change from str to int
census['birth_year'] = census['birth_year'].astype('int')
print(census['birth_year'].dtypes)

# Print the average birth year
print(census['birth_year'].mean())

# Convert the higher tax variable to the category
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered=True)

print(census['higher_tax'].unique())

# Label encode the higher tax variable and print the median
census['higher_tax_codes'] = census['higher_tax'].cat.codes
print(census.head())

print(census['higher_tax_codes'].median())

# Extra (No.11)
# Label encoding the marital status
print(census['marital_status'].unique())

census['marital_codes'] = pd.Categorical(census['marital_status'], ['single', 'married', 'divorced', 'widowed'], ordered=True)
print(census['marital_codes'].unique())

census['marital_codes'] = census['marital_codes'].cat.codes
print(census.head())

# (No.10) One-Hot Encode marital status to create binary
census = pd.get_dummies(data=census, columns=['marital_status'])
print(census.head())

# Extra (No.11)
census['age'] = 2021 - census['birth_year']
age_bins = np.arange(min(census['age']) - 4, 100, 5)
census['age_group'] = pd.cut(census['age'], bins=age_bins)

print(census.head())

# another code extra (no.11) age group
# census['age_group'] = pd.Categorical(census['birth_year'].apply(lambda x: str((2021-x) - (2021-x) % 5)\
#                       + '-' + str((2021-x) - (2021-x) % 5 + 4)), [str(5*i+5) + '-' + str(5*i+5+4)\
#                       for i in range(70)])
# print(census.head())

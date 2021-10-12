# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
print(abdata.head())

# No.2
xtab = pd.crosstab(abdata['group'], abdata['is_purchase'])
print(xtab)

# No.3
from scipy.stats import chi2_contingency

chi2, pval, dof, expected = chi2_contingency(xtab)
print('p-value', pval)

# No.4
num_visits = len(abdata)
print('number of visitors : ', num_visits)

# No.5
num_sales_needed_099 = 1000.0 / 0.99
print('num sales for $0.99 : ', num_sales_needed_099)

# No.6
p_sales_needed_099 = num_sales_needed_099 / num_visits
print('proportion of sales for 0.99 : ', p_sales_needed_099)

# No.7
num_sales_needed_199 = 1000 / 1.99
print('num sales for 1.99 : ', num_sales_needed_199)

p_sales_needed_199 = num_sales_needed_199 / num_visits
print('proportion of sales for 1.99 : ', p_sales_needed_199)

num_sales_needed_499 = 1000 / 4.99
print('num sales for 4.99 : ', num_sales_needed_499)

p_sales_needed_499 = num_sales_needed_499 / num_visits
print('proportion of sales for 4.99 : ', p_sales_needed_499) 

# no.8
samp_size_099 = np.sum(abdata['group'] == 'A')
sales_099 = np.sum((abdata['group'] == 'A') & (abdata['is_purchase'] == 'Yes'))

print('num size 0.99 : ', samp_size_099)
print('num purchase 0.99 : ', sales_099)

# No.9
samp_size_199 = np.sum(abdata['group'] == 'B')
sales_199 = np.sum((abdata['group'] == 'B') & (abdata['is_purchase'] == 'Yes'))

print('num size 1.99 : ', samp_size_199)
print('num purchase 1.99 : ', sales_199)

samp_size_499 = np.sum(abdata['group'] == 'C')
sales_499 = np.sum((abdata['group'] == 'C') & (abdata['is_purchase'] == 'Yes'))

print('num size 4.99 : ', samp_size_499)
print('num purchase 4.99 : ', sales_499)

# No.10
from scipy.stats import binom_test

pval = binom_test(sales_099, samp_size_099, p_sales_needed_099, alternative='greater')
print('p-value for A (0.99) : ', pval)

# No.11
pvalB = binom_test(sales_199, samp_size_199, p_sales_needed_199, alternative='greater')
print('p-value for B (1.99) : ', pvalB)

# No.12
pvalC = binom_test(sales_499, samp_size_499, p_sales_needed_499, alternative='greater')
print('p-value for C (4.99) : ', pvalC)

# No.13
charge_package = 4.99
print('Price for update package : $', charge_package)

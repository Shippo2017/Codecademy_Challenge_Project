# Import libraries
import numpy as np
import pandas as pd
import codecademylib3

# Import data
dogs = pd.read_csv('dog_data.csv')
print(dogs.head())
print(len(dogs))

print(dogs['breed'].unique())

# No.2
whippet_rescue = dogs.is_rescue[dogs['breed'] == 'whippet']

# No.3
num_whippet_rescues = np.sum(whippet_rescue == 1)
print('Whippets are rescues : ', num_whippet_rescues)

# No.4
num_whippets = len(whippet_rescue)
print('Total Whippets are : ', num_whippets)

print('Mean Whippets : ', np.mean(whippet_rescue))
# No.5
from scipy.stats import binom_test

pval = binom_test(num_whippet_rescues, num_whippets, .08)
print('p-value for whippets rescues of binom-test : ', pval)

# No.6
wt_whippets = dogs.weight[dogs['breed'] == 'whippet']
wt_terriers = dogs.weight[dogs['breed'] == 'terrier']
wt_pitbulls = dogs.weight[dogs['breed'] == 'pitbull']

# No.7
from scipy.stats import f_oneway
fstat, pval = f_oneway(wt_whippets, wt_terriers, wt_pitbulls)
print('p-value of ANOVA : ', pval)

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]
# print(dogs_wtp)

# No.8
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey = pairwise_tukeyhsd(dogs_wtp.weight, dogs_wtp.breed, 0.05)
print(tukey)

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]
# print(dogs_ps)

# No.9
xtab = pd.crosstab(dogs_ps.breed, dogs_ps.color)
print(xtab)

# No.10
from scipy.stats import chi2_contingency

chi2, pval, dof, expected = chi2_contingency(xtab)
print('p-value : ', pval)

# No.11

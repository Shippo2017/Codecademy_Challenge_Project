# import libraries
import codecademylib3
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp
from scipy.stats import binom_test

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

yes_hd = heart[heart.heart_disease == 'presence']
no_hd = heart[heart.heart_disease == 'absence']

# No.1
chol_hd = yes_hd['chol']
print(chol_hd.head())

# N0.2
chol_hd_mean = np.mean(chol_hd)
print('Average cholesterol level for patients with heart disease :')
print(chol_hd_mean)

# No.3 ans No.4
tstats, pval = ttest_1samp(chol_hd, 240)
print(pval/2)

# No.5
chol_no_hd = no_hd['chol']
print(chol_no_hd.head())

chol_no_hd_mean = np.mean(chol_no_hd)
print('Average cholesterol level for patients no heart disease :')
print(chol_no_hd_mean)

tsats, pval = ttest_1samp(chol_no_hd, 240)
print(pval/2)

# No.6
num_patients = len(heart)
print(num_patients)

# No.7
num_highfbs_patients = len(heart[heart['fbs'] == 1])
print(num_highfbs_patients)

# No.8
print(0.08 * num_patients)

# N0.10
p_value = binom_test(num_highfbs_patients, num_patients, 0.08, alternative='greater')
print(p_value)

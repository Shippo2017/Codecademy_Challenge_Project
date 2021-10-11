# Import libraries
import pandas as pd
import numpy as np

# Load datasets
lifespans = pd.read_csv('familiar_lifespan.csv')
iron = pd.read_csv('familiar_iron.csv')

# No.1
print(lifespans.head())

print(lifespans['pack'].unique())

# No.2
vein_pack_lifespans = lifespans.lifespan[lifespans['pack'] == 'vein']
print(vein_pack_lifespans.head())

# No.3
vein_pack_mean = np.mean(vein_pack_lifespans)
print('Mean lifespan for vein pack : ', vein_pack_mean)

# No.4
from scipy.stats import ttest_1samp

tstat, pval = ttest_1samp(vein_pack_lifespans, 73)
print('p-value for lifespan of Vein Pack, one-sample t-test : ', pval)

# No.6
artery_pack_lifespans = lifespans.lifespan[lifespans['pack'] == 'artery']
print(artery_pack_lifespans.head())

# No.7
print('Mean lifespan for Artery pack : ', np.mean(artery_pack_lifespans))

# No.8
from scipy.stats import ttest_ind

tstat, pval = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
print('p-value of two-sample t-test : ', pval)

# No.10
print(iron.head())

# No.11
xtab = pd.crosstab(iron['pack'], iron['iron'])
print(xtab)

# No.12
from scipy.stats import chi2_contingency

chi2, pval, dof, expected = chi2_contingency(xtab)
print('p-value : ', pval)

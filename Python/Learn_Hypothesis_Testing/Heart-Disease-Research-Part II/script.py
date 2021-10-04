# import libraries
import codecademylib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from scipy.stats import ttest_ind, f_oneway, chi2_contingency 
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# load data
heart = pd.read_csv('heart_disease.csv')
print(heart.head())

# No.2
sns.boxplot(x=heart['heart_disease'], y=heart['thalach'])
plt.xlabel('Heart Disease Diagnose')
plt.ylabel('Max heart rate in exercise test')
plt.show()
plt.clf()

# No.3
thalach_hd = heart.thalach[heart['heart_disease'] == 'presence']
thalach_no_hd = heart.thalach[heart['heart_disease'] == 'absence']
print(thalach_hd.head())
print(thalach_no_hd.head())

# No.4
thalach_hd_mean = np.mean(thalach_hd)
thalach_no_hd_mean = np.mean(thalach_no_hd)
thalach_mean_diff = thalach_no_hd_mean - thalach_hd_mean
print('`thalach` mean for patients diagnosed with heart disease :', )
print(thalach_hd_mean)
print('`thalach` mean for patients diagnosed with no heart disease :')
print(thalach_no_hd_mean)
print('`thalach` mean difference : ', thalach_mean_diff)

thalach_hd_median = np.median(thalach_hd)
thalach_no_hd_median = np.median(thalach_no_hd)
thalach_median_diff = thalach_no_hd_median - thalach_hd_median
print('`thalach` median for patients diagnosed with heart disease :')
print(thalach_hd_median)
print('`thalach` median for patients diagnosed with no heart disease :')
print(thalach_no_hd_median)
print('`thalach` median difference : ', thalach_median_diff)

# No.5
tstat, pval = ttest_ind(thalach_hd, thalach_no_hd)
print('p-value for `thalach` two-sample t-test : ', pval)

# No.7 - investigating other quantitative variables
# Age
sns.boxplot(x=heart['heart_disease'], y=heart['age'])
plt.xlabel('Heart Disease Diagnose')
plt.ylabel('Patients Age')
plt.show()
plt.clf()

age_hd = heart.age[heart['heart_disease'] == 'presence']
print(age_hd.head())
age_no_hd = heart.age[heart['heart_disease'] == 'absence']
print(age_no_hd.head())

age_mean_diff = np.mean(age_hd) - np.mean(age_no_hd)
print('`age` mean diff : ', age_mean_diff)

age_median_diff = np.median(age_hd) - np.median(age_no_hd)
print('`age` median diff : ', age_median_diff)

tstat, pval = ttest_ind(age_hd, age_no_hd)
print('p-value for `age` two-sample t-test : ', pval)

#trestbps
sns.boxplot(x=heart['heart_disease'], y=heart['trestbps'])
plt.xlabel('Heart Disease Diagnose')
plt.ylabel('Resting Blood Pressure (mm hg)')
plt.show()
plt.clf()

trestbps_hd = heart.trestbps[heart['heart_disease'] == 'presence']
print(trestbps_hd.head())
trestbps_no_hd = heart.trestbps[heart['heart_disease'] == 'absence']
print(trestbps_no_hd.head())

trestbps_mean_diff = np.mean(trestbps_hd) - np.mean(trestbps_no_hd)
print('`trestbps` mean diff : ', trestbps_mean_diff)

trestbps_median_diff = np.median(trestbps_hd) - np.median(trestbps_no_hd)
print('`trestbps` median diff : ', trestbps_median_diff)

tstat, pval = ttest_ind(trestbps_hd, trestbps_no_hd)
print('p-value for `trestbps` two-sample t-test : ', pval)

# chol - cholesterol
sns.boxplot(x=heart['heart_disease'], y=heart['chol'])
plt.xlabel('Heart disease diagnosed')
plt.ylabel('Cholesterol (mg/dl)')
plt.show()
plt.clf()

chol_hd = heart.chol[heart['heart_disease'] == 'presence']
print(chol_hd.head())
chol_no_hd = heart.chol[heart['heart_disease'] == 'absence']
print(chol_no_hd.head())

chol_mean_diff = np.mean(chol_hd) - np.mean(chol_no_hd)
print('`chol` mean diff : ', chol_mean_diff)

chol_median_diff = np.median(chol_hd) - np.median(chol_no_hd)
print('`chol` median diff : ', chol_median_diff)

tstat, pval = ttest_ind(chol_hd, chol_no_hd)
print('p-value for `chol` two-sample t-test : ', pval)

# No.8 - type of heart pain (cp)
sns.boxplot(x=heart['cp'], y=heart['thalach'])
plt.xlabel('Chest paint type')
plt.ylabel('Maximum heart rate achieved in exercise test')
plt.show()
plt.clf()

print(heart['cp'].unique())

# No.9
thalach_typical = heart.thalach[heart['cp'] == 'typical angina']
thalach_asymptom = heart.thalach[heart['cp'] == 'asymptomatic']
thalach_nonangin = heart.thalach[heart['cp'] == 'non-anginal pain']
thalach_atypical = heart.thalach[heart['cp'] == 'atypical angina']

print(thalach_typical.head())
print(thalach_asymptom.head())
print(thalach_nonangin.head())
print(thalach_atypical.head())

# No.10
fstat, pval = f_oneway(thalach_typical, thalach_asymptom, thalach_nonangin, thalach_atypical)
print('p-value for ANOVA : ', pval)

# No.11
tukey_result = pairwise_tukeyhsd(heart['thalach'], heart['cp'], 0.05)
print(tukey_result)

# No.12
xtab = pd.crosstab(heart['heart_disease'], heart['cp'])
print(xtab)

# No.13
chi2, pval, dof, expected = chi2_contingency(xtab)
print('chi2-value : ', chi2)
print('p-value for chi-square test : ', pval)

# No.14
# heart disease with sex
xtab_sex =pd.crosstab(heart['sex'], heart['heart_disease'])
print(xtab_sex) 

chi2, pval, dof, expected = chi2_contingency(xtab_sex)
print('chi2-value : ', chi2)
print('p-value for chi-square test : ', pval)

import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

# No.1
knicks_pts = nba_2010.pts[nba_2010['fran_id'] == 'Knicks']
nets_pts = nba_2010.pts[nba_2010['fran_id'] == 'Nets']
# print(knicks_pts)
# print(nets_pts)


# No.2
knicks_pts_mean = np.mean(knicks_pts)
nets_pts_mean = np.mean(nets_pts)
diff_mean_2010 = knicks_pts_mean - nets_pts_mean

print('Average points score of Knicks :')
print(knicks_pts_mean)
print('Average points score of Nets :')
print(nets_pts_mean)
print('Difference between the two teams average points score :')
print(diff_mean_2010)

# No.3
plt.figure(figsize=(10,5))
plt.hist(knicks_pts, color='blue', label='Knicks', normed=True, alpha=0.5)
plt.hist(nets_pts, color='red', label='Nets', normed=True, alpha=0.5)
plt.xlabel('Points each team')
plt.ylabel('Frequency')
plt.title('NBA team - Knicks Vs Nets', fontsize=20)
plt.show()
plt.clf()

# No.4
nba_2014 = nba[nba['year_id'] == 2014]
print(nba_2014.head())

knicks_pts14 = nba_2014.pts[nba_2014['fran_id'] == 'Knicks']
# knicks_pts14
nets_pts14 = nba_2014.pts[nba_2014['fran_id'] == 'Nets']
# nets_pts14

knicks_pts14_mean = np.mean(knicks_pts14)
nets_pts14_mean = np.mean(nets_pts14)
diff_mean_2014 = knicks_pts14_mean - nets_pts14_mean

print('Average points score of Knicks in 2014 :')
print(knicks_pts14_mean)
print('Average points score of Nets 2014:')
print(nets_pts14_mean)
print('Difference between the two teams average points score 2014:')
print(diff_mean_2014)

plt.figure(figsize=(10, 5))
plt.hist(knicks_pts14, color='blue', label='Knicks', normed=True, alpha=0.5)
plt.hist(nets_pts14, color='red', label='Nets', normed=True, alpha=0.5)
plt.xlabel('Point each team')
plt.ylabel('Frequency')
plt.title('Knicks Vs Nets (NBA 2014)', fontsize=20)
plt.show()
plt.clf()

# No.5
plt.figure(figsize=(12, 5))
sns.boxplot(data=nba_2010, x=nba_2010['fran_id'], y=nba_2010['pts'])
plt.title('Franchise Vs Points Score per Game (NBA Team 2010)')
plt.show()
plt.clf()

# No.6
location_result_freq = pd.crosstab(nba_2010['game_result'], nba_2010['game_location'])
print(location_result_freq)

# No.7
location_result_prop = location_result_freq / len(nba_2010)
print(location_result_prop)

# No.8
chi2, pval, dov, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

# No.9
cov_forecast_point = np.cov(nba_2010['forecast'], nba_2010['point_diff'])
print(cov_forecast_point)

# No.10
corr_forecast_point, p = pearsonr(nba_2010['forecast'], nba_2010['point_diff']) 
print(corr_forecast_point)

# No.11
plt.figure(figsize=(10, 5))
plt.scatter(x=nba['forecast'], y=nba['point_diff'])
plt.xlabel('Forecasted Win Probability')
plt.ylabel('Point Dofferential')
plt.show()

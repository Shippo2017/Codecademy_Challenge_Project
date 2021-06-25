import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

# Combining multiple File
df = glob.glob('states*.csv')

df_list = []
for filename in df:
  data = pd.read_csv(filename)
  df_list.append(data)

us_census = pd.concat(df_list)
# print(us_census)
# print(us_census.dtypes)
# print(us_census.columns)

# Cleaning Data
us_census.Income = us_census.Income.replace('[\$,]', '', regex=True)
us_census.Income = pd.to_numeric(us_census.Income)
# print(us_census.Income.head())

gender_split = us_census.GenderPop.str.split('_')
us_census['Men'] = gender_split.str.get(0)
us_census['Women'] = gender_split.str.get(1)
# print(us_census[['GenderPop', 'Men', 'Women']].head())

us_census.Men = us_census.Men.str[:-1]
us_census.Men = pd.to_numeric(us_census.Men)
us_census.Women = us_census.Women.str[:-1]
us_census.Women = pd.to_numeric(us_census.Women)
# print(us_census[['State', 'Men', 'Women']].head())

us_census = us_census.fillna(value={'Women': us_census.TotalPop - us_census.Men})
# print(us_census.Women)

us_census.Hispanic = us_census.Hispanic.replace('[\%,]', '', regex=True)
us_census.Hispanic = pd.to_numeric(us_census.Hispanic)
us_census.White = us_census.White.replace('[\%,]', '', regex=True)
us_census.White = pd.to_numeric(us_census.White)
us_census.Black = us_census.Black.replace('[\%,]', '', regex=True)
us_census.Black = pd.to_numeric(us_census.Black)
us_census.Native = us_census.Native.replace('[\%,]', '', regex=True)
us_census.Native = pd.to_numeric(us_census.Native)
us_census.Asian = us_census.Asian.replace('[\%,]', '', regex=True)
us_census.Asian = pd.to_numeric(us_census.Asian)
us_census.Pacific = us_census.Pacific.replace('[\%,]', '', regex=True)
us_census.Pacific = pd.to_numeric(us_census.Pacific)

us_census.fillna(value={
  'Hispanic': us_census.Hispanic.mean(),
  'White': us_census.White.mean(),
  'Black': us_census.Black.mean(),
  'Native': us_census.Native.mean(),
  'Asian': us_census.Asian.mean(),
  'Pacific': us_census.Pacific.mean()
}, inplace=True)

# Check Duplicates
duplicates = us_census.duplicated(subset=['State'])
# print(duplicates)
# print(duplicates.value_counts())

us_census = us_census.drop_duplicates(subset=['State'])
print(us_census)


# Scatter Plot
plt.scatter(us_census.Women, us_census.Income)
plt.title('US Census Data Women Vs Income')
plt.xlabel('Women')
plt.ylabel('Income')

plt.show()
plt.cla()

print(us_census.columns)

# Histogram Race
plt.figure(figsize=(15,15))

fig, ax = plt.subplots(2,3)
ax[0][0].hist(us_census.Hispanic, color='#A52A2A')
ax[0][1].hist(us_census.White, color='#00CED1')
ax[0][2].hist(us_census.Black, color='#9400D3')
ax[1][0].hist(us_census.Native, color='#A52A2A')
ax[1][1].hist(us_census.Asian, color='#00CED1')
ax[1][2].hist(us_census.Pacific, color='#9400D3')

ax[0][0].set(title='Hispanic', xlabel='% Population', ylabel='Number of state')
ax[0][1].set(title='White', xlabel='% Population', ylabel='Number of state')
ax[0][2].set(title='Black', xlabel='% Population', ylabel='Number of state')
ax[1][0].set(title='Native', xlabel='% Population', ylabel='Number of state')
ax[1][1].set(title='Asian', xlabel='% Population', ylabel='Number of state')
ax[1][2].set(title='Pacific', xlabel='% Population', ylabel='Number of state')

fig.suptitle('Histogram From Different Race', y=1.05, fontsize=15)
fig.tight_layout()

plt.show()
plt.clf()

# 15 
hispanic = us_census.Hispanic.sum()
white = us_census.White.sum()
black = us_census.Black.sum()
native = us_census.Native.sum()
asian = us_census.Asian.sum()
pacific = us_census.Pacific.sum()

race_types = ['hispanic', 'white', 'black', 'native', 'asian', 'pacific']
races = [hispanic, white, black, native, asian, pacific]
plt.pie(races, labels=race_types, autopct='%d%%')
plt.title('Race Distribution in US')
plt.axis('equal')
plt.show()

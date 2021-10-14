import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

# No.5
df["Total Goals"]= df['Home Team Goals'] + df['Away Team Goals']

# No.6-11
sns.set_style('whitegrid')
sns.set_context('poster', font_scale=0.8)
f, ax = plt.subplots(figsize=(15,5))
ax = sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title('World Cup Data With Seaborn')
plt.show()
plt.clf()

# No.12
print(df_goals.head())

# No.13
sns.set_style('whitegrid')
sns.set_context('notebook', font_scale=1.25)
f, ax2 = plt.subplots(figsize=(15,5))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Goals Visualization')
plt.show()

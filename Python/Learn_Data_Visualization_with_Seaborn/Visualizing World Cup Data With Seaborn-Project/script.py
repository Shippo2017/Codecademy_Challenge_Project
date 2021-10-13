import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('WorldCupMatches.csv')
df_goals = pd.read_csv('goals.csv')

df["Total Goals"]= df['Home Team Goals'] + df['Away Team Goals']
# print(df_goals.head())

sns.set_style('whitegrid')
sns.set_context('notebook', font_scale=1)

f, ax = plt.subplots(figsize=(12,7))
ax = sns.barplot(data=df, x='Year', y='Total Goals')
ax.set_title('World Cup Data With Seaborn')

f, ax2 = plt.subplots(figsize=(12,7))
ax2 = sns.boxplot(data=df_goals, x='year', y='goals', palette='Spectral')
ax2.set_title('Goals Visualization')

plt.show()

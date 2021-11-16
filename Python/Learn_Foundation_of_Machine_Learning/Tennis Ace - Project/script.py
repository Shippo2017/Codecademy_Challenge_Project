import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
print(df.head())

print(len(df))
print(df.columns)
print(df.describe())
print(df.isna().any())
print(df.Player.nunique())

# Add win-loss ratios
df['win_loss_ratio'] = df.apply(lambda x: float(x.Wins) / x.Losses if x.Losses > 0 else 0, axis=1)
print('Avalaible Stats \n')
for stat in df.columns.values:
  print(stat)

# Group assume values are either related to player ID, variables, perfomance indicators
players_id = ['Player', 'Year']
variables = ['FirstServe', 'FirstServePointsWon', 'FirstServeReturnPointsWon', 'SecondServePointsWon', 'SecondServeReturnPointsWon',\
            'Aces', 'BreakPointsConverted', 'BreakPointsFaced', 'BreakPointsOpportunities', 'BreakPointsSaved', 'DoubleFaults',\
            'ReturnGamesPlayed', 'ReturnGamesWon', 'ReturnPointsWon', 'ServiceGamesPlayed', 'ServiceGamesWon', 'TotalPointsWon',\
            'TotalServicePointsWon', 'Losses', 'win_loss_ratio']
perform_indicators = ['Wins', 'Losses', 'Winnings', 'Ranking']

# perform exploratory analysis here:
print(df.corr())

# # uncomment below to see result

# for var in variables:
#   sns.set_style('darkgrid')
#   sns.set_palette('bright')

#   plt.subplots(2, 2, figsize=(15, 10))

#   # Ranking
#   ax = plt.subplot(2, 2, 1)
#   plt.scatter(df[var], df['Ranking'], alpha=0.4)
#   ax.set_xlabel(var)
#   ax.set_ylabel('Ranking')
#   ax.set_title('Player Ranking Against {}'.format(var))

#   # Winnings
#   ax = plt.subplot(2, 2, 2)
#   plt.scatter(df[var], df['Winnings'], alpha=0.4)
#   ax.set_xlabel(var)
#   ax.set_ylabel('Winning')
#   ax.set_title('Player Winnings Against {}'.format(var))

#   # Wins
#   ax = plt.subplot(2, 2, 3)
#   plt.scatter(df[var], df['Wins'], alpha=0.4)
#   ax.set_xlabel(var)
#   ax.set_ylabel('Wins')
#   ax.set_title('Player Wins Against {}'.format(var))

#   # Win-Loss Ratio
#   ax = plt.subplot(2, 2, 4)
#   plt.scatter(df[var], df['win_loss_ratio'], alpha=0.4)
#   ax.set_xlabel(var)
#   ax.set_ylabel('Win-Loss Ratio')
#   ax.set_title('Player Win-Loss Ratio Against {}'.format(var))

#   plt.tight_layout() #distance for each plot
#   plt.show()
#   plt.clf()


## perform single feature linear regressions here:

# single feature linear regressions (FirstServeReturnPointsWon)

# Select features and value to predict
features = df[['FirstServeReturnPointsWon']]
winnings = df[['Winnings']]

# train, test, split data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size=0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train, winnings_train)

# score model on test data
print('Predicting winning with FirstServeReturnPointsWon Test Score : ', model.score(features_test, winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot prediction agains actual winnings
plt.scatter(winnings_test, winnings_prediction, alpha=0.4)
plt.title('Predicted Winning vs. Actual Winning -1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

# single feature linear regressions (BreakPointsOpportunities)

# Select features and value to predict
features = df[['BreakPointsOpportunities']]
winnings = df[['Winnings']]

# train, test, split data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size=0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train, winnings_train)

# score model on test data
print('Predicting winning with BreakPointsOpportunities Test Score : ', model.score(features_test, winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot prediction agains actual winnings
plt.scatter(winnings_test, winnings_prediction, alpha=0.4)
plt.title('Predicted Winning vs. Actual Winning -1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()


## perform two feature linear regressions here:

# Select features and value to predict
features = df[['FirstServeReturnPointsWon', 'BreakPointsOpportunities']]
winnings = df[['Winnings']]

# train, test, split data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size=0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train, winnings_train)

# score model on test data
print('Predicting winning with 2 Features Test Score : ', model.score(features_test, winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot prediction agains actual winnings
plt.scatter(winnings_test, winnings_prediction, alpha=0.4)
plt.title('Predicted Winning vs. Actual Winning -2 Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()


## perform multiple feature linear regressions here:

features = df[['FirstServe', 'FirstServePointsWon', 'FirstServeReturnPointsWon', 'SecondServePointsWon', 'SecondServeReturnPointsWon',\
            'Aces', 'BreakPointsConverted', 'BreakPointsFaced', 'BreakPointsOpportunities', 'BreakPointsSaved', 'DoubleFaults',\
            'ReturnGamesPlayed', 'ReturnGamesWon', 'ReturnPointsWon', 'ServiceGamesPlayed', 'ServiceGamesWon', 'TotalPointsWon',\
            'TotalServicePointsWon']]
winnings = df[['Winnings']]

# train, test, split data
features_train, features_test, winnings_train, winnings_test = train_test_split(features, winnings, train_size=0.8)

# create and train model on training data
model = LinearRegression()
model.fit(features_train, winnings_train)

# score model on test data
print('Predicting winning with Multiple Features Test Score : ', model.score(features_test, winnings_test))

# make predictions with model
winnings_prediction = model.predict(features_test)

# plot prediction agains actual winnings
plt.scatter(winnings_test, winnings_prediction, alpha=0.4)
plt.title('Predicted Winning vs. Actual Winning -Multiple Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

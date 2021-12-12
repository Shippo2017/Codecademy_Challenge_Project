def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier

income_data = pd.read_csv('income.csv', header=0, delimiter=", ")
print(income_data.head())
print(income_data.iloc[0])

# Changing the type
income_data['sex-int'] = income_data['sex'].map({'Male':1, "Female":0})

# checking data
print(income_data['native-country'].value_counts())

income_data['country-int'] = income_data['native-country'].apply(lambda x: 0 if x == 'United-States' else 1)

# Format The Data For Scikit-learn
labels = income_data['income']
many_data = income_data[["age", "capital-gain", "capital-loss", "hours-per-week", "sex-int", "country-int"]]

train_data, test_data, train_labels, test_labels = train_test_split(many_data, labels, random_state=1)

# Create The Random Forest
forest = RandomForestClassifier(random_state=1)
forest.fit(test_data, test_labels)
score = forest.score(test_data, test_labels)
print(score)
print(list(zip(["age", "capital-gain", "capital-loss", "hours-per-week", "sex"],forest.feature_importances_)))

# Single Tree
classifier = tree.DecisionTreeClassifier(random_state=1)
classifier.fit(train_data, train_labels)
score = classifier.score(test_data, test_labels)
print('\n' ,score)
print(list(zip(["age", "capital-gain", "capital-loss", "hours-per-week", "sex"],classifier.feature_importances_)))

import codecademylib3_seaborn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

flags = pd.read_csv('flags.csv', header=0)
print(flags.head())
print(flags.columns)

# Creating data and labels
labels = flags[['Landmass']]
# data = flags[['Red', 'Green', 'Blue', 'Gold', 'White', 'Black', 'Orange']]
data = flags[["Red", "Green", "Blue", "Gold","White", "Black", "Orange",
 "Circles", "Crosses","Saltires","Quarters","Sunstars", "Crescent","Triangle"]]

train_data,  test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1)

# Make and test the model
# tree = DecisionTreeClassifier(random_state=1)
# tree.fit(train_data, train_labels)
# print(tree.score(test_data, test_labels))

# Tuning the model
scores = []
for i in range(1,21):
  tree = DecisionTreeClassifier(random_state=1, max_depth=i)
  tree.fit(train_data, train_labels)
  score = tree.score(test_data, test_labels)
  scores.append(score)
  print(i, score)

plt.plot(range(1, 21), scores)
plt.xlabel('Depth')
plt.ylabel('%')
plt.show()
plt.clf()

# Extensions
labels_2 = flags['Language']
data_2 = flags[['Landmass', 'Zone', 'Area', 'Population']]

train_data, test_data, train_labels, test_labels = train_test_split(data_2, labels_2, random_state=1)

scores = []
for i in range(1,11):
    tree = DecisionTreeClassifier(random_state=1, max_depth=i, max_leaf_nodes=10)
    tree.fit(train_data, train_labels)
    score = tree.score(test_data, test_labels)
    scores.append(score)
print(scores)
    
plt.plot(range(1,11), scores)
plt.xlabel('Depth')
plt.ylabel('%')
plt.show()
plt.clf()

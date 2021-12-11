import codecademylib3_seaborn
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from svm_visualization import draw_boundary
from players import aaron_judge, jose_altuve, david_ortiz

# Create the labels
print(aaron_judge.columns)
print('\n', aaron_judge.description.unique())
print('\n', aaron_judge.type.unique())

def find_strike_zone(dataset, athlete_name):
  # convert 'S' : 1, 'B':0
  dataset['type'] = dataset['type'].map({'S':1, 'B':0})
  # print('\n', aaron_judge.type.unique())

  # Plotting the pitches
  # print('\n', aaron_judge['plate_x'])
  # drop Nan
  dataset = dataset.dropna(subset = ['plate_x', 'plate_z', 'type'])

  fig, ax = plt.subplots()
  plt.scatter(
    x=dataset['plate_x'],
    y=dataset['plate_z'],
    c=dataset['type'],
    cmap = plt.cm.coolwarm,
    alpha=0.25)
  plt.title(f'{athlete_name.title()} strike zone')
  plt.xlabel('plate_x')
  plt.ylabel('plate_z')

  # Building the SVM
  training_set, validation_set = train_test_split(dataset, random_state=1)
  classifier = SVC(kernel='rbf', gamma=3, C=1)
  classifier.fit(training_set[['plate_x', 'plate_z']], training_set['type'])

  # Optimizing the SVM
  score = classifier.score(validation_set[['plate_x', 'plate_z']], validation_set['type'])
  print(f'\n{athlete_name.title()}', score)

  # call draw_boundary function
  ax.set_ylim(-2, 6)
  ax.set_xlim(-3, 3)
  draw_boundary(ax, classifier)

  plt.show()
  plt.clf()

find_strike_zone(aaron_judge, 'Aaron Judge')
find_strike_zone(jose_altuve, 'Jose Altuve')
find_strike_zone(david_ortiz, 'David Ortiz')

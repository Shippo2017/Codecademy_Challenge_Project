import codecademylib3_seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the passenger data
passengers = pd.read_csv('passengers.csv')

# clean data
# Update sex column to numerical
passengers['Sex'] = passengers['Sex'].map({'female':1, 'male':0})

# Fill the nan values in the age column
print(passengers['Age'].values)
passengers['Age'].fillna(inplace=True, value=passengers['Age'].mean())

# Create a first class column
passengers['FirstClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 1 else 0)

# Create a second class column
passengers['SecondClass'] = passengers['Pclass'].apply(lambda x: 1 if x == 2 else 0)
print(passengers.head())

# Select and Split the data
# Select the desired features
features = passengers[['Sex', 'Age', 'FirstClass', 'SecondClass']]
survived = passengers['Survived']

# Perform train, test, split
train_features, test_features, train_labels, test_labels = train_test_split(
  features, 
  survived, 
  test_size=0.2, 
  random_state=1
  )

# Normalize the data
# Scale the feature data so it has mean = 0 and standard deviation = 1
scaler = StandardScaler()
train_features = scaler.fit_transform(train_features)
test_features = scaler.transform(test_features)

# Create and Evaluate the Model
# Create and train the model
model = LogisticRegression()
model.fit(train_features, train_labels)

# Score the model on the train data
print(model.score(train_features, train_labels))

# Score the model on the test data
print(model.score(test_features, test_labels))

# Analyze the coefficients
print(list(zip(['Sex', 'Age', 'FirstClass', 'SecondClass'], model.coef_[0])))

# Predicted the model
# Sample passenger features
Jack = np.array([0.0,20.0,0.0,0.0])
Rose = np.array([1.0,17.0,1.0,0.0])
You = np.array([1.0,34.0,0.0,1.0])

# Combine passenger arrays
sample_passengers = np.array([Jack, Rose, You])

# Scale the sample passenger features
sample_passengers = scaler.transform(sample_passengers)
print(sample_passengers)

# Make survival predictions!
print(model.predict(sample_passengers))
probabilities = model.predict_proba(sample_passengers)
print(probabilities)

# Plot
# plot
x = range(len(sample_passengers))
y = probabilities[:,1]
plt.bar(
    x, 
    y * 100
)
plt.xticks(np.arange(3), ('Jack', 'Rose', 'You'))
plt.yticks(np.arange(0, 101, 25), ('0%', '25%', '50%', '75%', '100%'))
plt.title('Chance to survive the titanic', weight='bold', fontsize=15)
plt.show()

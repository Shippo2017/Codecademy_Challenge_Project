import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
# print(digits)
# print(digits.DESCR)
print(digits.data)
print(digits.target)

# Visualize the image at index [100]
plt.gray()
plt.matshow(digits.images[100])
plt.show()

print(digits.target[100])

#  take a look at 64 sample images
fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

for i in range(64):
  # Initialize the subplots: add a subplot in the grid of 8 by 8, at the i+1-th position
  ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])

  # Display an image at the i-th position
  ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')

  # Label the image with the target value
  ax.text(0, 7, str(digits.target[i]))

plt.show()
plt.clf()

# K-Means Clustering
model = KMeans(n_clusters=10, random_state=43)
model.fit(digits.data)

# Visualizing after K-Means
fig = plt.figure(figsize=(8,3))
fig.suptitle('Cluster Center Images', fontsize=14, fontweight='bold')

for i in range(10):
  ax = fig.add_subplot(2, 5, 1+i)
  ax.imshow(model.cluster_centers_[i].reshape((8,8)), cmap=plt.cm.binary)

plt.show()

# Testing Your Model
new_samples = np.array([
[0.75,5.33,7.46,7.62,6.70,3.50,0.53,0.00,3.35,7.62,4.41,3.20,6.01,7.62,6.45,0.38,0.37,1.90,0.00,0.00,0.00,2.41,7.62,2.89,0.00,0.00,0.00,0.00,0.00,0.15,7.23,4.34,0.00,0.00,0.00,0.00,0.00,0.90,7.24,4.41,0.76,6.54,7.62,7.24,4.87,6.78,7.23,1.51,1.97,7.62,7.62,7.62,7.62,7.62,4.70,0.07,0.07,3.27,3.81,3.43,2.04,5.32,7.62,5.33],
[0.00,0.00,0.00,0.60,2.89,4.04,4.50,0.68,0.00,1.43,5.18,7.62,7.62,7.62,7.55,1.59,1.74,7.54,7.08,4.25,1.36,6.70,4.42,0.00,3.72,7.62,0.99,0.00,0.00,6.85,4.56,0.00,3.80,7.62,0.07,0.00,0.00,6.85,4.56,0.00,2.80,7.62,3.33,0.00,0.00,7.00,4.56,0.00,0.00,5.54,7.62,5.24,4.48,7.62,3.35,0.00,0.00,0.37,4.02,6.63,6.86,5.16,0.37,0.00],
[0.00,4.79,7.47,7.62,7.62,2.50,0.00,0.00,0.00,3.35,3.95,1.37,7.15,4.57,0.00,0.00,0.00,0.00,0.15,2.43,7.31,4.33,0.00,0.00,0.00,0.00,6.01,7.61,7.62,3.49,0.00,0.00,0.00,0.00,2.05,2.67,5.93,6.85,0.15,0.00,0.00,0.00,0.00,0.00,2.58,7.62,1.98,0.00,0.00,0.76,2.67,4.57,6.09,7.62,1.82,0.00,0.00,5.49,7.62,6.93,5.64,3.11,0.00,0.00],
[0.00,0.15,3.27,4.57,4.57,4.57,2.89,0.00,0.68,6.15,7.62,6.32,6.47,7.62,4.87,0.00,3.49,7.62,2.65,0.00,1.98,7.62,2.43,0.00,4.56,6.93,0.00,0.00,0.30,7.39,4.93,0.00,4.56,6.85,0.00,0.00,0.00,4.41,7.46,0.38,4.56,7.00,0.00,0.00,0.00,3.04,7.62,0.76,3.11,7.62,4.54,1.98,1.44,5.62,7.54,0.53,0.07,4.61,7.61,7.61,7.62,7.39,3.33,0.00]
])

new_labels = model.predict(new_samples)
print(new_labels)

for i in range(len(new_labels)):
  if new_labels[i] == 0:
    print(0, ends='')
  elif new_labels[i] == 1:
    print(9, end='')
  elif new_labels[i] == 2:
    print(2, end='')
  elif new_labels[i] == 3:
    print(1, end='')
  elif new_labels[i] == 4:
    print(6, end='')
  elif new_labels[i] == 5:
    print(8, end='')
  elif new_labels[i] == 6:
    print(4, end='')
  elif new_labels[i] == 7:
    print(5, end='')
  elif new_labels[i] == 8:
    print(7, end='')
  elif new_labels[i] == 9:
    print(3, end='')

from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Load the data
emails = fetch_20newsgroups()
print(emails.target_names)

# Exploring the data
emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'])
print(emails.data[5])
print(emails.target[5])

# Making the training data set
train_emails = fetch_20newsgroups(
  categories = ['rec.sport.baseball', 'rec.sport.hockey'],
  subset='train',
  shuffle=True,
  random_state=108
  )

test_emails = fetch_20newsgroups(
  categories = ['rec.sport.baseball', 'rec.sport.hockey'],
  subset='test',
  shuffle=True,
  random_state=108
)


# Counting words
counter = CountVectorizer()
counter.fit(test_emails.data + train_emails.data)

train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)


# Making a Naive Bayes Classifier
classifier = MultinomialNB()
classifier.fit(train_counts, train_emails.target)

print(classifier.score(test_counts, test_emails.target))

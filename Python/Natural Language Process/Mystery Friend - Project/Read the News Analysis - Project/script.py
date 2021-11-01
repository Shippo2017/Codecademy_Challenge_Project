from operator import index
from nltk.util import pr
import pandas as pd
import numpy as np
from articles import articles
from preprocessing import preprocess_text
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

# View artticle
print(articles[:2])

# preprocess article
processed_articles = [preprocess_text(article) for article in articles]

# preprocess_articles = []
# for article in articles:
#     processed_articles.append(preprocess_text[article])

# initialize and fit CountVectorizer
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(processed_articles)

# convert count to tf-idf
transformer = TfidfTransformer(norm=None)
tfidf_scores_transformed = transformer.fit_transform(counts)

# initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm=None)
tfidf_scores = vectorizer.fit_transform(processed_articles)

# check if tf-idf scores are equal
if np.allclose(tfidf_scores_transformed.todense(), tfidf_scores.todense()):
    print(pd.DataFrame({'Are the tf-idf scores the same?':['YES']}))
else:
    print(pd.DataFrame({'Are the tf-idf score the same?':['No, something is wrong :(']}))

# get vocabularies of term
try:
    feature_names = vectorizer.get_feature_names()
except:
    pass

# get index article
try:
    article_index = [f"Article {i+1}" for i in range(len(articles))]
except:
    pass

# create pandas DataFrame with word counts
try:
    df_word_counts = pd.DataFrame(counts.T.todense(), index=feature_names, columns=article_index)
    print(df_word_counts)
except:
    pass

# create pandas DataFrame(s) with tf-idf scores
try:
    df_tf_idf = pd.DataFrame(tfidf_scores_transformed.T.todense(), index=feature_names, columns=article_index)
    print(df_tf_idf)
except:
    pass

try:
    df_tf_idf = pd.DataFrame(tfidf_scores.T.todense(), index=feature_names, columns=article_index)
    print(df_tf_idf)
except:
    pass

# get highest scoring tf-idf term for each article
topics = [df_tf_idf[f'Article {i+1}'].idxmax() for i in range(len(article_index))]

# create pandas DataFrame(s) for articles
try:
    df_articles_topics = pd.DataFrame({'Topics' : topics}, index=article_index)
    print(df_articles_topics)
except:
    pass

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# print(df.dtypes)

# list of all column headers
columns = df.columns.tolist()

for column in columns:
  # print(column)
  sns.countplot(df[column], order=df[column].value_counts().index)
  plt.title(column + ' Value Count')
  plt.xticks(rotation=30, fontsize=10)
  plt.xlabel(column, fontsize=12)
  plt.show()
  plt.clf()

# Extention
# turn any bar graph with less than six bars into a pie chart
for column in columns:
    if df[column].nunique() <= 5:
        continue
    else:
        plt.figure(figsize=(10,5))
        df[column].value_counts().plot(kind='pie', autopct='%0.1f%%', shadow=True)
        # rotare value labels
        plt.axis('equal')
        plt.title(column + " value Counts")
        plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
        plt.show()
        plt.clf()  

# create bar charts using a list comprehension
def bar_graph():
    for column in columns:
        sns.countplot(x=df[column], order=df[column].value_counts().index, palette='pastel')
        # rotare value labels
        plt.xticks(rotation=30, fontsize=10)
        plt.xlabel(column, fontsize=12)
        plt.title(column + " value Counts")
        plt.show()
        plt.clf()

bar_graph()

# remove any graph that finds uninformative
def bar_graph(data, column):
    sns.countplot(x=data[column], order=data[column].value_counts().index, palette='pastel')
    # rotare value labels
    plt.xticks(rotation=30, fontsize=10)
    plt.xlabel(column, fontsize=12)
    plt.title(column + " value Counts")
    plt.show()
    plt.clf()

bar_graph(df, 'Class')
bar_graph(df, 'Population')
bar_graph(df, 'Habitat')
bar_graph(df, 'Cap Surface')
bar_graph(df, 'Cap Color')
bar_graph(df, 'Gill Color')
bar_graph(df, 'Odor')

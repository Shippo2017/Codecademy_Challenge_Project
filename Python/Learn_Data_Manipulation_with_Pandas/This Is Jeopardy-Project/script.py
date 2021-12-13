import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.read_csv('jeopardy.csv')
print(df.head())
print(df.iloc[100])
print(df.columns)

# rename columns
df = df.rename(columns = {"Show Number": "show_num",
                          " Air Date": "air_date", 
                          " Round" : "round", 
                          " Category": "category", 
                          " Value": "value", 
                          " Question":"question", 
                          " Answer": "answer"})
print(df.columns)

# filtering a dataset by a list of words
def filter_data(data, words):
    filter = lambda x : all(word.lower() in x.lower() for word in words)
    return data.loc[data['question'].apply(filter)]

# testing the filter function
filtered = filter_data(df, ['king'])
print('num of questions that contain those words : ', len(filtered['question']))

# andding new column. clean the value count $ and None
df['float_value'] = df['value'].apply(lambda x: float(x[1:].replace(",","")) if x != "None" else 0)
print(df['float_value'].unique())

# mean float value
print('The average value is ', df['float_value'].mean())

# filtering the dataset and finding the average value of those questions
filtered = filter_data(df, ['king', 'england'])
print('the average value of those questions is ',filtered['float_value'].mean())

# a function to find the unique answers of a set of data
def answer_count(data):
    return data['answer'].value_counts()

# testing the function
print(answer_count(filtered))

# extention

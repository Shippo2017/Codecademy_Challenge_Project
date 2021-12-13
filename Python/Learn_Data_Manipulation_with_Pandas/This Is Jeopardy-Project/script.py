import re
import pandas as pd
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_rows', None)

jeopardy_data = pd.read_csv('jeopardy.csv')
# print(jeopardy_data.head())

# print(jeopardy_data.columns)

# Rename Columns
jeopardy_data.rename(columns={
  'Show Number': 'show_num', 
  ' Air Date': 'show_date', 
  ' Round': 'round', 
  ' Category': 'category', 
  ' Value': 'value',
  ' Question': 'question', 
  ' Answer': 'answer'
}, inplace=True)
print(jeopardy_data.columns)

# Lower Category
jeopardy_data['category'] = jeopardy_data['category'].apply(lambda x: x.lower())
# print(jeopardy_data['category'].head())

# No.3
def filter_data(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['question'].apply(filter)]

# No.4
filtered = filter_data(jeopardy_data, ['King', 'England'])
print(filtered['question'])
print(len(filtered['question']))

# Clean up HTLM version 'question'
jeopardy_data['question'] = jeopardy_data['question'].apply(lambda x: re.sub(r'<[^<>*]>', '', x))

# no.5
jeopardy_data['value'] = jeopardy_data['value'].apply(lambda x: float(x[1:].replace(',','')) if x != 'None' else 0)
print(jeopardy_data['value'].unique)

jeopardy_mean = jeopardy_data['value'].mean()
print(jeopardy_mean)

# no.6
def get_answer_counts(data):
  return data['answer'].value_counts()

print(get_answer_counts(filtered))

# Extension (not yet)

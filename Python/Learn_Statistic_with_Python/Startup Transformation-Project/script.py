import codecademylib3
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')
expense_overview = pd.read_csv('expenses.csv')

# code goes here
# Analyzing Revenue and Expenses
print(financial_data.head())

month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']

plt.plot(month, revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
plt.clf()

plt.plot(month, expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()
plt.clf()
print(expense_overview)


# Pie Chart 
expense_categorie = expense_overview['Expense']
proportion = expense_overview['Proportion']
plt.pie(proportion, labels = expense_categorie, autopct = '%0.2f%%')
plt.title('Expenses Categories')
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.clf()

# Pie Chart and Collapsing Categories
expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, 0.08]
plt.pie(proportions, labels = expense_categories, autopct = '%0.2f%%')
plt.title('Expenses Categories')
plt.axis('equal')
plt.tight_layout()
plt.show()
plt.clf()

expense_cut = 'Salary' # answer


# Employee Productivity
employees = pd.read_csv('employees.csv')
print(employees.head())

sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity.head(10))

employees_cut = sorted_productivity.head(100)
print(employees_cut)

transformation = 'standardization' # answer


# Commute Times and Log Transformation
commute_times = employees['Commute Time']
print(commute_times.describe())

commute_times_log = np.log(commute_times)

plt.hist(commute_times_log)
plt.title('Employee Commute Times')
plt.xlabel('Commute Times')
plt.ylabel('Frequency')
plt.show()
plt.clf()


# Extra
# Using sklearn
income_productivity = employees[['Salary', 'Productivity']]
print(income_productivity.head())

minmax_scaler = MinMaxScaler()
normalized_data = minmax_scaler.fit_transform(income_productivity)
print(normalized_data)

scaler = StandardScaler()
standardized_data = scaler.fit_transform(income_productivity)
print(standardized_data)

# relation between productivity and income
print('Minimum Salary :', employees['Salary'].min())
print('Lowest Productivity : ', employees['Productivity'].min())
print('\nMaximum Salary : ', employees['Salary'].max())
print('Highest Productivity : ', employees['Productivity'].max())

# scatter plot of Income and productivity

plt.figure(figsize=(10,5))
plt.scatter(x=employees['Salary'], y=employees['Productivity'])
plt.title('Income vs Productivity')
plt.xlabel('Income ($)')
plt.ylabel('Productivity')
plt.show()

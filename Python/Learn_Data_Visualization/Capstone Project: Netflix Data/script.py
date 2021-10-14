#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

netflix_stocks = pd.read_csv('NFLX.csv')
print(netflix_stocks.head(2))

dowjones_stocks = pd.read_csv('DJI.csv')
print(dowjones_stocks.head(2))

netflix_stocks_quarterly = pd.read_csv('NFLX_daily_by_quarter.csv')
print(netflix_stocks_quarterly.head(2))

# rename adj close
# Netflix_stocks 
netflix_stocks.rename(columns={
    'Adj Close': 'Price'
}, inplace=True)

# dowjones_stocks
dowjones_stocks.rename(columns={
    'Adj Close': 'Price'
}, inplace=True)

# netflix_stocks_quarterly
netflix_stocks_quarterly.rename(columns={
    'Adj Close': 'Price'
}, inplace=True)


print(netflix_stocks.head(1))
print(dowjones_stocks.head(1))
print(netflix_stocks_quarterly.head(1))

# Violin Plot for netflix quarterly
sns.color_palette('Pastel1')
sns.set_style('whitegrid')
sns.set_context('talk', rc={'lines.linewidht': .5})

f, ax = plt.subplots(figsize=(10,5))
ax = sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')
ax.set_title('Distribution of 2017 Netflix Stock by Quarter', fontsize=15)
ax.set_xlabel('Business Quarter in 2017')
ax.set_ylabel('Closing Stock Price')

figl = plt.gcf()
plt.show()
figl.savefig('netfli_quarter_2017.png')


# Step 6
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

plt.figure(figsize=(10,5))
plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)
plt.legend(['Actual', 'Estimate'])
plt.xticks(x_positions, chart_labels)
plt.title('Earning Per Share in Cents', fontsize=15)

plt.show()
plt.savefig('netflix_EPS_2017.png')

# Step 7
# The metrics below are in billions of dollars
revenue_by_quarter = [2.79,2.98,3.29,3.7]
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

plt.figure(figsize=(15,5))

# Revenue
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of dataset
d = 4 # Number of sets of bars
w = 0.8 # Width of each bar
bars1_x = [t*element + w*n for element in range(d)]

plt.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2  # This is our second dataset (out of 2)
t = 2  # Number of dataset
d = 4  # Number of sets of bars
w = 0.8 # Width of each bar
bars2_x = [t*element + w*n for element in range(d)]

plt.bar(bars2_x, earnings_by_quarter)


middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]

plt.legend(labels)
plt.title('Summary of Earning and Revenue by Netflix', fontsize=15)
plt.xticks(middle_x, quarter_labels)
plt.xlabel('Business quarter in 2017', fontsize=10)
plt.ylabel('Points')

plt.show()
plt.savefig('netflix_EPS_rev_2017.png')


# Step 8
plt.figure(figsize=(15,5))

# Left plot Netflix
ax1 = plt.subplot(1,2,1)
plt.bar(netflix_stocks['Date'], netflix_stocks['Price'], color='purple')
ax1.set_title('Netflix')
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price')
plt.xticks(rotation=45)

# Right plot Dow Jones
ax2 = plt.subplot(1,2,2)
plt.bar(dowjones_stocks['Date'], dowjones_stocks['Price'])
ax2.set_title('Dow Jones')
ax2.set_xlabel('Date')
ax2.set_ylabel('Stock Price')
plt.xticks(rotation=45)

plt.suptitle('Comparison Netflix Stock vs. Dow Jones Industrial Average 2017', fontsize=20, y=1)
plt.subplots_adjust(wspace=.8, bottom=0.2)
plt.tight_layout()
plt.show()

plt.savefig('netflix_vs_dowjon_2017.png')

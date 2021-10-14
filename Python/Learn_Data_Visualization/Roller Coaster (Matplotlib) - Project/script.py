# Import internal library
import codecademylib3

# 1 
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(wood.head(2))

# load rankings data
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(wood.head(2))

print(wood.describe(include='all'))
print(steel.describe(include='all'))

wood_year = wood.groupby('Year of Rank').Rank.count().reset_index()
steel_year = steel.groupby('Year of Rank').Rank.count().reset_index()

print(steel_year)
print(wood_year)

print(wood['Name'].unique())
print(wood.Park[wood['Name'] == 'El Toro'].unique())

# 2
# Create a function to plot rankings over time for 1 roller coaster
def coaster_ranking(coaster_name, park_name, material):
    if material == 'wood':
        df = wood[(wood['Name'] == coaster_name) & (wood['Park'] == park_name)]
        
    if material == 'steel':
        df = steel[(steel['Name'] == coaster_name) & (steel['Park'] == park_name)]
        
    x_value = df['Year of Rank']
    y_value = df['Rank']
    
    plt.figure(figsize=(10,5))
    ax = plt.subplot()
    plt.plot(x_value, y_value, marker='o', linewidth=2, color='mediumvioletred')
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('Roller Coaster (El Toro) Ranking per Year', fontsize=15)
    ax.invert_yaxis()
    plt.show()
    
plt.clf()
coaster_ranking('El Toro', 'Six Flags Great Adventure', 'wood')


# 3
# Create a plot of El Toro ranking over time
# function to plot rankings over time for 2 roller coasters
def coaster_2_ranking(coaster1_name, park1_name, coaster2_name, park2_name, material):
    df1 = material[(material['Name'] == coaster1_name) & (material['Park'] == park1_name)]
    df2 = material[(material['Name'] == coaster2_name) & (material['Park'] == park2_name)]
    
    fig, ax = plt.subplots()
    ax.plot(df1['Year of Rank'], df1['Rank'], marker='o', linewidth=2, color='mediumvioletred')
    ax.plot(df2['Year of Rank'], df2['Rank'], marker='o', linewidth=2, color='cyan')
    ax.invert_yaxis()   
                
    plt.xlabel('Year')
    plt.ylabel('Ranking')
    plt.title('{} & {} ranking'.format(coaster1_name, coaster2_name), fontsize=15)
    plt.legend(['El Toro', 'Boulder Dash'])   
    plt.show()

# Create a plot of El Toro and Boulder dash hurricanes
coaster_2_ranking('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)
plt.clf()

# 4
# Create a function to plot top n rankings over time
def top_ranking(ranking_df, n):
    top_n_rankings = ranking_df[ranking_df['Rank'] <= n]
    
    fig, ax = plt.subplots(figsize=(10, 5))

    for coaster in set(top_n_rankings['Name']):
        coaster_rankings = top_n_rankings[top_n_rankings['Name'] == coaster]
        ax.plot(coaster_rankings['Year of Rank'], coaster_rankings['Rank'], label=coaster, marker='o')
    
    ax.set_yticks([i for i in range(1,6)])
    ax.invert_yaxis()
    
    plt.title("Top 10 Rankings", fontsize=15)
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend(loc=4)
    plt.show()
    
# Create a plot of top n rankings over time
top_ranking(wood, 5)
plt.clf()

# 5
# load roller coaster data
roller = pd.read_csv('roller_coasters.csv')
print(roller.head())

# 6
# Create a function to plot histogram of column values
def plot_histogram(coaster_df, column_name):
    plt.hist(coaster_df[column_name].dropna(), normed=True, histtype='step', linewidth=2)
    plt.title('Histogram of Roller Coaster {}'.format(column_name))
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()

# Create histogram of roller coaster speed    
plot_histogram(roller, 'speed')
plt.clf()
# Create histogram of roller coaster length
plot_histogram(roller, 'length')
plt.clf()
# Create histogram of roller coaster number of inversions
plot_histogram(roller, 'num_inversions')
plt.clf()


# Create a function to plot histogram of height values
def plot_histogram_height(coaster_df):
    heights = coaster_df[coaster_df['height'] <= 140]['height'].dropna()
    plt.hist(heights)
    plt.title('Histogram of Roller Coaster Height', fontsize=15)
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.show()

# Create a histogram of roller coaster height   
plot_histogram_height(roller)
plt.clf()

# 7
# Create a function to plot inversions by coaster at park
def plot_inversion_by_coaster(coaster_df, park_name):
    park_coasters = coaster_df[coaster_df['park'] == park_name]
    park_coasters = park_coasters.sort_values('num_inversions', ascending=False)
    coaster_names = park_coasters['name']
    number_inversions = park_coasters['num_inversions']
    
    plt.figure(figsize=(15, 5))
    plt.bar(range(len(number_inversions)), number_inversions)
    
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=45)
    
    plt.title('Number of Inversions per Coaster at {}'.format(park_name))
    plt.xlabel('Roller Coaster')
    plt.ylabel('# of Inversions')
    plt.show()
    
# Create barplot of inversions by roller coasters
plot_inversion_by_coaster(roller, 'Six Flags Magic Mountain')
plt.clf()

# 8
# Create a function to plot a pie chart of status.operating
def pie_chart_status(coaster_df):
    operating_coasters = coaster_df[coaster_df['status'] == 'status.operating']
    closed_coasters = coaster_df[coaster_df['status'] == 'status.closed.definitely']
    num_operating_coasters = len(operating_coasters)
    num_closed_coasters = len(closed_coasters)
    status_count = [num_operating_coasters, num_closed_coasters]
    
    plt.figure(figsize=(10,5))
    plt.pie(status_count, autopct='%0.1f%%', labels=['Operating', 'Closed'])
    plt.axis('equal')
    plt.title('Current condition of Roller Coasters', fontsize=15)
    plt.show()

# Create pie chart of roller coasters
pie_chart_status(roller)
plt.clf()

# 9
# Create a function to plot scatter of any two columns
def scatter_plot(coaster_df, column_x, column_y):
    plt.scatter(coaster_df[column_x], coaster_df[column_y])
    plt.title('Scatter Plot of {} vs. {}'.format(column_x, column_y))
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.show()
    
# Create a function to plot scatter of speed vs height
def scatter_plot_height_speed(coaster_df):
    coaster_df = coaster_df[coaster_df['height'] < 140]
    
    plt.figure(figsize=(10,5))
    plt.scatter(coaster_df['height'], coaster_df['speed'])
    plt.title('Scatter Plot of Speed vs. Height')
    plt.xlabel('Height')
    plt.ylabel('Speed')
    plt.show()
    

# Create a scatter plot of roller coaster height by speed
scatter_plot_height_speed(roller)
plt.clf()


# Extra (On The Way!!!)


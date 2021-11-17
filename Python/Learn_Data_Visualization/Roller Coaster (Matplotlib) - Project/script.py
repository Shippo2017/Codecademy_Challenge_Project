# Import internal library
import codecademylib3

# 1
# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2
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

# 3
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


# 4
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

# 5
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

# 6
# load roller coaster data
roller = pd.read_csv('roller_coasters.csv')
print(roller.head())

# clean data
# Check null
print(roller.isnull().sum())

# drop null
roller = roller.dropna()

# check data
print(roller.describe())

# select rows which is non-zero
roller_coaster = roller.loc[(roller.speed != 0) & (roller.height != 0) & (roller.length != 0)]
print(roller_coaster.describe())

# 7
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

# 8
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

# 9
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

# 10
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


# Extra

# What roller coaster seating type is most popular? And do different seating types result in higher/faster/longer roller coasters?

# the most popular seating type
print('The most popular seating type :')
print(roller_coaster['seating_type'].value_counts()[:10].reset_index())

# Different seating types result in higher/faster/longer in roller coaster
def plot_seating_type(dataset, column):
    fig, ax = plt.subplots(figsize=(10,5))
    ax = sns.barplot(data=dataset, x='seating_type', y=column, palette='bright')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    ax.set_title(f'Different Seating Type vs. {column.title()}', weight='bold')
    ax.set_xlabel('Seating Type')
    ax.set_ylabel(column.title())
    plt.show()

# Seating type vs Speed
plot_seating_type(roller_coaster, 'speed')
plt.clf()
#seating type vs height
plot_seating_type(roller_coaster, 'height')  
plt.clf()
# Seating type vs length
plot_seating_type(roller_coaster, 'length')
plt.clf()


# Do roller coaster manufacturers have any specialties (do they focus on speed, height, seating type, or inversions)?

# num of manufacturer
print('Num of manufacturers :')
print(roller_coaster.manufacturer.nunique())

# 10 manufacturers constructed most roller coaster
print('Manufacturers constructed the most roller coaster :')
print(roller_coaster['manufacturer'].value_counts()[:10].reset_index())

# manufacturers have any specialities (on speed and height)
def plot_manufacturers(dataset, column):
    manufacturers = dataset[dataset['manufacturer'] == column]
    speed = manufacturers.speed.values
    height = manufacturers.height.values
    
    fig, ax = plt.subplots(figsize=(10,5))
    plt.scatter(x=speed, y=height, alpha=0.5)
    
    ax.set_title(f'Roller Coaster manufacturer by {column.title()}', weight='bold')
    ax.set_xlabel('Speed')
    ax.set_ylabel('Height')
    plt.show()

# Manufacturer by Vekoma
plot_manufacturers(roller_coaster, 'Vekoma')
plt.clf()
# Manufacturer by Intamin
plot_manufacturers(roller_coaster, 'Intamin')
plt.clf()
# Manufacturer by B&M
plot_manufacturers(roller_coaster, 'B&M')
plt.clf()

# manufacturers have any specialities (on seating type and inversions)
def manufacturer_seating_inversions(dataset, column):
    
    manufacturers = dataset[dataset['manufacturer'] == column]
    
    # filtered by seating_type dataset
    seating_types = manufacturers.groupby('seating_type').name.count().reset_index(name='count')
    
     # filtered by num_inversions dataset
    invers_num = manufacturers.groupby('num_inversions').name.count().reset_index(name='count')
    
    plt.figure(figsize=(15, 5), dpi=150)
    
    # plot a bar chart of the manufacturer's coasters categoried by seating type
    ax = plt.subplot(1,2,1)
    # plt.subplots_adjust(wspace=0.2)
    x = range(len(seating_types['seating_type'].values))
    ax.bar(x, seating_types['count'], color='cyan') 
    ax.set_xlabel('Seating Type')
    ax.set_ylabel('Count')
    ax.set_xticks(x)
    ax.set_xticklabels(seating_types['seating_type'], rotation=45)
    
    # plot a bar chart of the manufacturer's coasters categoried by inversion numbers
    ax = plt.subplot(1,2,2)
    x1 = range(len(invers_num['num_inversions'].values))
    ax.bar(x1, invers_num['count'], color='magenta') 
    ax.set_xlabel('Num of Inversions')
    ax.set_ylabel('Count')
    ax.set_xticks(x1)
    ax.set_xticklabels(invers_num['num_inversions'], rotation=15)
    
    plt.suptitle(f'Manufacturer by {column.title()}', weight='bold', fontsize=15)
    plt.show()

# Manufacturer by Vekoma
manufacturer_seating_inversions(roller_coaster, 'Vekoma')
plt.clf()
# Manufacturer by Intamin
manufacturer_seating_inversions(roller_coaster, 'Intamin')
plt.clf()
# Manufacturer by B&M
manufacturer_seating_inversions(roller_coaster, 'B&M')
plt.clf()

# Do amusement parks have any specialties?

# check the top 5 parks have most roller coasters
print('The top 5 parks have most roller coasters :')
print(roller_coaster['park'].value_counts()[:5].reset_index())

# The highest roller coaster in the park
print('The highest (meters) roller coaster in the park :')
print(roller_coaster['height'].max())

# the name of park that has hihgest coaster
print('Parks where the highest roller coasters are :')
print(roller_coaster.loc[roller_coaster['height'] == 902.0, 'park'].value_counts().reset_index())

print(roller_coaster[(roller_coaster['height'] == 902)])

# The fastest roller coaster in the park
print('The fastest (kilometers/hours) roller coaster in the park :')
print(roller_coaster['speed'].max())

# the name of park that has fastest coaster
print('Parks where the fastest roller coasters are :')
print(roller_coaster[(roller_coaster['speed'] == 240)])

# The longest roller coaster
print('The longest (meters) roller coaster in the park :')
print(roller_coaster['length'].max())

# the name of park that has longest coaster
print('Parks where the longest roller coasters are :')
print(roller_coaster[(roller_coaster['length'] == 2479)])

# park specialities 
def park_specialities(dataset, column):
    park_coasters = dataset[dataset['park'] == column]
    seating_types = park_coasters.groupby('seating_type').name.count().reset_index(name='count')
    invers_num = park_coasters.groupby('num_inversions').name.count().reset_index(name='count')
    
    plt.figure(figsize=(13, 5), dpi=150)
    
    # plot a scatter of park specialities (height and speed)
    ax3 = plt.subplot(2,1,1)
    plt.subplots_adjust(hspace=0.5)
    speed = park_coasters.speed.values
    height = park_coasters.height.values
    
    ax3.scatter(speed, height, alpha=0.4, color='magenta') 
    ax3.set_xlabel('Speed')
    ax3.set_ylabel('Height')
  
    
    # plot a bar graph of park specialities (height and speed)
    ax = plt.subplot(2,2,3)
    x = range(len(seating_types['seating_type'].values))
    ax.bar(x, seating_types['count'], color='cyan') 
    ax.set_xlabel('Seating Type')
    ax.set_ylabel('Count')
    ax.set_xticks(x)
    ax.set_xticklabels(seating_types['seating_type'], rotation=45)
    
    # plot a bar chart of the manufacturer's coasters categoried by inversion numbers
    ax2 = plt.subplot(2,2,4)
    x1 = range(len(invers_num['num_inversions'].values))
    ax2.bar(x1, invers_num['count'], color='magenta') 
    ax2.set_xlabel('Num of Inversions')
    ax2.set_ylabel('Count')
    ax2.set_xticks(x1)
    ax2.set_xticklabels(invers_num['num_inversions'], rotation=15)
    
    plt.suptitle(f'Amusent Park {column.title()}', weight='bold', fontsize=15)
    plt.show()

# Six Flags Magic Mountain Park
park_specialities(roller_coaster, 'Six Flags Magic Mountain')
plt.clf()
# Foire Park
park_specialities(roller_coaster, 'Foire')
plt.clf()
# Cedar Point Park
park_specialities(roller_coaster, 'Cedar Point')
plt.clf()

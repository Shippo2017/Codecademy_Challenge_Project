# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def convert_recorded_damages(damges):
 # Convert damages data from string to float
  conversion = {"M": 1000000, "B": 1000000000}
  update_damages = []

  for damage in damages:
    if damage == "Damages not recorded":
      update_damages.append(damage)
    elif damage.find("M") != -1:
      update_damages.append(float(damage[0:damage.find("M")]) * conversion["M"])
    elif damage.find("B") != -1:
      update_damages.append(float(damage[0:damage.find("B")]) * conversion["B"])

  return update_damages

# test function by updating damages
damages = convert_recorded_damages(damages)
# print(damages)

# 2 
# Create a Table
def create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, deaths):
  hurricane_dicts = {}
  for i in range(0, len(names)):
    hurricane_dicts[names[i]] = {"Name": names[i],
      "Month": months[i],
      "Year": years[i],
      "Max Sustained Wind": max_sustained_winds[i],
      "Areas Affected": areas_affected[i],
      "Damage": damages[i],
      "Deaths": deaths[i]}

  return hurricane_dicts

# Create and view the hurricanes dictionary
hurricanes = create_hurricanes_table(names, months, years, max_sustained_winds, areas_affected, deaths)
print(hurricanes["Maria"], '\n')

# 3
# Organizing by Year
def hurricane_organize_by_year(hurricanes):
  hurricane_by_year = {}
  for year in hurricanes.values():
    current_year = year["Year"]

    if current_year in hurricane_by_year:
      hurricane_by_year[current_year].append(year)
    else:
      hurricane_by_year[current_year] = [year]

  return hurricane_by_year
  
# create a new dictionary of hurricanes with year and key
hurricane_by_years = hurricane_organize_by_year(hurricanes)
# print(hurricane_by_years[2005], '\n')

# 4
# Counting Damaged Areas
def count_affected_areas(hurricanes):
  count_areas = {}

  for area in hurricanes.values():
    areas = area["Areas Affected"]

    for i in range(0, len(areas)):
      if areas[i] in count_areas:
        count_areas[areas[i]] += 1
      else:
        count_areas[areas[i]] = 1

  return count_areas
# create dictionary of areas to store the number of hurricanes involved in
affected_areas_count = count_affected_areas(hurricanes)
# print(affected_areas_count)

# 5 
# Calculating Maximum Hurricane Count
def most_areas_effected(affected_areas_count):
  max_area = ''
  max_count = 0

  for max in affected_areas_count:
    if affected_areas_count[max] > max_count:
      max_count = affected_areas_count[max]
      max_area = max
  
  return max_count, max_area
# find most frequently affected area and the number of hurricanes involved in
max_areas_count, max_area = most_areas_effected(affected_areas_count)
print("The most affected area by hurricane is "+max_area+" with value of "+str(max_areas_count)+" times.\n")

# 6
# Calculating the Deadliest Hurricane
def most_death(hurricanes):
  hurricane_name = ''
  max_deaths = 0

  for death in hurricanes:
    if hurricanes[death]["Deaths"] > max_deaths:
      max_deaths = hurricanes[death]["Deaths"]
      hurricane_name = death

  return hurricane_name, max_deaths

# find highest mortality hurricane and the number of deaths
hurricane_name, max_deaths = most_death(hurricanes)
print("Hurricane name: "+hurricane_name+", that caused the greatest number of deaths: "+str(max_deaths)+".\n")

# 7
# Rating Hurricanes by Mortality
def rating_mortality_scale(hurricanes):
  hurricane_death_scale = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}

  for mortality in hurricanes:
    death = hurricanes[mortality]["Deaths"]

    if death > mortality_scale[4]:
       hurricane_death_scale[5].append(mortality)
    elif death > mortality_scale[3]:
       hurricane_death_scale[4].append(mortality)
    elif death > mortality_scale[2]:
      hurricane_death_scale[3].append(mortality)
    elif death > mortality_scale[1]:
       hurricane_death_scale[2].append(mortality)
    elif death > mortality_scale[0]:
       hurricane_death_scale[1].append(mortality)
    else:
       hurricane_death_scale[0].append(mortality)

  return hurricane_death_scale

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_death_scale = rating_mortality_scale(hurricanes)
print(hurricane_death_scale, "\n")

# 8 Calculating Hurricane Maximum Damage
def hurricane_max_damage_cost(hurricanes):
  max_hurricane = ''
  max_damage_cost = 0

  for cost in hurricanes:
    if hurricanes[cost]["Damage"] == "Damages not recorded":
      continue
    elif hurricanes[cost]["Damage"] > max_damage_cost:
      max_damage_cost = hurricanes[cost]["Damage"]
      max_hurricane = cost

  return max_hurricane, max_damage_cost 

# find highest damage inducing hurricane and its total cost
max_hurricane, max_damage_cost = hurricane_max_damage_cost(hurricanes)
print("The greates hurricanes "+max_hurricane+" costly "+str(max_damage_cost))

# 9
# Rating Hurricanes by Damage
def hurricane_damage_scale(hurricanes):
  hurricane_by_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

  for damage in hurricanes:
    damages = hurricanes[damage]["Damage"]

    if damages == "Damages not recorded":
      continue
    elif damages > damage_scale[4]:
      hurricane_by_damage[5].append(damage)
    elif damages > damage_scale[3]:
      hurricane_by_damage[4].append(damage)
    elif damages > damage_scale[2]:
      hurricane_by_damage[3].append(damage)
    elif damages > damage_scale[1]:
      hurricane_by_damage[2].append(damage)
    elif damages > damage_scale[0]:
      hurricane_by_damage[1].append(damage)
    else:
      hurricane_by_damage[0].append(damage)

  return hurricane_by_damage
# categorize hurricanes in new dictionary with damage severity as key
hurricane_by_damage = hurricane_damage_scale(hurricanes)
print(hurricane_by_damage)

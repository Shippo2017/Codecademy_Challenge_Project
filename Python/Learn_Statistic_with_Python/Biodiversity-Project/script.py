import codecademylib
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

# Loading the Data
species = pd.read_csv('species_info.csv')
# print species.head()

# Inspecting the DataFrame
species_count = len(species)

species_type = species.category.unique()

conservation_statuses = species.conservation_status.unique()

# Analyze Species Conservation Status
conservation_counts = species.groupby('conservation_status').scientific_name.count().reset_index()
# print conservation_counts

# Analyze Species Conservation Status II
species.fillna('No Intervention', inplace = True)

conservation_counts_fixed = species.groupby('conservation_status').scientific_name.count().reset_index()

# Plotting Conservation Status by Species
protection_counts = species.groupby('conservation_status')\
    .scientific_name.count().reset_index()\
    .sort_values(by='scientific_name')
    
plt.figure(figsize=(10, 4))
ax = plt.subplot()
plt.bar(range(len(protection_counts)),
       protection_counts.scientific_name.values)
ax.set_xticks(range(len(protection_counts)))
ax.set_xticklabels(protection_counts.conservation_status.values)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
labels = [e.get_text() for e in ax.get_xticklabels()]
print ax.get_title()
plt.show()

species['is_protected'] = species.conservation_status != 'No Intervention'

category_counts = species.groupby(['category', 'is_protected'])\
                         .scientific_name.count().reset_index()
# print category_counts.head()

category_pivot = category_counts.pivot(columns='is_protected', index='category', values='scientific_name').reset_index()

category_pivot.columns = ['category', 'not_protected', 'protected']

category_pivot['percent_protected'] = category_pivot.protected / (category_pivot.protected + category_pivot.not_protected)

print category_pivot.head()

contingency_mammal_bird = [
  [30, 146], 
  [75, 413]]

_, pval_mammal_bird, _, _ = chi2_contingency(contingency_mammal_bird)
print(pval_mammal_bird)

contingency_reptile_mammal = [
  [5, 73],
  [30, 146]
]

_, pval_reptile_mammal, _, _ = chi2_contingency(contingency_reptile_mammal)
print(pval_reptile_mammal)



# In Search of Sheep
species['is_sheep'] = species.common_names.apply(lambda x: 'Sheep'in x)
# print(species.head())

species_is_sheep = species[species.is_sheep == True]
# print(species_is_sheep)

sheep_species = species_is_sheep[(species_is_sheep.category == 'Mammal')]
print(sheep_species)

# Merging Sheep and Observation
sheep_observations = pd.merge(sheep_species, observations)
print(sheep_observations)

obs_by_park = sheep_observations.groupby('park_name').observations.sum().reset_index()
print(obs_by_park)

# Plotting Sheep Sightings
plt.figure(figsize=(16,4))
ax = plt.subplot()
plt.bar(range(len(obs_by_park)), obs_by_park.observations.values)
ax.set_xticks(range(len(obs_by_park)))
ax.set_xticklabels(obs_by_park.park_name.values)
plt.ylabel('Number of Observations')
plt.title('Observation of Sheep per Week')
plt.show()



# Foot and Mouth Reduction Effort - Sample Size Determination
baseline =  15 #recorded last year was 15%

minimum_detectable_effect = 100*5./15
print(minimum_detectable_effect)

sample_size_per_variant = 870

yellowstone_weeks_observing = sample_size_per_variant/507.0 
#Yellowstone National Park
print(yellowstone_weeks_observing )

bryce_weeks_observing = sample_size_per_variant/250.0
# sample_size_per_variant
print(bryce_weeks_observing)

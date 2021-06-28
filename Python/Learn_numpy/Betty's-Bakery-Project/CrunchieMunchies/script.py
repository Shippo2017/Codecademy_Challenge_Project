import numpy as np

calories_stats = np.genfromtxt('cereal.csv', delimiter=',')
print(calories_stats)

average_calories = np.mean(calories_stats)
print(average_calories)

calories_stats_sorted = np.sort(calories_stats)
print(calories_stats_sorted)

median_calories = np.median(calories_stats)
print(median_calories)

nth_percentile = np.percentile(calories_stats, 4)
print(nth_percentile)

more_calories = np.mean(calories_stats > 60)
print(more_calories) #96.10..%

calories_std = np.std(calories_stats)
print(calories_std)

print(len(calories_stats))

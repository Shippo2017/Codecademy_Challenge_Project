import csv
import statistics


# Read CSV
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    count = 0
    for row in file_read:
        print(row)
        if count > 9:
            break
        count += 1


# Find out the average age of the patients in the dataset.
ages = []
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    for row in file_read:
        ages.append(int(row['age']))

def avg_age(age):
    return sum(age)/len(age)

print("The average age of the patients in the dataset, " + str(round(avg_age(ages), 2)) + " years.")


# Analyze where a majority of the individuals are from
regions = []
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    for row in file_read:
        regions.append(row['region'])

def count_region(region):
    regions_num = {}  
    for i in regions:
        regions_num[i] = regions_num.get(i, 0)+1
    return regions_num

print(count_region(regions))
print("Region with the biggest members are " + str(statistics.median_high(count_region(regions))))


# The different costs between smokers vs. non-smokers
smokers_charges = []
non_smokers_charges = []
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    for row in file_read:
        if row['smoker'] == 'yes':
            smokers_charges.append(float(row['charges']))
        elif row['smoker'] == 'no':
            non_smokers_charges.append(float(row['charges']))

print("The average charges of smokers, " + str(round(statistics.mean(smokers_charges), 2)))
print("The average charges of smokers, " + str(round(statistics.mean(non_smokers_charges), 2)))

# The average age is for someone who has at least one child in this dataset.
ages_at_least_one_child = []
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    for row in file_read:
        if int(row['children']) >= 1:
            ages_at_least_one_child.append(int(row['age']))
        
print("The average age is for someone who has at least one child in this dataset, " + 
    str(round(statistics.mean(ages_at_least_one_child), 2)))


# Average cost of medical insurance by region
charges = []
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    charges.append(float(row['charges']))

    southwest = []
    southeast = []
    northwest = []
    northeast = []

    for row in file_read:
        if row['region'] == 'southwest':
            southwest.append(float(row['charges']))
        elif row['region'] == 'southeast':
            southeast.append(float(row['charges']))
        elif row['region'] == 'northwest':
            northwest.append(float(row['charges']))
        elif row['region'] == 'northeast':
            northeast.append(float(row['charges']))

regions_charges_dict = {}
regions_charges_dict['southwest'] = statistics.mean(southwest)
regions_charges_dict['southeast'] = statistics.mean(southeast)
regions_charges_dict['northwest'] = statistics.mean(northwest)
regions_charges_dict['notheast'] = statistics.mean(northeast)
print(regions_charges_dict)
print("Region with the most expensive insurance charges is " + 
    str(statistics.median_high(regions_charges_dict)))

# The difference in the average cost between male and female patients
sexes = []
with open('insurance.csv') as csv_file:
    file_read = csv.DictReader(csv_file)
    sexes.append(row['sex'])

    males = []
    females = []

    for row in file_read:
        if row['sex'] == 'male':
            males.append(float(row['charges']))
        elif row['sex'] == 'female':
            females.append(float(row['charges']))

avg_males = round(statistics.mean(males))
avg_female = round(statistics.mean(females))
diff_charges = avg_males - avg_female
print("Average charges for male is " + str(avg_males))
print("Avearge charges for females is " + str(avg_female))
print("Different charges between male and female are " + str(diff_charges))

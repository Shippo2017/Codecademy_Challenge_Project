medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""


# Working with string
# print(medical_data)

update_medical_data = medical_data.replace('#', '$')
# print(update_medical_data)

# Calculate the number of Medical Records
num_records = 0

for cost in update_medical_data:
  if cost == "$":
    num_records += 1
# print("There are "+str(num_records)+" medical records in the data.")


#Splitting string
medical_data_split = update_medical_data.split(';')
# print(medical_data_split)

medical_records = []

for record in medical_data_split:
  medical_records.append(record.split(','))  
# print(medical_records)


# Cleaning Data
medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
# print(medical_records_clean)

# Analyzing data

# Print Only Name
# for name in medical_records_clean:
#   print(record[0])

# Name Uppercase
# for name in medical_records_clean:
#   name[0] = name[0].upper()
#   # print(name[0])

# extra - only first name
for name in medical_records_clean:
  name[0] = name[0].split()[0]
print(name[0])

# Separate out all
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print("Names: "+str(names))
print("ages: "+str(ages))
print("bmis: "+str(bmis))
print("insurance_costs: "+str(insurance_costs))

# Average BMI
total_bmi = 0

for bmi in bmis:
  total_bmi += float(bmi)
print(total_bmi)

average_bmi = total_bmi / len(bmis)
print("Average BMI: "+str(average_bmi))

# extra 
# Average Insurance Cost
# Remove dollar sign
update_insurance_costs = []

for record in insurance_costs:
  update_insurance_costs.append(record.strip("$"))
print("Insurance costs: "+str(update_insurance_costs))

# Calculate Cost 
total_cost = 0

for cost in update_insurance_costs:
  total_cost += float(cost)
print(total_cost)

average_cost = total_cost / len(update_insurance_costs)
print("Average insurance costs: "+str(average_cost))

# Output string for individual
for i in range(0, len(medical_records_clean)):
  print("{} is {} years old with a BMI of {} and an insurance cost of {}.".format(names[i], ages[i], bmis[i], insurance_costs[i]))

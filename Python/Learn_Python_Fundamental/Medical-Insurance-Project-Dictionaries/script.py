# Storing patient names and insurance costs
medical_costs = {}

# Add
medical_costs["Marina"] = 6607.0 
medical_costs["Vinay"] = 3225.0
# Add
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
print(medical_costs)
# Update
medical_costs["Vinay"] = 3325.0
print(medical_costs)


# Calculate Average
total_cost = 0

for cost in medical_costs.values():
  total_cost += cost
print(total_cost)

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: "+str(average_cost))


# List Comprehension to Dictionary
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"] 
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {name:age for name, age in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get("Marina", "None")
print("Marina's age is "+str(marina_age))


# Create a Medical Database
medical_records = {}

# Add
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Issac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)

# Access Connie
connies_insurance_cost = medical_records["Connie"]["Insurance_cost"]
print("Connie's insurance cost is "+str(connies_insurance_cost)+" dollars.")

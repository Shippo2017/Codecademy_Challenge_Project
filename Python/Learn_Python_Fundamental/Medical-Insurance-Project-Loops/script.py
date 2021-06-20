names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
# Creating a for Loop
total_cost = 0

# Extra (convert to while)
# for cost in actual_insurance_costs:
#   total_cost += cost
# print(total_cost)
i = 0
while i < len(actual_insurance_costs):
  total_cost += actual_insurance_costs[i]
  i+=1
  print(total_cost)

average_cost = total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + "dollars.\n")

# Range in Loop 
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  change_cost = actual_insurance_costs[i] - average_cost # extra
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")

# COnditions inside a Loop
  if insurance_cost > average_cost:
    print("The insurance cost for "+name+" is "+str(change_cost)+" above average.")
  elif insurance_cost < average_cost:
    print("The insurance cost for "+name+" is "+str(change_cost)+" below average.")
  else:
    print("The insurance cost for "+name+" is equal to the average.")

# Creating List Comprehension
update_estimated_costs = [num*11/10 for num in estimated_insurance_costs]
print(update_estimated_costs)

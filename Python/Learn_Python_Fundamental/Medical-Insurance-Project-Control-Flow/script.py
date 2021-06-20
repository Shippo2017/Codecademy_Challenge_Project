# Add your code here
# Analyzing Smoker Status
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

# Analyzing BMI
def analyze_bmi(bmi_value):
  bmi_adjustment = bmi_value - 25 #extra
  if bmi_value > 30: 
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI by " + str(bmi_adjustment) + " points" + "\n")
  elif (bmi_value >= 25) and (bmi_value <= 30):
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI by " + str(bmi_adjustment) + " points" + "\n")
  elif (bmi_value >= 18.5) and (bmi_value < 25):
    print("Your BMI is in a healthy range.\n")
  elif bmi_value < 18.5:
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.\n")
      
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost

# EXTRA : Use try and except statements to build error control into your code
try:
# Estimate Keanu's insurance cost
  keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi = 26.2, num_of_children = 3, smoker = 1 )

# Estimate my insurance cost
  my_insurance_cost = estimate_insurance_cost(name = 'Shippo', age = 33, sex = 1, bmi = 23.6, num_of_children = 2, smoker = 0)
  
except Exception:
  print("Oops! did you add all your data?")

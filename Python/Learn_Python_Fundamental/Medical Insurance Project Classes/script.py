class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker
    try:
      int_age = int(self.age)
    except ValueError:
      print("Only whole number")

  # Method (Calculate cost)
  def estimated_insurance_cost(self):
    try:
      estimated_cost = 250*self.age\
                    - 128*self.sex\
                    +370*self.bmi\
                    + 425*self.num_of_children\
                    + 24000*self.smoker\
                    - 12500
      print(self.name + "'s estimated insurance cost is " + str(estimated_cost) + " dollars.")
    except TypeError:
      print("Are your entries whole number for age, sex, bmi, number of children and smoker numeric?")

  # Method (Update age)
  def update_age(self, new_age):
    self.age = new_age
    self.estimated_insurance_cost()
    print(self.name + " is now " + str(self.age) + " years old.")

  # Method (Modify num_of_childre)
  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    self.estimated_insurance_cost()

    if self.num_of_children == 1:
      print(self.name + " has " + str(self.num_of_children) + " child.")
    else:
      print(self.name + " has " + str(self.num_of_children) + " children.")

  # Method (Update BMI)
  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    self.estimated_insurance_cost()
    print(self.name + " has new bmi:" + str(self.bmi))

  # Method (Update smoker)
  def update_smoking_status(self, new_smoker):
    self.smoker = new_smoker
    if self.smoker == 1:
      print(self.name + " is now a smoker")
    else:
      print(self.name + " is not smoker")
    self.estimated_insurance_cost()

  # Method (extra- update list patient)
  def patient_profile(self):
    return f"""
    Name: {self.name} 
    Age: {self.age}
    Sex: {self.sex} 
    BMI: {self.bmi} 
    Number of Children: {self.num_of_children}  
    Smoker: {self.smoker}
    """

patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
patient1.update_age(26)
patient1.update_num_children(1)
patient1.update_bmi(20)
patient1.update_smoking_status(2.3)
print(patient1.patient_profile())
patient1.estimated_insurance_cost()

patient2 = Patient("Jane Doe", "azzz", 0, 23.1, 0, 0)
print(patient2.patient_profile())
patient2.estimated_insurance_cost()

# print(patient1.name)
# print(patient1.age)
# print(patient1.sex)
# print(patient1.bmi)
# print(patient1.num_of_children)
# print(patient1.smoker)

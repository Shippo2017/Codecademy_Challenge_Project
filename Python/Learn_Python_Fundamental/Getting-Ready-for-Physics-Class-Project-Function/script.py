# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below: 

# Turn up the Temperature
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp 

f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Use the Force
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print('The GE train supplies '+ str(train_force) + ' Newtons of force.')

def get_energy(mass, c):
  return mass * c ** 2

bomb_energy = get_energy(bomb_mass, c=3*10**8)
print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules.')

# Do the Work
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)
print('The GE trains does ' + str(train_work) + ' Joules of work over '  + str(train_distance) +  ' meters.')

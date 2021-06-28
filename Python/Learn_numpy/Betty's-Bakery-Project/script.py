import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print(cupcakes)

# Load this file into a variable called recipes
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

# Select all elements from the 3rd column and save them to the variable eggs
eggs = recipes[:, 2]
print eggs

# Which recipes require exactly 1 egg? Use a logical statement to get True or False for each value of eggs
one_egg = recipes[(eggs == 1)]
print(one_egg)

# You already have a variable for cupcakes. Create a variable for cookies with the data from the 3rd row
cookies = recipes[2 ,:]
print(cookies)

# Get the number of ingredients for a double batch of cupcakes 
double_batch = cupcakes * 2
print(double_batch)

# adding cookies and double_batch
grocery_list = cookies + double_batch
print(grocery_list)

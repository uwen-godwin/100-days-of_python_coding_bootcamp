# The code above converts the input into an array seperating
# each name in the input by a comma and space.

names_string = input("Enter names separated by commas: ")
names = names_string.split(", ")

# import function
import random

# Get the total number of items in the list
numb_list = len(names)

# Generate random numbers between 0 and the last index
random_names = random.randint(0, numb_list - 1)

# Choose and print a random name to buy the meal
print(f"{names[random_names]} is going to buy the meal today!")

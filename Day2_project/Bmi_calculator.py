# A program that calculates the Body Mass Index (BMI)
# from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount,
# the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg)
# by the square of their height (in m):

# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
my_height = float(height)
my_weight = int(weight)
bmi = my_weight / my_height ** 2

my_bmi = int(bmi)

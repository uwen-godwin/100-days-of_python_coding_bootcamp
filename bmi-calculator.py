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

print(my_bmi)
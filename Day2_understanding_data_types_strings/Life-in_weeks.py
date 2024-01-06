# A program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
print("Please enter your age")
age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years = 90 - int(age)
weeks = years * 52
print(f"You have {weeks} weeks left.")

# a program that adds the digits in a 2 digit number. e.g. 
# if the input was 35, then the output should be 3 + 5 = 8
# It then prompt the user to continue, if yes, the program repeat again.

print("Welcome to the arena of concatenation")
two_digit_number = input("Please enter a 2 digit number: ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
first_number = int(two_digit_number[0])

second_number = int(two_digit_number[1])

print(first_number + second_number)

print("Do you want to continue concatenating? 'Y', or 'N' ")
concat = input()
if concat == "Y":
    print("Welcome to the arena of concatenation again.")
    two_digit_number = input("Please enter a 2 digit number: ")
    first_number = int(two_digit_number[0])
    second_number = int(two_digit_number[1])
    print(first_number + second_number)
    print("Thank you for concatenating")
else:
    print("Bye for now")


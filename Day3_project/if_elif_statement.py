# A simple program that checks your height to determine if you can ride a rollercoaster.
# It then checks for your age to determine how much you can pay for the ride,
# if your height is good enough.

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride th rollercoater")
    age = int(input("What is your age? "))
    if age > 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry! you have to grow toller before you can ride the rollercoaster.")

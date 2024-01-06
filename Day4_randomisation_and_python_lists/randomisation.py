# A program that provides functions for generating pseudorandom numbers.
# It provides functions for generating pseudorandom numbers.mport random

print("Welcome to the world of randomisation")
import random
# Generate random integer numbers between 10 and 20
random_integer = random.randint(10, 20)
print(random_integer)

# Generate random floating numbers between 0 and 5
randomfloat = random.random() * 5
print(randomfloat)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

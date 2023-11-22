import random

i = 100
j = int(20e7)  # Convert float to integer (20 million)

# Generates a random number between i and j using randrange()
a = random.randrange(i, j)

# Generates a random number between j and i using randrange()
b = random.randrange(j - i) + i

# Generates a random integer between 100 and 200 using randint()
c = random.randint(100, 200)

# Generates a random integer between 100 and 200 using randint()
d = random.randint(100, 200 - 100) + 100

print('i =', i, ' and j =', j)
print('randrange() generated number:', a)
print('randrange() generated number (reversed range):', b)
print('randint() generated number:', c)
print('randint() generated number (reversed range):', d)


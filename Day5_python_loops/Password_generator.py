#Password Generator Project

# This line imports the random module, which is used to generate random values.
import random

# These lines define three lists: letters, numbers, and symbols. These lists contain lowercase letters, numbers, and symbols that can be used to create a password.
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# The program prints a welcome message and then prompts the user to input the number of letters, symbols, and numbers they want in their password.
print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 

nr_symbols = int(input("How many symbols would you like?\n"))

nr_numbers = int(input("How many numbers would you like?\n"))

# This part creates an empty list password_characters and uses the random.choices() function to randomly select characters from the specified lists (letters, symbols, and numbers). The k parameter determines the number of characters to choose.
password_characters = []
password_characters.extend(random.choices(letters, k=nr_letters))
password_characters.extend(random.choices(symbols, k=nr_symbols))
password_characters.extend(random.choices(numbers, k=nr_numbers))

# This line shuffles the characters in the password_characters list. This step adds an extra layer of randomness to the password.
random.shuffle(password_characters)

# The characters in the password_characters list are joined together to form the final password.
password = "".join(password_characters)

# Finally, the program prints the generated password using f-string.
print(f"Your password is: {password}")

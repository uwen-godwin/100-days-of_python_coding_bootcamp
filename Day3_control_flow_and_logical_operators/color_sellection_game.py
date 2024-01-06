# A program that uses your color choices to determine your wine

print("Welcome to G-roll game!")

color = input("What is your favorite color? Green, White, Yellow, or Red: ").lower()

if color == "green":
    print("Sorry! You can't continue.")
elif color == "white":
    print("You just got started.")
elif color == "red":
    print("Game over.")
elif color == "yellow":
    print("You win. Welcome champion")
else:
    print("Color does not exist. Please try again.")


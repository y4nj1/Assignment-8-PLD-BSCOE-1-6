# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

from random import randrange
min = 0
max = 100


randNum = randrange(min, max)

# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count >= 0:
    count = count
 
    # taking guessing number as input
    userGuess = int(input("Pick a number from {} through {}: ".format(min, max)))
 
    # Condition testing
    if (randNum == userGuess):
        count = count + 1
        print(f"Congratulations! you got the generated number, {randNum}. You did it in {count} tries.")
        # Once guessed, loop will break
        break
    elif (randNum > userGuess):
        print("The number you guessed is less than the generated number. Try again.")
    elif (randNum < userGuess):
        print("The number you guessed is greater than the generated number. Try again.")
    count = count + 1

# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random
min = 0
max = 100

randNum = sorted(random.sample(range(min, max)))
userGuess = int(input("Guess the number here:"))
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You lose” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

win_d1 = random.randint(0, 9)
win_d2 = random.randint(0, 9)
win_d3 = random.randint(0, 9)
win_c = [win_d1, win_d2, win_d3]

inp_d1 = int(input("Enter your first number here: "))
inp_d2 = int(input("Enter your second number here: "))
inp_d3 = int(input("Enter your third number here: "))
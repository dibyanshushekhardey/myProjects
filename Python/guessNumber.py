import math
import random

# take the inputs in the form of upper and lower bounds
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# now the machine will randomly generate the number to be gussed 
# by the user in the range of upper and lower bound
# that the user gave
# not included the upper and lower bound

# use of random module

x = random.randint(lower, upper)
print("\n\tYou have only ", 
round(math.log(upper-lower+1, 2)), " chances to guess the integer!\n")

# let us initialise the number of guesses using a variable count
count = 0

# to calculate the minikmum number of guesses will depend upon range
while count < math.log(upper-lower+1, 2):
    count += 1
    # take the guess from the user as input
    guess = int(input("Guess a number: "))
    # test the condition
    if x == guess:
        print("\tCongratulation player! you did it in ", count, " try")
        # break the loop if the guess is correct
        break
    elif x > guess:
        print("Sorry! you guessed it too small!")
    elif x < guess:
        print("Sorry! You guessed it too large!")

# Be mindful that number of guesses dhould not br more that the required guess
# apply the conditio to it
if count >= math.log(upper - lower +1, 2):
    print("\nThe number is %d", x)
    print("\tBetter luck next time!")

# Resources used
# https://www.geeksforgeeks.org/number-guessing-game-in-python/
# https://www.geeksforgeeks.org/python-random-module/#:~:text=Python%20Random%20module%20is%20an,a%20list%20or%20string%2C%20etc.
# https://www.w3schools.com/python/ref_math_log.asp

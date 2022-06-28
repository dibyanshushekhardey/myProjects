# import necessary modules
import random

print("\tGreetings user!\n")
name = input("Enter your name: ")
print("Good luck! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print("Guess the characters")

guesses = ''
turns = 8 # any number of turns can be used. I took the liberty of 8
while turns > 0:
    # count the number of times a user fails
    failed = 0

    for char in word:
        # check the the character is in guess basket
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            #print(char, end=" ")

            # for every fai;ure 1 will be incremented in failure
            failed += 1
    if failed == 0:
        # if failed is zero then the player wins
        # print the appropriate message
        print("You win User! ")
        # print the wrd that the user guessed correctly
        print("The word is: ", word)
        break
    
    # if user has guessed the input character wrong then
    # program will ask the user to enyter another alphabet
    print()
    guess = input("Guess a character: ")

    # every input character that user has guessed will be stored in guesses
    guesses += guess

    # check the input with the character in word
    if guess not in word:
        turns -= 1
        # if the character doesn't match the pwrd then wrong will be shown in putput
        print("Wrong")
        # then the number of turns left will be shown in the output
        print("You have", + turns,  "more guesses")

        if turns == 0:
            print("You loose")

# resources
# https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

# 1. Alex Fhermaye
# 2. Milestone 4
# 3. 3.11.4

import random
# 4. Create a variable named numbers. It needs to generate a number between 1 to 10.
# Put the answer on the next line. 
numbers = random.randint(1, 10)

# 5. Create a variable named player_name.  It needs to prompt the user to enter his/her name.
# Put the answer on the next line. 
player_name = input("What is your name? ")

# 6. Create a variable named number_of_guesses and assign 0 to it.
# Put the answer on the next line. 
number_of_guesses = 0 

# 7. Print a string which includes the player_name variable. It should say: player_name, I am guessing a number between 1 and 10!
# Put the answer on the next line. 
print(f"{player_name}, I am guessing a number between 1 and 10!")

# 8. Create a WHIlE Loop. Give the user 5 attempts to guess the number. If the number is too low print Your guess is too low. If the number is too high print Your guess is too high. Create a break if the user answers it correctly.
while number_of_guesses < 5:
    guess = int(input(f"{player_name}, what is your guess? "))
    number_of_guesses += 1

    if guess == numbers:
        print("You guessed right!")
        break
    elif guess > 10 or guess < 1: 
        print("Your guess is out of bounds! Please choose a number between 1 and 10.")
    elif guess > numbers:
        print("Your guess is too high!")
    elif guess < numbers:
        print("Your guess is too low!")
    
# 9. if/else Statements - Verifying if the user has guessed the number or not.. If they did...then print a message for them along with the number of tries. If the player couldnt guess the number at the end...print the number along with a message.
if guess == numbers:
    print(f"Good job {player_name}! You guessed {number_of_guesses} times.")
else:
    print(f"Wrong! The number was {numbers}... Sad sad times.")


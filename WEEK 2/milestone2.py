# Update the comments in the header 
# Edit the comments below this row 👇
# Alex Fhermaye
# Python Version 3.11.4
# Milestone 2


###### Import the random Module #####
import random
import time

###### Here are your list of Pirates #####
pirates = [
    'Anne Bonny',
    'Captain Henry Morgan',
    'Black Sam Bellamy',
    'Black Bart Roberts',
    'Edward Blackbeard Teach',
    'Captain William Kidd',
    'Pierre Le Grand',
    'Red Leg Grieves',
    'Edward Low',
    'Calico Jack Rackham'
]

#####  Attacks List #####
attack = ['dodge', 'parry', 'thrust']


##### Choosing the Characters for the fight #####
player = random.choice(pirates)
opponent = random.choice(pirates)

##### Announce Game Start #####
print("Ahoy ye swabs! Prepare for battle!")

print(f"{player} has challenged {opponent} in one on one combat!")

##### Initialize Scoring Variables ##### 
pscore = 0
oscore = 0
gameover = False
x = 1

# Create a loop that will run UNTIL either the player or opponent scores at least 3 points (WHILE LOOP GOES HERE)
# Write your code below this row 👇
while gameover == False:
    pattack = random.choice(attack)
    oattack = random.choice(attack)
    print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')

    if pattack == "dodge" and oattack == "parry":
        print(f"{player} wins this time!")
        pscore +=1
        time.sleep(2)
    elif pattack == "parry" and oattack == "thrust":
        print(f"{player} wins this time!")
        pscore +=1
        time.sleep(2)
    elif pattack == "thrust" and oattack == "dodge":
        print(f"{player} wins this time!")
        pscore +=1
        time.sleep(2)
    elif oattack == "dodge" and pattack == "parry":
        print(f"{opponent} wins this time!")
        oscore +=1
        time.sleep(2)
    elif oattack == "parry" and pattack == "thrust":
        print(f"{opponent} wins this time!")
        oscore +=1
        time.sleep(2)
    elif oattack == "thrust" and pattack == "dodge":
        print(f"{opponent} wins this time!")
        oscore +=1
        time.sleep(2)
    else:
        print("That was a tie!")
        time.sleep(2)

    print("\n")
    print(f"ROUND {x} ENDS")
    x += 1
    time.sleep(1)

    print("\n")
    print(f"{player} points: {pscore} and {opponent} points: {oscore}")
    print("\n")
    time.sleep(1.5)

# Create a conditional to determine if the player or opponent that will stop the loop if either reached a score of 3.
# Write your code below this row 👇

    if pscore == 3:
        print(f"\n{player} is the first to win 3 rounds!")
        time.sleep(1)
        print(f"\n{player} wins!")
        break

    elif oscore == 3:
        print(f"\n{opponent} is the first to win 3 rounds!")
        time.sleep(1)
        print(f"\n{opponent} wins!")
        break


# This code needs to be nested inside your loop 👇
# THINK: Recall that any code nested inside a loop will run each time the loop executes
##### Choosing the attack #####
# pattack = random.choice(attack)
# oattack = random.choice(attack)

# print(f'{player} attacks with {pattack}, while {opponent} attacks with {oattack}')

# Create a scoring system to record 1 point for each 'win' scored by either the player or the opponent
# HINT: You will need to use conditionals to compare the attacks
# HINT: You will need to update the score variables 
# Dodge beats Parry > Parry beats Thrust > Thrust beats Dodge
# Write your code below this row 👇


    # if pattack == "dodge" and oattack == "parry":
    #     print(f"{player} wins this time! {player}: {pscore} {opponent}: {oscore}")
    #     pscore +=1
    #     time.sleep(2)
    # elif pattack == "parry" and oattack == "thrust":
    #     print(f"{player} wins this time! {player}: {pscore} {opponent}: {oscore}")
    #     pscore +=1
    #     time.sleep(2)
    # elif pattack == "thrust" and oattack == "dodge":
    #     print(f"{player} wins this time! {player}: {pscore} {opponent}: {oscore}")
    #     pscore +=1
    #     time.sleep(2)
    # elif oattack == "dodge" and pattack == "parry":
    #     print(f"{opponent} wins this time! {player}: {pscore} {opponent}: {oscore}")
    #     oscore +=1
    #     time.sleep(2)
    # elif oattack == "parry" and pattack == "thrust":
    #     print(f"{opponent} wins this time! {player}: {pscore} {opponent}: {oscore}")
    #     oscore +=1
    #     time.sleep(2)
    # elif oattack == "thrust" and pattack == "dodge":
    #     print(f"{opponent} wins this time! {player}: {pscore} {opponent}: {oscore}")
    #     oscore +=1
    #     time.sleep(2)
    # else:
    #     print("\nThat was a tie!")
    #     time.sleep(2)

# Create a conditional outside of the loop to print the winner's name.
# Write your code below this row 👇

print("\n")
if pscore == 3:
    print(f"Congratulations {player}! You have defeated {opponent}!")
else:
    print(f"Congratulations {opponent}! You made {player} look bad.")
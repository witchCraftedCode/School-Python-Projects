# [Alex Fhermaye]
# [Python Version 3.11.4]
# [Nesting Loops & Complex Loops]


import random
import time

goodguy = str(input("Enter your Knight's Name: "))
goodguy = "Sir " + goodguy

# Here, we are assigning the value 'The Black Knight' to the variable badguy
# 1. CHANGE THE LINE BELOW SO THE USER CAN ENTER A VALUE FOR BADGUY
badguy = str(input("Enter the Black Knight's Name: "))
badguy = "Sir " + badguy

# Once Upon A Time...
print(goodguy + ", a Knight in search of adventure, is wandering through the enchanted forest one day.")

# 2. WHAT ACTION DOES time.sleep(2) PERFORM?
# A: This code delays what appears in the terminal by 2 seconds so that it looks like a brief pause
time.sleep(2)

print("As " + goodguy + " reaches a clearing, he encounters the fearsome " + badguy + "!")

time.sleep(2)

print(goodguy + ": You, Sir, are a Blackguard and a coward! I challenge you to a duel!")
print(badguy + ": I'mma cut you, fool!")

# Good Guy Health
gghealth = 100
# Bad Guy Health
bghealth = 100

# Fight Sequence Loop
while True:

    # 3. EXPLAIN HOW GOODGUY / BADGUY HIT POINTS ARE GENERATED
    # A: The hitpoints are being generated randomly by the code below. This code is pulling a random integer from 1 - 100 and using it to generate the hitpoint. 

    # Good Guy / Bad Guy Hit Points
    gghit = random.randint(1, 100)
    bghit = random.randint(1, 100)
    # #######################################################

    # 4. WHAT PURPOSE DOES '\n' SERVE?
    # A: "\n" serves as a space by moving the payload below but in this case of it being empty it is perceived as a space
    print("\n")

    # 5. FIND & CORRECT THE SYNTAX ERRORS. COMMENT OUT THE INCORRECT LINES AND
    # WRITE THE CORRECT CODE UNDERNEATH

    #print(goodguy + " rolls a " + gghit)
    #print(badguy + " rolls a " + bghit)

    print(goodguy + " rolls a " + str(gghit))
    print(badguy + " rolls a " + str(bghit))

    # 6. EXPLAIN HOW THE VALUE IN DAMAGE IS CALCULATED
    # A: When both characters roll, whichever is the highest is the attacker and damage is calculated by subtracting the attacker's roll minus the defender's roll
    # Damage Calculator
    if gghit > bghit:

        damage = gghit - bghit
        bghealth = bghealth - damage
        print(goodguy + " strikes " + badguy + " for a " + str(damage) + " hit!\n")

        if bghealth >= 100:
            print(badguy + ": Thou hast missed.\n")
        elif bghealth >= 75:
            print(badguy + ": Tis but a flesh wound.\n")
        elif bghealth >= 50:
            print(badguy + ": Alas! A fair strike! En garde!\n")
        elif bghealth >= 25:
            print(badguy + ": Thou art a worthy opponent.\n")
        elif bghealth < 10:
            print(badguy + ": I am beaten. Well fought...\n")
            break
    # #######################################################
    elif bghit > gghit:

        damage = bghit - gghit
        gghealth = gghealth - damage

        print(badguy + " strikes " + goodguy + " for a " + str(damage) + " hit!\n")

    # 7. CORRECT THE SYNTAX ERROR(S)
        if gghealth == 100:
            print(goodguy + ": Thou hast missed.\n")
        elif gghealth >= 75:
            print(goodguy + ": Tis but a flesh wound.\n")
        elif gghealth >= 50:
            print(goodguy + ": Alas! A fair strike! En garde!\n")
        elif gghealth >= 25:
            print(goodguy + ": Thou art a worthy opponent.\n")
        elif gghealth < 10:
            print(goodguy + ": I am beaten. Well fought...\n")
            break
    # #######################################################

# END OF LOOP ###############################################

# 8. PRINT A CONGRATULATORY STATEMENT HERE USING THE NAME OF THE WINNER (GOODGUY OR BADGUY)
if gghealth > bghealth:
    print(f"Congratulations {goodguy}! You are victorious!")
else:
    print(f"Congratulations {badguy}! You are the winner!")

time.sleep(2)

print("End of the Knight Fight\n")

# 9. PART 2
'''
In your own words, answer the following 4 questions on the use of the WHILE Loop in the script from Part 1:

HINT: The answer to #1 and #2 should not be the same.

    1. What Condition will end the WHILE Loop?  
    # - The condition that ends the WHILE loop is break   

    2. How is that Condition handled in the code?
    # - break is executed when either the good knight or the bad knight's hitpoints(gghit or bghit) less than 10. After this condition is met, break stops the WHILE loop

    3. What events happen inside the WHILE Loop?
    # - Inside the WHILE loop, we start off with gghit and bghit being set to roll a random number between 1 - 100 including the 100 and then we start the two main if statements where it is determined by the random number roll who attacks in this turn and by subtracting both random number rolls we get the actual damage to the character who is defending. When either one of both knight's health reaches less than 10, it determines that the other knight is the winner and breaks the loop. 

    4. Why are gghealth & bghealth initially set outside the WHILE Loop?
    # - they are placed outside the WHILE loop because we want them to be unaffected by the loop and not mess anything up in the loop and if they were in the loop then the health would constantly be resetting. 


'''

#### CHECKLIST ####

# (x) Use input() to allow the user to name the badguy.                   
# (x) Explain what is happening with time.sleep(2).
# (x) Explain how goodguy and badguy hit points are generated.
# (x) What purpose does '\n' serve?
# (x) Locate & Correct the syntax errors.
# (x) Explain how the value in damage is calculated.
# (x) Correct the syntax error in the last conditional statement.
# (x) Print a congratulatory statement using the name of the winner (either goodguy or badguy).


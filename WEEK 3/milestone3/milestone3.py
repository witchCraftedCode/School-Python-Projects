# Alex Fhermaye
# Python version 3.11.4
# Pirate Swashbuckle Fight Milestone 3
import time

# 1. Import the utilities file
import utilities

# 2. Import the pirates.txt file
pirates = utilities.importify('pirates.txt')

# dodge > parry > thrust > dodge
attack =['dodge', 'parry', 'thrust']

# 3. Use the utilites to randomly pick pirates for player and opponent
player = utilities.randopick(pirates)
opponent = utilities.randopick(pirates)

# 4. Add a while loop so that the pirates are not the same
while player == opponent:
    opponent = utilities.randopick(pirates)

print ("Advast ye swabs, a fight betwixt \n" + player + " & " + opponent + " 'tis bout to commence! ")
time.sleep(1)

pscore = 0
oscore = 0
gameover = False

while gameover == False:
    # This has changed for milestone 3. The game will still end when the player or opponent reaches 3. 
    if pscore >= 3:
        print (player + " has vanquished " + opponent)
        time.sleep(1.2)
        print ("Hip hip huzzah!")
        gameover = True
        break
    elif oscore >= 3:
        print (opponent + " has vaquished " + player)
        time.sleep(1.2)
        print ("Oh Captain, my Captain!")
        gameover = True
        break
    # 5. Exception - Add a while True and exception. 
    # Example: the player attack variable should allow the user to pick between the different types     
    while True:
        try:
            pattack = int(input("Select attack: \n [1] Dodge, [2] Parry, [3] Thrust \n Enter: "))
            if pattack > 0 and pattack < 4:
                break
            else:
                print("You can't follow instructions whippersnapper!\n Try again! ")
        except ValueError:
            print("You can't follow instructions whippersnapper!\n Try again! ")


    # 6. Player only - Create an if/elif statement to set the number entry to the correct attack.
    if pattack == 1:
        pattack = 'dodge'
    elif pattack == 2:
        pattack = 'parry'
    elif pattack == 3:
        pattack = 'thrust'

    # The program randomly picks the attack for the opponent
    oattack = utilities.randopick(attack)

    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    while pattack == oattack:
        oattack = utilities.randopick(attack)

    print (player + " attacks with a " + pattack)
    time.sleep(1)
    print (opponent + " attacks with a " + oattack)
    time.sleep(1)

    # 8. Change your if/elif statment from milestone 2. Use the and to compare the attacks. All attacks must be used correctly.
    if pattack == 'dodge' and oattack == 'parry':
        print("\n")
        print(f"{player} defeats {opponent}")
        pscore +=1
    elif pattack == 'parry' and oattack == 'thrust':
        print("\n")
        print(f"{player} defeats {opponent}")
        pscore +=1
    elif pattack == 'thrust' and oattack == 'dodge':
        print("\n")
        print(f"{player} defeats {opponent}")
        pscore +=1
    elif oattack == 'dodge' and pattack == 'parry':
        print("\n")
        print(f"{opponent} defeats {player}")
        oscore +=1
    elif oattack == 'parry' and pattack == 'thrust':
        print("\n")
        print(f"{opponent} defeats {player}")
        oscore +=1
    elif oattack == 'thrust' and pattack == 'dodge':
        print("\n")
        print(f"{opponent} defeats {player}")
        oscore +=1

        
    # 9. Print a string that includes the player and the players score.
    print("\n")
    print(f"{player}: {str(pscore)}")

    # 10. Print a string that includes the opponent and the opponents score.
    print(f"{opponent}: {str(oscore)}")
    print("\n")

### CHECKLIST ###
'''
1 = [x]
2 = [x]
3 = [x]
4 = [x]
5 = [x]
6 = [x]
7 = [x]
8 = [x]
9 = [x]
10 = [x]
'''
# Alex Fhermaye
# Python Version 3.11.4
# File Input/Output 

# Input / Output

# w write permissions
# w+ write permissions w\create blank doc
# r read only permission
# a append

#######################
# MLB TEAMS
#######################

# 2. The example below uses the old method of opening an external file.
# Convert the open() function below [line 19 - 22 ]to with open().

# Baseball Team Text file import
with open('mlb-teams.txt', 'r') as f:
    mlb = f.read().splitlines()
    f.close()


# 3. Replace the w+ with the appropriate option for appending the file.
with open('mlb-teams.txt', 'a') as f:
    
# 4.  Using the f.write() function, add three more teams to the list:
# [ Seattle Pilots, Washington Senators & Montreal Expos ]
    f.write("Seattle Pilots\n")
    f.write("Washington Senators\n")
    f.write("Montreal Expos\n")
    f.close()

#######################
# HALL OF FAME PLAYERS
#######################

favorite_baseball_player = "Old Hoss Radbourne\n"

with open('hall_of_fame.txt', 'w+') as f:
    f.write("Bobby Bonds\n")
    f.write("Al Kaline\n")
    f.write("Mickey Mantle\n")
    f.write("Willie Mays\n")

# 5. Using the f.write() funtion, add the player stored in
# favorite_baseball_player to the hall_of_fame.txt file
# Note: You MUST reference the variable in this part.

    f.write(favorite_baseball_player)
    f.write('\n')
    f.close()

# 6. Replace the r with the appropriate option for appending the file.
with open('hall_of_fame.txt', 'a') as f:
    
 # 7. Using the f.write() function, add 3 more players the list:
# [Babe Ruth, Willie Stargell & Roberto Clemente]
    f.write("Babe Ruth\n")
    f.write("Willie Stargell\n")
    f.write("Roberto Clemente\n")
    f.close()

# 8. Using with open(), place the values stored in hall_of_fame.txt into a variable called hof_players
# with open(hall_of_fame.txt)=-0p9gfcx  

hof_players = ''
with open('hall_of_fame.txt', 'r') as f:
    hof_players = f.read().splitlines()
    f.close()
    

# 9. Write a print statement below with the MLB Team closest to your Home Town.
print(mlb[18])

# 10. Write a print statement to print one of the players stored in the variable hof_players created in step 8.
print(hof_players[1])



### CHECKLIST ###

# [X] Comment headers
# [X] Covert the open() function to with open()
# [X] Replace the w+ with the correct option for appending to the file
# [X] Using f.write(), add the three teams specified to mlb-teams.txt
# [X] Using the f.write() function, add the player stored in the variable to hall_of_fame.txt
# [X] Replace the r with the correct option for appending to the file
# [X] Using the f.write() function, add the 3 players specified to hall_of_fame.txt
# [X] Import the data from hall_of_fame.txt into a variable called hof_players
# [X] Using the list index, print the MLB team closest to your hometown to the screen
# [X] Using the list index, print one of the players in the hof_players variable
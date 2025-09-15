# [ALEX FHERMAYE]
# Python Version 3.11.4
# Activity 2

# PART 1

# Strings
city = 'cape canaveral' 
nickname = 'thrusters'
# These two code lines 6 and 7 represent variables with a string stored in each 

# String Methods 
print("Welcome to " + city + " home of the " + nickname.capitalize())
# This print command will show two strings and two variables which will show "Welcome to cape canaveral home of the Thrusters"
# The string inside the nickname variable will show with the first letter capitalized because it is using a string method such as capitalize()

# Print to screen
name = input("Enter name: ")
# This variable is storing an input method where a user can enter data but it will not be stored
print("Introducing the latest " + nickname.title() + " player, " + name.title())
# Here we can see a printed combination of strings and variables where the variables have a string method called title() which makes the first letter of the string capitalized and the subsequent letters not capitalized 
# This will show "Introducing the latest Thrusters player, Alex" in terminal

#__________________________________________________________________________________

# PART 2 

String = "Hello"
Number = 2
List = [1,2,3]
Tuple = (1,2,3)
Dictionary = {1: "Kyle", 2: "Reese"}

car = input("What kind of car do you drive? ")

number_of_cars = int(input("How many cars do you have in your garage? "))

print("Wow! " + car + " is a slow car and " + str(number_of_cars) + " is NOT ENOUGH!")